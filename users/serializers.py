from rest_framework.serializers import ModelSerializer

from users.models import Payments, User


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):
    # + вывод истории платежей
    payments = PaymentsSerializer(source="payments_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class SimpleUserSerializer(ModelSerializer):
    """Простой сериалайзер"""

    class Meta:
        model = User
        fields = "__all__"
