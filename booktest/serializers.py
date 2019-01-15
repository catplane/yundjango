from rest_framework import serializers

from booktest.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'

