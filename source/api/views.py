from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectSerializer, IssueSerializer
from webapp.models import Project, TrackerIssue


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        else:
            return super().get_permissions()


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = (DjangoModelPermissions,)
    serializer_class = IssueSerializer
    queryset = TrackerIssue.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        else:
            return super().get_permissions()