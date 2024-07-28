from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, CourseSubscription, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(
            title="DJANGO DRF", description="DJANGO DRF", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Lesson_1",
            description="Lesson_1",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_lesson(self):
        url = reverse("materials:retrieve_lesson", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_create_lesson(self):
        url = reverse("materials:create_lesson")
        data = {
            "title": "Lesson_2",
            "description": "Lesson_2",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_update_lesson(self):
        url = reverse("materials:update_lesson", args=(self.lesson.pk,))
        data = {"title": "New_lesson"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("title"), "New_lesson")

    def test_delete_lesson(self):
        url = reverse("materials:delete_lesson", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("materials:lessons_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.pk,
                        "title": self.lesson.title,
                        "description": self.lesson.description,
                        "preview": None,
                        "url": None,
                        "course": self.lesson.course.pk,
                        "owner": self.lesson.owner.pk,
                    }
                ],
            },
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.course = Course.objects.create(
            title="DRF", description="DRF", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title="Lesson_1",
            description="Lesson_1",
            course=self.course,
            owner=self.user,
        )
        self.subscription = CourseSubscription.objects.create(
            course=self.course, user=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse("materials:subscription")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "подписка удалена")
