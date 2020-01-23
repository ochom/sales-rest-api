from django.http import Http404
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AgentModelSerializer, ClientModelSerializer, OrderModelSerializer, ProductModelSerializer
from .models import AgentModel, ClientModel, OrderModel, ProductModel


def index(request):
    return render(request, "home.html", )


class Agents(generics.ListCreateAPIView):
    queryset = AgentModel.objects.all()
    serializer_class = AgentModelSerializer


class AgentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentModel.objects.all()
    serializer_class = AgentModelSerializer


class Clients(generics.ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientModelSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientModelSerializer


class Orders(APIView):
    def get(self, request, format=None):
        queryset = OrderModel.objects.all()
        agent_id = request.query_params.get('agent', None)
        client_id = request.query_params.get('client', None)
        if agent_id is not None:
            queryset = queryset.filter(agent_id=agent_id)
        elif client_id is not None:
            queryset = queryset.filter(client_id=client_id)
        serializer = OrderModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer


class Products(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer

# class Productss(APIView):
#     def get(self, request, format=None):
#         queryset = ProductModel.objects.all()
#         serializer = ProductModelSerializer(queryset, many=True, context={"request": request})
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ProductModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductssDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return ProductModel.objects.get(pk=pk)
#         except ProductModel.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         queryset = self.get_object(pk)
#         serializer = ProductModelSerializer(queryset)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         queryset = self.get_object(pk)
#         serializer = ProductModelSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         queryset = self.get_object(pk)
#         queryset.delete()
#         return Response("Deleted", status=status.HTTP_204_NO_CONTENT)
