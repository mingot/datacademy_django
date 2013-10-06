from django.conf.urls import patterns, url
from courses import views


# Patters for the API access.
urlpatterns = patterns(
    '',
    url(r'^$',
        views.CourseList.as_view(),
        name='course_list'),  #list courses
    # url(r'^(?P<pk>[0-9]+)/$', ),  #course detail - list lectures
    
    #list lectures for given course id
    url(r'^lectures/list/(?P<course>[0-9]+)/$',
        views.LectureList.as_view(),
        name='lecture_list'),

    #detail lecture for given lecture id
    url(r'^lectures/(?P<pk>[0-9]+)/$',
        views.LectureDetail.as_view(),
        name='lecture_detail'),

    #list lectures for given lecture id
    url(r'^exercises/list/(?P<lecture>[0-9]+)$',
        views.ExerciseList.as_view(),
        name='exercise_list'),
)
