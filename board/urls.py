from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostsSearch.as_view(), name='post_search'),
    path('create/', PostsCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscribe/<int:pk>', subscribe_me, name='subscribe'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]