from rest_framework import serializers
from .models import AgentModel, AgentSkillModel, ClientModel, OrderModel, ProductModel


class AgentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentModel
        fields = ['id', 'username', 'name', 'address', 'email', 'rating',]


# class AgentSkillModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AgentSkillModel
#         fields = ['id', 'agent_id', 'skill',]


class ClientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = ['id', 'username', 'name', 'address', 'email', 'location',]

    # def create(self, validated_data):
    #     client = ClientModel.objects.create(**validated_data)
    #     return client


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['id', 'client_id', 'agent_id', 'product_id', 'quantity', 'total_cost', 'created_at', 'status']


class ProductModelSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        fields = ['id', 'product_name', 'description', 'price', 'photo_url', 'units']

    # this method returns the absolute server url of the image
    def get_photo_url(self, product):
        request = self.context.get('request')
        photo_url = product.image.url
        if product.image and hasattr(product.image, 'url'):
            return request.build_absolute_uri(photo_url)
        else:
            return "/static/images/user.jpg"