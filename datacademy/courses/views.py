from django.views.generic import ListView, DetailView
from .models import Course, Lecture, Exercise


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'


class LectureList(ListView):
    model = Lecture
    context_object_name = 'lecture_list'


class LectureDetail(DetailView):
    model = Lecture
    context_object_name = 'lecture'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(PublisherDetail, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['exercise_list'] = self.object.exercise_set.all()
    #     return context

class ExerciseList(ListView):
    model = Exercise
    context_object_name = 'exercise_list'

