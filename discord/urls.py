
from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ServerViewSet, ChannelViewSet, RelationshipViewSet, MessageViewSet, UserCreate, PostMessageViewSet, PostServerViewSet
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings



router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('servers', ServerViewSet)
router.register('post-servers', PostServerViewSet)
router.register('channels', ChannelViewSet)
router.register('relationships', RelationshipViewSet)
router.register('messages', MessageViewSet)
router.register('post-messages', PostMessageViewSet)


urlpatterns = [
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)