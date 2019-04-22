from rest_framework.routers import DefaultRouter

from app_ex.Mercury import views

router = DefaultRouter()

# router.register(r'user_home', views.UserHtmlViewSet, base_name="user_home")

urlpatterns = router.urls
