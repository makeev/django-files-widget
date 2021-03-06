try:
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf.urls import url

from topnotchdev.files_widget.views import upload, thumbnail_url

urlpatterns = [
    url(u'^upload/$', upload, name="files_widget_upload"),
    url(u'^thumbnail-url/$', thumbnail_url, name="files_widget_get_thumbnail_url"),
]
