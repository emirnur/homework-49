from rest_framework import serializers

from webapp.models import Project, TrackerIssue


class IssueSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TrackerIssue
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'created_by',
                  'assigned_to', 'created_at')


class ProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    issues_project = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'issues_project')


