from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import *


# Create your views here.
class CategoryView(APIView):
    #List all
    def get(self, request):
        data = CategoryModel.objects.all()
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Create
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Update
    def put(self, request):
        id = request.POST.get('id')
        category = request.POST.get('category')
        try:
            data = CategoryModel.objects.get(id=id)
            if data:
                data.category = category
                data.save()
                resp={
                    'success': 'true',
                    'message': '''Category has been successfully changed.'''
                }

                return Response(resp, status=status.HTTP_201_CREATED)
        except:
                resp = {
                    'success': 'false',
                    'message': 'Something went wrong please try again.'
                }
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

    #Delete
    def delete(self, request):
        id = request.POST.get('id')
        try:
            data = CategoryModel.objects.get(id=id).delete()
            resp={
                    'success': 'true',
                    'message': '''Category has been successfully deleted.'''
                }

            return Response(resp, status=status.HTTP_200_OK)
        except:
                resp = {
                    'success': 'false',
                    'message': 'Something went wrong please try again.'
                }
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)


    

class ProductView(APIView):
    #List all
    def get(self, request):
        data = ProductModel.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Create
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #update
    def put(self, request):
        id = request.POST.get('id')
        product_name = request.POST.get('product_name')
        product_model_name = request.POST.get('product_model_name')
        price = request.POST.get('price')
        product_category = request.POST.get('product_category')
        data = ProductModel.objects.get(id=id)
        if data:
            data.product_name = product_name
            data.product_model_name = product_model_name
            data.price = price
            data.product_category = product_category
            data.save()
            resp={
                'success': 'true',
                'message': '''Product has been successfully changed.'''
            }

            return Response(resp, status=status.HTTP_201_CREATED)

        resp = {
            'success': 'false',
            'message': 'Something went wrong please try again.'
        }

        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

    #Delete
    def delete(self, request):
        id = request.POST.get('id')
        data = ProductModel.objects.get(id=id).delete()
        try:
            data = ProductModel.objects.get(id=id).delete()
            resp={
                    'success': 'true',
                    'message': '''Product has been successfully deleted.'''
                }

            return Response(resp, status=status.HTTP_200_OK)
        except:
                resp = {
                    'success': 'false',
                    'message': 'Something went wrong please try again.'
                }
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)