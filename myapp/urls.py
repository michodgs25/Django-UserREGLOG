from django.conf.urls import (
    include, url,
    TemplateView)

urlpatterns = ('myapp.views',
               url(r'^connection/',
                   TemplateView.as_view(template_name='login.html')),
               url(r'^login/', 'login', name='login'))
