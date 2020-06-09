from rest_framework import serializers

from sauce.models import Sauce


class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sauce
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'name': {'validators': []}
        }
