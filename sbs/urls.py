from django.urls import path,re_path
from . import views
from .views import ( 
                    index,
                    add,
                    update,
                    delete,
                    i
                    #index,video_watch_view,liked_video,dislike_video,subscriber_view,video_comment, 
                   )


urlpatterns=[
   path('', i, name="home"),
   path('index', index, name="home"),
   path('accounts/profile/',index,name="home"),    path("add", add, name="edit"),
   path("edit/<int:id>/", views.update, name="edit"),
   path("delete/<int:id>/", views.delete, name="home"),
   path("filter",views.filter,name="j")
]