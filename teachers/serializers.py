from rest_framework import serializers

from teachers.models import Category, Teachers, TeachersVideos


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersVideos
        fields = ('video',)


class TeacherSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Teachers
        fields = '__all__'
