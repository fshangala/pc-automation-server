from dataclasses import field, fields
from rest_framework import serializers
from softwares.models import Software, BetSite

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model=Software
        fields="__all__"

class BetSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=BetSite
        fields="__all__"