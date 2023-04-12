from rest_framework import serializers
from .models import dog, Food


# serializers.ModelSerializer just tells django to convert sql to JSON
class dogSerializer(serializers.ModelSerializer):
    class Meta:
        model = dog  # tell django which model to use
        # tell django which fields to include
        fields = ('id', 'name', 'birthday', 'age', 'breed', 'weight')


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'dog', 'time_fed', 'food_total')
