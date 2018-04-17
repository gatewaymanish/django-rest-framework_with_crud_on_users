from django.conf.urls import url, include
from django.contrib import admin
from users import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('users.urls', namespace='users')),
    url(r'^$', views.api_root),

    
]
