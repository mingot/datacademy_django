from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from userena import views as userena_views
from accounts import forms as accounts_forms


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='home'),
    url(r'^rserver$', TemplateView.as_view(template_name='rserver.html'),
        name='rserver'),

    # url(r'^about/$', TemplateView.as_view(template_name='about.html'),
    #     name="about"),
    # url(r'^contact/$', TemplateView.as_view(template_name='contact.html'),
    #     name="contact"),
    # url(r'^videostream/', include('videostream.urls')),
    # url(r'^detectors/', include('detectors.urls')),

    # userena app
    # edit profile (overriding)
    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$',
        userena_views.profile_edit,
        {'edit_profile_form': accounts_forms.EditDatacademyProfileForm},
        name='userena_profile_edit'),
    (r'^accounts/', include('userena.urls')),

    # courses app
    (r'^courses/', include('courses.urls')),

    # news app
    (r'^news/', include('news.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Allow access to the Media folder from the browser
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
            }),
    )
