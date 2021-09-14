#  Created by btrif Trif on 14-09-2021 , 11:35 AM.
from rest_framework import serializers
from .models import Lanaguage

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lanaguage
        fields =  ('id', 'name', 'paradigm')