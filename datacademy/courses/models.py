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
    course = models.ForeignKey('Course')
    slides = models.FileField(upload_to='lectures/',
                              blank=True,
                              null=True)
    video = models.FileField(upload_to='lectures/',
                             blank=True,
                             null=True)


class Exercise(CommonInfo):
    lecture = models.ForeignKey('Lecture')
    initial_code = models.TextField()
    hint = models.TextField()
    unit_test = models.TextField()


