from leadApp.models import Lead
from rest_framework import serializers


class LeadSerializer(serializers.ModelSerializer):
    # source=serializers.ChoiceField(choices=Lead.SOURCE_CHOICE)
    class Meta:
        model=Lead
        fields="__all__"
        read_only_fields=["id","added_date"]