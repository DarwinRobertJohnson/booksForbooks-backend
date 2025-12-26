
from rest_framework import serializers
from .models import BookEntry


class BookEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookEntry
        fields = "__all__"