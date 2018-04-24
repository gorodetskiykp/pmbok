from django.db import models

class Project(models.Model):
    full_name = models.CharField('Полное название', max_length=500, unique=True, blank=False, null=False)
    short_name = models.CharField('Краткое название', max_length=50, unique=True, blank=False, null=False)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['short_name']
