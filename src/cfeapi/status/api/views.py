from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication

from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer

class StatusApiDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user = self.request.user)
    #
    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None


class StatusAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StatusSerializer
    passed_id = None

    # Override get_queryset for searching eg. /?p=content
    def get_queryset(self):
        request = self.request
        print(request.user)
        qs = Status.objects.all()
        query = self.request.GET.get('p')
        if query is not None:
            qs = qs.filter(content__icontains=query)

        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('id', None) or self.passed_id
    #     queryset = self.get_queryset()
    #     obj = None
    #     if passed_id is not None:
    #         obj = get_object_or_404(queryset, id=passed_id)
    #         self.check_object_permissions(request, obj)
    #     return obj
    #
    # def get(self, request, *args, **kwargs):
    #     url_passed_id              = request.GET.get('id', None)
    #     # json_data               = json.loads(request.body)
    #     # new_passed_id       = json.data.get('id', None)
    #     # print(request.body)
    #
    #     passed_id = url_passed_id or None
    #     # print(request.data)
    #     if passed_id is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)


    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

# class StatusAPIView(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.ListAPIView):
#
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#
#     # Override get_queryset for searching eg. /?p=content
#     def get_queryset(self):
#         request = self.request
#         qs = Status.objects.all()
#         query = self.request.GET.get('p')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#
#         return qs
#
#     def get_object(self):
#         request = self.request
#         passed_id = request.GET.get('id', None) or self.passed_id
#         queryset = self.get_queryset()
#         obj = None
#         if passed_id is not None:
#             obj = get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)
#         return obj
#
#     def get(self, request, *args, **kwargs):
#         url_passed_id              = request.GET.get('id', None)
#         # json_data               = json.loads(request.body)
#         # new_passed_id       = json.data.get('id', None)
#         # print(request.body)
#
#         passed_id = url_passed_id or None
#         # print(request.data)
#         if passed_id is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)
#
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#
#         # body_ = request.body
#         # if is_json(body_):
#         #     json_data = json.loads(request.body)
#
#         new_passed_id = json_data.get('id', None)
#
#         requested_id = request.data.get('id')
#         passed_id = url_passed_id or new_passed_id or requested_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)

# class StatusAPIView(generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#
#     # Override get_queryset for searching eg. /?p=content
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#
#         return qs

# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#
#     # Override get_queryset for searching eg. /?p=content
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('p')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#
#         return qs
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class StatusDetailAPIView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     # lookup_field = 'id'
#
#     def get_object(self, *args, **kwargs):
#         kwargs = self.kwargs
#         kw_id = kwargs.get('id')
#         return Status.objects.get(id=kw_id)

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def get_object(self, *args, **kwargs):
#         kwargs = self.kwargs
#         kw_id = kwargs.get('id')
#         return Status.objects.get(id=kw_id)
#
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def get_object(self, *args, **kwargs):
#         kwargs = self.kwargs
#         kw_id = kwargs.get('id')
#         return Status.objects.get(id=kw_id)
