from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from mainapp.models import Category, TypeWork


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_category', 'category_view']


class TypeWorkSerializer(ModelSerializer):
    class Meta:
        model = TypeWork
        fields = ['id', 'name_work', 'category', 'hours', 'cost']
