from django.urls import path
from .views import main_banner
from .views import (PersonalInfoListCreateAPIView, AdditionalInfoListCreateAPIView,
                    ExperienceListCreateAPIView, WorkExperienceListCreateAPIView, PortfolioListCreateAPIView)

urlpatterns = [
    path("", main_banner),
    path("personal-info/", PersonalInfoListCreateAPIView.as_view(), name="personal-info"),
    path("additional-info/", AdditionalInfoListCreateAPIView.as_view(), name="additional-info"),
    path("experience/", ExperienceListCreateAPIView.as_view(), name="experience"),
    path("work-experience/", WorkExperienceListCreateAPIView.as_view(), name="work-experience"),
    path("portfolio/", PortfolioListCreateAPIView.as_view(), name="portfolio"),
]
