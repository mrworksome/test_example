from django.conf.urls import url

from my_app.views import IndexView
app_name = 'my_app'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(.*)/$', IndexView.as_view(), name='index'),
]