from django.shortcuts import render
from rest_framework.reverse import reverse

from rest_framework.response import Response
from rest_framework import generics

from .models import Note
from django.contrib.auth.models import User
from .serializers import noteSerializer, userSerializer

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

# Create your views here.
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request):
        return Response({
            #'user': reverse(CurrentUserView.name, request=request),
            'note': reverse(NotesListView.name, request=request),
            'filterbydate': reverse(filterbydate.name, request=request),
        })

class NotesListView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = noteSerializer
    name = 'note-list'


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = noteSerializer
    name = 'note-detail'

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    name = 'user-detail'

class filterbydate(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = noteSerializer

    name = 'filterbydate'
    filter_fields = ('update','ref','id')


