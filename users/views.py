from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsListAPIView(ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    # Фильтрация для эндпоинта вывода списка платежей
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    # фильтровать по курсу или уроку
    filterset_fields = (
        "course",
        "lesson",
    )
    # Порядок сортировки
    ordering_fields = ("date",)
    # фильтровать по способу оплаты
    search_fields = ("payment_method",)
