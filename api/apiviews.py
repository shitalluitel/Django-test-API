# # from django.shortcuts import render
#
# # # Create your views here.
#
#
#
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Api
from .serializers import ApiSerializer


@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all Apis, or create a new Api.
    """
    if request.method == 'GET':
        Apis = Api.objects.all()

        '''
        pagination for api view
        '''

        paginator = PageNumberPagination()
        paginator.page_size = 1
        result_page = paginator.paginate_queryset(Apis, request)
        serializer = ApiSerializer(result_page, many=True)
        # return Response(serializer.data)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    """
    Get, udpate, or delete a specific Api
    """
    try:
        Apis = Api.objects.get(pk=pk)
    except Api.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializer(Apis)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApiSerializer(Apis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Apis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
