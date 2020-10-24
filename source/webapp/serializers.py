from rest_framework import serializers
from webapp.models import  Favorites


class FavoriteSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    photo = serializers.PrimaryKeyRelatedField(read_only=True)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)


