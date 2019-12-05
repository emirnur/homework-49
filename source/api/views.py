from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import ProjectSerializer, IssueSerializer
from webapp.models import Project, TrackerIssue


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    queryset = TrackerIssue.objects.all()