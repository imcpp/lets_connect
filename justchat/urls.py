from django.contrib import admin
from django.urls import path, include,re_path
from chat.views import *
from courses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post, name = 'index'),
    path('post/', post, name = 'post'),
    re_path('add_comment/(?P<pk>\d+)', add_comment, name = 'add_comment'),
    path("search/",search,name='search'),
    path("profile/",profile,name='profile'),
    path("signup/",signup,name="signup"),
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
    path('createpost/', create_post, name = 'create_post'),
    path('createnewpost/', create_new_post, name = 'create_new_post'),
    path('yourpost/', user_post, name = 'user_post'),
    re_path('delete_post/(?P<pk>\d+)', delete_post, name = 'delete_post'),
    path('chat/', include('chat.urls', namespace='chat')),
    path('courses/',home,name='home'),
    path('search1/',search1,name='search1'),
    path('rating/',rating,name='rating'),
    path('price/',price,name='price'),
]
