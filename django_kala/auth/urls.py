from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login
from .views import *


urlpatterns = [
   url(regex=r'^$',
       view=UsersView.as_view(),
       name='users',
   ),

   url(regex=r'^invite_user$',
       view=InviteUserView.as_view(),
       name='invite_user',
   ),

   url(regex=r'^(?P<pk>\d+)/settings/details$',
       view=DetailsView.as_view(),
       name='details',
   ),

   url(regex=r'^(?P<pk>\d+)/settings/avatar',
       view=AvatarView.as_view(),
       name='avatar',
   ),

   url(
       regex=r'^login/$',
       view=login,
       kwargs={'template_name': 'login.html'},
       name='login'
   ),
   url(
       regex=r'^logout/$',
       view=logout_then_login,
       kwargs={'login_url': '/accounts/login'},
       name='logout'
   ),
   #    url(r'^create_account$', CreateAccount.as_view(), name='create_account'),
   url(
       regex=r'^edit_profile/(?P<pk>\d+)/$',
       view=EditProfile.as_view(),
       name='edit_profile'
   ),
]
