from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from .models import Course, Lecture, Exercise


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'

    def get_queryset(self):
        # Show only the courses the current user is enrolled in
        profile = self.request.user.get_profile()
        return profile.courses.all()


class CourseDetail(DetailView):
    model = Course
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        # Save the course in the user courses
        context = super(CourseDetail, self).get_context_data(**kwargs)
        profile = self.request.user.get_profile()
        context['is_enrolled'] = False
        if profile.courses.filter(id=self.object.pk).exists():
            context['is_enrolled'] = True
        return context


class LectureList(ListView):
    model = Lecture
    context_object_name = 'lecture_list'


class LectureDetail(DetailView):
    model = Lecture
    context_object_name = 'lecture'

    def get_context_data(self, **kwargs):
        # Save the course in the user courses
        context = super(LectureDetail, self).get_context_data(**kwargs)
        profile = self.request.user.get_profile()
        profile.courses.add(self.object.course)
        profile.save()
        return context

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(LectureDetail, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['element_active'] = self.object
    #     return context


class ExerciseList(ListView):
    model = Exercise
    context_object_name = 'exercise_list'


class ExerciseDetail(DetailView):
    model = Exercise
    context_object_name = 'exercise'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ExerciseDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lecture'] = self.object.lecture
        context['element_active'] = self.object
        return context


def lecture_discussion(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    return render_to_response('courses/course_discussion.html',
                              {'lecture': lecture},
                              context_instance=RequestContext(request))

