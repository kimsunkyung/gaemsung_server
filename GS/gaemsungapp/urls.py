from django.conf.urls import url

from gaemsungapp.views import *

urlpatterns = [
    url(r'^mypage/info/(?P<user_id>\d+)/$',get_mypage_info, name = "get_mypage_info" ),
    url(r'^mypage/user/(?P<user_id>\d+)/$',get_mypage_name, name = "get_user" ),
    url(r'^mypage/image/(?P<user_id>\d+)/$', get_mypage_img, name="get_mypage_img"),

]

