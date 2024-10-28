from django.http import HttpResponse, JsonResponse
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


def test_view(request):
    send_test_email()
    return HttpResponse("Email отправлен!")


@csrf_exempt
def send_email_view(request):
    if request.method == "POST":
        data = json.loads(request.body)  # Получаем данные из POST-запроса
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        # Сформируйте сообщение для отправки
        full_message = f"Message from {name} ({email}):\n\n{message}"

        # Отправьте email
        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email="ExtroEdLive@gmail.com",  # Ваш email-отправитель
            recipient_list=["ExtroEdLive@gmail.com"],  # Ваш email-получатель
            fail_silently=False,
        )
        return JsonResponse({"status": "Email sent successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=400)