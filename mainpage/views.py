from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import PersonalInfo, AdditionalInfo, Experience, WorkExperience, Portfolio, ContactMessage
from .serializers import (
    PersonalInfoSerializer,
    AdditionalInfoSerializer,
    ExperienceSerializer,
    WorkExperienceSerializer,
    PortfolioSerializer,
    ContactMessageSerializer
)


def main_banner(request):
    context = {
        "main_info": PersonalInfo.objects.all(),
        "additional": AdditionalInfo.objects.all(),
        "experience": Experience.objects.all(),
        "work_experience": WorkExperience.objects.all(),
        "leadership": WorkExperience.objects.filter(leadership=True),
        "portfolio": Portfolio.objects.all(),
    }
    return render(request, "base.html", context)


class PersonalInfoListCreateAPIView(ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


class AdditionalInfoListCreateAPIView(ListAPIView):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoSerializer


class ExperienceListCreateAPIView(ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class WorkExperienceListCreateAPIView(ListAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class PortfolioListCreateAPIView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ContactMeAPIView(CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
