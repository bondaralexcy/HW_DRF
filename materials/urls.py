from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView,
                             SubscribtionCourseAPIView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("course", CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="create_lesson"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="retrieve_lesson"),
    path(
        "lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="update_lesson"
    ),
    path(
        "lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="delete_lesson"
    ),
    path("subscription/", SubscribtionCourseAPIView.as_view(), name="subscription"),
]
urlpatterns += router.urls
