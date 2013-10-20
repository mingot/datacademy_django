from django.views.generic import ListView, DetailView
from .models import Course, Lecture, Exercise


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'


class CourseDetail(DetailView):
    model = Course
    context_object_name = 'course'


class LectureList(ListView):
    model = Lecture
    context_object_name = 'lecture_list'


class LectureDetail(DetailView):
    model = Lecture
    context_object_name = 'lecture'

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
