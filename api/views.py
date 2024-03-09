from django.shortcuts import render, get_object_or_404
from goods.models import Good
from goods.serializers import GoodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GoodList(APIView):

    def get(self, request):
        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GoodDetail(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Good.objects.all(), pk=pk)
        serializer = GoodSerializer(obj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        obj = get_object_or_404(Good.objects.all(), pk=pk)
        serializer = GoodSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(Good.objects.all(), pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)