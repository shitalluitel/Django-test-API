# # from django.shortcuts import render
#
# # # Create your views here.
#
#
#
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Api
from .serializers import ApiSerializer


@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all Apis, or create a new Api.
    """
    if request.method == 'GET':
        Apis = Api.objects.all()
        serializer = ApiSerializer(Apis, many=True)
        return Response(serializer.data)

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


# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAuthenticated
# from .models import Api
# from .serializers import ApiSerializer
#
#
# class ApiListCreateAPIView(ListCreateAPIView):
#     queryset = Api.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ApiSerializer
#
#
# class ApiRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Api.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ApiSerializer
