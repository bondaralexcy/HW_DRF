# from rest_framework.fields import SerializerMethodField
from rest_framework import serializers
from materials.validators import validate_allow_site
from materials.models import Course, Lesson, CourseSubscription


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.CharField(validators=[validate_allow_site], read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"


    def create(self, validated_data):
        user = self.context['request'].user
        lesson = Lesson(**validated_data)
        lesson.owner = user
        lesson.save()
        return lesson


class CourseSerializer(serializers.ModelSerializer):
    # Добавил поле lessons_count - количество уроков
    lessons_count = serializers.SerializerMethodField()
    # Список уроков в курсе
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)
    # Наличие подписки
    course_subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, instance):
        """Подсчет количества уроков"""
        return instance.lesson_set.count()


    def get_course_subscribe(self, instance):
        user = self.context['request'].user
        if CourseSubscription.objects.filter(user=user, course=instance).exists():
            return True
        return False


    def create(self, validated_data):
        user = self.context['request'].user
        course = Course(**validated_data)
        course.owner = user
        course.save()
        return course


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'
