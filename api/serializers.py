from rest_framework import serializers
from .models import Food, Today


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'cal']


class TodaysCalories(serializers.ModelSerializer):
    class Meta:
        model = Today
        fields = ['id', 'name', 'cal']
