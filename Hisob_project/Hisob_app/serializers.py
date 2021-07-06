from rest_framework import serializers
from .models import Shart, Bajarish


class ShartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shart
        fields = "__all__"

class BajarishSerializer(serializers.Serializer):
    shart = ShartSerializer()
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()
    result = serializers.IntegerField() # natija

def create(self, validated_data):
    if validated_data['shart'] == 1:
        result_one = int(validated_data['number1'] + validated_data['number2'])
        model = Bajarish(
            shart_id=validated_data['shart'],
            number1=validated_data['number1'],
            number2=validated_data['number2'],
            result=result_one
        )
        model.save()
    elif validated_data['shart'] == 2:
        result_two = int(validated_data['number2'] - validated_data['number1'])
        model = Bajarish(
            shart_id=validated_data['shart'],
            number1=validated_data['number1'],
            number2=validated_data['number2'],
            result=result_two
        )
        model.save()
    elif validated_data['shart'] == 3:
        result_there = int(validated_data['number1'] - validated_data['number2'])
        model = Bajarish(
            shart_id=validated_data['shart'],
            number1=validated_data['number1'],
            number2=validated_data['number2'],
            result=result_there
        )
        model.save()
    elif validated_data['shart'] == 4:
        result_foo = int(validated_data['number1'] * validated_data['number2'])
        model = Bajarish(
            shart_id=validated_data['shart'],
            number1=validated_data['number1'],
            number2=validated_data['number2'],
            result=result_foo
        )
        model.save()

    elif validated_data['shart'] == 5:
        result_five = int(validated_data['number1'] / validated_data['number2'])
        model = Bajarish(
            shart_id=validated_data['shart'],
            number1=validated_data['number1'],
            number2=validated_data['number2'],
            result=result_five
        )
        model.save()
    elif validated_data['shart'] == 6:

        result_six = int(validated_data['number2'] / validated_data['number1'])
        model = Bajarish(
            shart_id=validated_data['shart'],
            number1=validated_data['number1'],
            number2=validated_data['number2'],
            result=result_six
        )
        model.save()




