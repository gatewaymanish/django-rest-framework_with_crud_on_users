from django.conf.urls import url,include
from .views import *


urlpatterns = [
    # url(r'^home/$', home, name='home'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
cd