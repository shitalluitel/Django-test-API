from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Api
from .serializers import ApiSerializer
from .permissions import IsOwner


# from rest_framework.permissions import IsAuthenticated


class CreateListApi(APIView):
    def get(self, request, format=None):
        api = Api.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(api, request)
        serializer = ApiSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.user = request.user
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_data(*args):
    try:
        api = Api.objects.get(pk=args[0])
        return api
    except Api.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateApi(APIView):
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return Api.objects.filter(pk=self.kwargs['pk'])

    def put(self, request, pk, format=None):
        serializer = ApiSerializer(get_data(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class DeleteDetailApi(APIView):
    def get(self, request, pk, format=None):
        serializer = ApiSerializer(get_data(pk))
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        self.get_data(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
