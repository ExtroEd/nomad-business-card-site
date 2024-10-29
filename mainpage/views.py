from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import PersonalInfo, AdditionalInfo, Experience, WorkExperience, Portfolio, ContactMessage
from .serializers import (
    PersonalInfoSerializer,
    AdditionalInfoSerializer,
    ExperienceSerializer,
    WorkExperienceSerializer,
    PortfolioSerializer,
    ContactMessageSerializer
)
from .smtp.sender import send_test_email
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json


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


class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


class AdditionalInfoViewSet(viewsets.ModelViewSet):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ContactMeAPIView(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


def test_view(request):
    send_test_email()
    return HttpResponse("Email отправлен!")


@csrf_exempt
def send_email_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email="ExtroEdLive@gmail.com",
            recipient_list=["ExtroEdLive@gmail.com"],
            fail_silently=False,
        )
        return JsonResponse({"status": "Email sent successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=400)
