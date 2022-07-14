from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Address
from core.serializers import UserSerializer, AddressSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class AddressViewSet(viewsets.ViewSet):
    """
    Addresses endpoint that allows user to manage theirs address book records.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddressSerializer

    def list(self, request):
        addresses = Address.objects.filter(author=request.user).all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def retrieve(self, request, pk=None):
        addr = self.get_object(pk)
        serializer = AddressSerializer(addr)
        return Response(serializer.data)

    def create(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, format=None):
        addr = self.get_object(pk)
        if addr.author != request.user:
            return Response(
                {'message': 'You can update only yours addressbook'},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = AddressSerializer(addr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        addr = self.get_object(pk)
        if addr.author != request.user:
            return Response(
                {'message': 'You can delete only yours address records'},
                status=status.HTTP_403_FORBIDDEN,
            )
        addr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
