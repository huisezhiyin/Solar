from rest_framework.routers import DefaultRouter

from app_ex.Mercury import views

router = DefaultRouter()

router.register(r'user', views.UserViewSet, base_name="user")
router.register(r'logged_user', views.LoggedUserViewSet, base_name="logged_user")

urlpatterns = router.urls
