from rest_framework import response
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class GetAllItems(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response([
            {'id': 0, 'name': 'Item 0'},
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'},
            {'id': 3, 'name': 'Item 3'}
        ])

class GetItem(GenericAPIView):
    def get(self, request, *args, **kwargs):
        id = str(request.GET.get('id'))
        return Response([
            {'id': 0, 'name': 'Item 0'},
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'},
            {'id': 3, 'name': 'Item 3'}
        ][id])


