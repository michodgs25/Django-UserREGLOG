from django.conf.urls import include, url, patterns

urlpatterns = patterns('myapp.views',
                       url(r'^hello/', 'hello', name='hello'),
                       url(r'^morning/', 'morning', name='morning'),)
