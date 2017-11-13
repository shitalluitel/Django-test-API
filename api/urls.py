from django.conf.urls import url
# from . import apiviews
from .views import CreateListApi, DeleteDetailApi, UpdateApi
urlpatterns = [
    # url(
    #     regex=r'^test/$',
    #     view=views.ApiListCreateAPIView.as_view(),
    #     name='flavor_rest_api'
    # ),
    # url(
    #     regex=r'^test/(?P<pk>\d+)/$',
    #     view=views.ApiRetrieveUpdateDestroyApiView.as_view(),
    #     name='flavor_rest_api'
    # ),
    # url(regex=r'^test/$', view=apiviews.task_list, name='task_list'),
    # url(regex=r'^test/(?P<pk>\d+)/$', view=apiviews.task_detail, name='task_detail'),

    url(regex=r'^test/$', view=CreateListApi.as_view(), name='task_list'),
    url(regex=r'^(?P<pk>\d+)/test/$', view=UpdateApi.as_view(), name='task_detail'),
    url(regex=r'^test/(?P<pk>\d+)/$', view=DeleteDetailApi.as_view(), name='task_detail'),
]
