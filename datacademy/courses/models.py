import time
from django.db import models


class CommonInfo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        abstract = True
        ordering = ['title']

    def __unicode__(self):
        return u'%s' % self.title


class Course(CommonInfo):
    LEVEL_CHOICES = (
        ('Beginner', 'beginner'), 
        ('Intermediate', 'intermediate'), 
        ('Advanced', 'advanced')
        )

    short_description = models.CharField(max_length=150)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    date = models.DateField()
    author = models.ForeignKey('accounts.Teacher')

    @property
    def duration(self):
        # Total number of seconds of video that the course have
        lectures = self.lecture_set.all()
        duration = 0
        for lecture in lectures:
            duration += lecture.video_duration
        return duration

    def duration_formatted(self):
        return time.strftime('%H:%M:%S', time.gmtime(self.duration))


class Lecture(CommonInfo):
    number = models.PositiveSmallIntegerField()
    course = models.ForeignKey('Course')
    slides = models.FileField(upload_to='lectures/',
                              blank=True,
                              null=True)
    video = models.TextField(blank=True,
                             null=True)
    video_duration = models.IntegerField(blank=True, null=True,
                                         verbose_name='Video duration(s)')

    class Meta:
        ordering = ['number']

    def video_duration_formatted(self):
        return time.strftime('%H:%M:%S', time.gmtime(self.video_duration))

    # def next_lecture(self):
    #     next = Lecture.objects.filter(course=self.course).\
    #         filter(number__gt=self.number).order_by('number')[0:1]
    #     return next


class Exercise(CommonInfo):
    number = models.PositiveSmallIntegerField()
    lecture = models.ForeignKey('Lecture')
    initial_code = models.TextField()
    hint = models.TextField()
    unit_test = models.TextField()

    class Meta:
        ordering = ['number']


