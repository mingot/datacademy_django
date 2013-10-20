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
    pass


class Lecture(CommonInfo):
    # number = models.PositiveSmallIntegerField()
    course = models.ForeignKey('Course')
    slides = models.FileField(upload_to='lectures/',
                              blank=True,
                              null=True)
    video = models.FileField(upload_to='lectures/',
                             blank=True,
                             null=True)

    # def next_lecture(self):
    #     next = Lecture.objects.filter(course=self.course).\
    #         filter(number__gt=self.number).order_by('number')[0:1]
    #     return next


class Exercise(CommonInfo):
    # number = models.PositiveSmallIntegerField()
    lecture = models.ForeignKey('Lecture')
    initial_code = models.TextField()
    hint = models.TextField()
    unit_test = models.TextField()


