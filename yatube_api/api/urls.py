from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentView, FollowView, GroupView, PostView

router = DefaultRouter()
router.register('posts', PostView)
router.register('groups', GroupView)
router.register('follow', FollowView, basename='followers')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentView, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
