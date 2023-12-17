from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import *

def home(request):
    return HttpResponse('home pageyy!')

class ProjectViewset(viewsets.ViewSet):
    permission_classes=[permissions.AllowAny]
    queryset= Project.objects.all()

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    # def partial_update(self, request, pk=None):
    #    pass

    def destroy(self, request, pk=None):
        pass