from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     RetrieveUpdateAPIView, UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import Payments, User
from users.permissions import IsOwner
from users.serializers import (PaymentsSerializer, SimpleUserSerializer,
                               UserSerializer)

# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#
#     def perform_create(self, serializer):
#         new_user = serializer.save(is_active=True)
#         new_user.set_password(self.request.data['password'])
#         new_user.save()

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner,)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # Разрешить авторизацию всем пользователям
    # не смотря на то, что на уровне проекта реализован доступ только для авторизованных пользователей
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """ Этот метод надо добавить, т.к. мы испортили стандартную модель User (пустое имя пользователя)"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SimpleUserSerializer

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner, IsAuthenticated)



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

class PaymentsRetrieveAPIView(RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsUpdateAPIView(UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsCreateAPIView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsDestroyAPIView(DestroyAPIView):
    queryset = Payments.objects.all()

