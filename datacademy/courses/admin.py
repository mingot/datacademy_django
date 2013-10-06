from django.contrib import admin
from .models import Course, Lecture, Exercise


class LectureInline(admin.TabularInline):
    model = Lecture


class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureInline]


class ExerciseInline(admin.TabularInline):
    model = Exercise


class LectureAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Exercise)

