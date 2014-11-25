from django.conf.urls import patterns, include, url
# from scholar_survey_app.views import foo
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scholar_survey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$','scholar_survey_app.views.index', name='index'),
)
