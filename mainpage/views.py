from django.shortcuts import render

from .models import PersonalInfo, AdditionalInfo, Experience, WorkExperience, Portfolio
from rest_framework import generics
from .serializers import (PersonalInfoSerializer, AdditionalInfoSerializer,
                          ExperienceSerializer, WorkExperienceSerializer, PortfolioSerializer)


def main_banner(request):
    main_info = PersonalInfo.objects.all()
    additional = AdditionalInfo.objects.all()
    experience = Experience.objects.all()
    work_experience = WorkExperience.objects.all()
    portfolio = Portfolio.objects.all()
    leadership = WorkExperience.objects.filter(leadership=True)
    return render(
        request,
        "base.html",
        {
            "main_info": main_info,
            "additional": additional,
            "experience": experience,
            "work_experience": work_experience,
            "leadership" : leadership,
            "portfolio": portfolio
        }
    )


class PersonalInfoListCreateAPIView(generics.ListCreateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer

class AdditionalInfoListCreateAPIView(generics.ListCreateAPIView):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoSerializer

class ExperienceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class WorkExperienceListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class PortfolioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
