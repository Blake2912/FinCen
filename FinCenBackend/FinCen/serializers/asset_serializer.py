from rest_framework import  serializers
from varname import nameof
from ..models import *

class AssetInfoResponseSerializer(serializers.Serializer):
    asset_id = serializers.IntegerField()
    symbol = serializers.CharField()
    asset_type = serializers.CharField()
    quantity = serializers.IntegerField()
    purchase_price = serializers.FloatField()
    purchase_datetime = serializers.DateTimeField()

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop(nameof(Asset.user), None)
        rep.pop(nameof(Asset.created_at), None)
        return rep


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class SaveAssetPayloadSerializer(serializers.Serializer):
    api_key = serializers.CharField()
    symbol = serializers.CharField()
    asset_type = serializers.CharField()
    quantity = serializers.IntegerField()
    purchase_price = serializers.FloatField()
    purchase_datetime = serializers.DateTimeField()