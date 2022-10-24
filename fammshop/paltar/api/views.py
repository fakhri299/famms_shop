from paltar.api.serializers import DescriptionSerializer
from paltar.models import Description
from paltar.models import Product,Category
from paltar.api.serializers import PaltarSerializer,CategorySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.generics import get_object_or_404









      

class CategoryListCreateApiView(CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class DescriptionCreateApiView(ListCreateAPIView):
    queryset=Description.objects.all()
    serializer_class=DescriptionSerializer


class DescriptionDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset=Description.objects.all()
    serializer_class=DescriptionSerializer

   

class PaltarCreateApiView(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=PaltarSerializer


    def perform_create(self, serializer):
        description_pk=self.kwargs.get('description_pk')
        description=get_object_or_404(Description,pk=description_pk)
        client=self.request.user
        serializer=PaltarSerializer(description=description,client=client)
        serializer.save()

   
       
class PaltarDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=PaltarSerializer

