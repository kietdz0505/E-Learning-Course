from courses.models import Category, Course, Lesson,Tag
from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        d = super().to_representation(instance)
        d['image'] = instance.image.url
        return d


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = ['id','subject','description','created_date','image','category_id']


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = ['id','subject','created_date','image']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']


class LessonDetailsSerializer(LessonSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content','tags']
