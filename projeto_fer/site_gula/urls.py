from django.conf.urls import url
from . import views
#from django.contrib.auth_views import views as auth_views
from django.contrib.auth import views as auth_views
from django.conf.urls import include

handler400 = 'views.my_custom_bad_request_view'
handler403 = 'views.my_custom_permission_denied_view'
handler404 = 'views.my_custom_page_not_found_view'
handler500 = 'views.my_custom_error_view'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^graficos$', views.graficos, name='graficos'),
]
