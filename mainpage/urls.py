from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PersonalInfoViewSet,
    AdditionalInfoViewSet,
    ExperienceViewSet,
    WorkExperienceViewSet,
    PortfolioViewSet,
    ContactMeAPIView, main_banner,
)
from . import views


router = DefaultRouter()
router.register(r'personal-info', PersonalInfoViewSet)
router.register(r'additional-info', AdditionalInfoViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'work-experience', WorkExperienceViewSet)
router.register(r'portfolio', PortfolioViewSet)
router.register(r'contact-me', ContactMeAPIView)

urlpatterns = [
    path('', main_banner, name='main-banner'),
    path('api/', include(router.urls)),  # Добавляем маршруты из роутера
    path('test-email/', views.test_view, name='test-email'),
    path('send-email/', views.send_email_view, name='send-email'),
]
