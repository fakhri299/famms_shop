from rest_framework import serializers
from paltar.models import Product,Category,Description,User

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Description
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class ClientSerializer(serializers.ModelSerializer):
      class Meta:
        model=User
        fields='__all__'

class PaltarSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField(read_only=True,many=True)
    description=serializers.StringRelatedField(read_only=True)
    client=serializers.StringRelatedField(many=True,read_only=True)
   

    class Meta:
        model=Product
        fields='__all__'

