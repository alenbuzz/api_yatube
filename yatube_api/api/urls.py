from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(
    'posts',
    PostViewSet,
    basename='post'
)
router.register(
    'groups',
    GroupViewSet,
    basename='group'
)
router.register(
    'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
