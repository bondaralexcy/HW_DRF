# from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from materials.validators import validate_allow_site
from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.CharField(validators=[validate_allow_site])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    # Добавил поле lessons_count - количество уроков
    lessons_count = serializers.SerializerMethodField()
    # Список уроков в курсе
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, instance):
        """Подсчет количества уроков"""
        return instance.lesson_set.count()
