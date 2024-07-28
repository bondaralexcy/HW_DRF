from django.utils.decorators import method_decorator
# from materials.validators import validate_allow_site
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, CourseSubscription, Lesson
from materials.paginations import LessonCoursePaginator
from materials.serializers import (CourseSerializer, LessonSerializer,
                                   SubscriptionSerializer)
from users.permissions import IsModerator, IsOwner


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="description from swagger_auto_schema via method_decorator"
        # responses =
        # request_body =
    ),
)
class CourseViewSet(ModelViewSet):
    """ViewSet for Course"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LessonCoursePaginator

    def perform_create(self, serializer):
        """Метод создания записи
        используется для автоматического добавления владельца (через ViewSet)
        """
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """Метод ViewSet, который отвечает за доступ к данным"""
        if self.action == "create":
            self.permission_classes = (~IsModerator,)
        elif self.action == "list":
            self.permission_classes = (IsOwner | IsModerator,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (
                IsOwner,
                ~IsModerator,
            )
        return super().get_permissions()

    def perform_update(self, serializer):
        """Метод обновления данных о курсах"""
        course = serializer.save()
        # Здесь можно добавить действие при апдейте курса
        course.save()


class LessonCreateAPIView(CreateAPIView):
    """Generic-class CreateAPIView для модели Lessons"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        ~IsModerator,
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        """Метод используется для автоматического добавления владельца (через Generics)"""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        ~IsModerator,
        IsAuthenticated,
    )
    pagination_class = LessonCoursePaginator

    # def get_queryset(self):
    #     if self.request.user.groups.filter(name='moderators').exists():
    #         return Lesson.objects.all()
    #     return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsModerator | IsOwner,
    )


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsModerator | IsOwner,
    )


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )


class SubscribtionCourseAPIView(APIView):
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = (
            CourseSubscription.objects.all()
            .filter(user=user)
            .filter(course=course_item)
        )

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"

        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            CourseSubscription.objects.create(user=user, course=course_item)
            message = "подписка добавлена"

        # Возвращаем ответ в API
        return Response({"message": message})
