from dataclasses import field, fields
from rest_framework import serializers
from softwares.models import Software

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model=Software
        fields="__all__"