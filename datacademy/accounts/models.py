from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from courses.models import Course, Lecture, Exercise


class DatacademyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    
    short_bio = models.TextField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)

    courses = models.ManyToManyField(Course, blank=True, null=True)
    lectures = models.ManyToManyField(Lecture, blank=True, null=True)
    exercises = models.ManyToManyField(Exercise, blank=True, null=True)


class Teacher(models.Model):
    profile = models.OneToOneField(DatacademyProfile, unique=True)
    years_experience = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=150)

    def __unicode__(self):
        return u'Teacher Mr. %s' % self.profile.user.last_name


