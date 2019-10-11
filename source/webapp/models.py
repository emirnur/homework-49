from django.db import models


class TrackerIssue(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус',
                                 related_name='issues')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Тип',
                               related_name='issues')
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True, blank=False, verbose_name='Проект',
                             related_name='issues')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.summary


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Статус')

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Тип')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.title
