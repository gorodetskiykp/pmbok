from django.db import models


class Process(models.Model):
    name = models.CharField('Название', max_length=100, unique=True, blank=False, null=False)
    order = models.PositiveSmallIntegerField('Порядок')
    process_group = models.ForeignKey('ProcessGroup', verbose_name="Группа процессов", on_delete=models.SET_NULL, null=True)
    knowlege_field = models.ForeignKey('KnowlegeField', verbose_name="Область знаний", on_delete=models.SET_NULL, null=True) 
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Процесс"
        verbose_name_plural = "Процессы"
        ordering = ['process_group', 'knowlege_field', 'order']


class ProcessGroup(models.Model):
    name = models.CharField('Название', max_length=100, unique=True, blank=False, null=False)
    order = models.PositiveSmallIntegerField('Порядок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа процессов"
        verbose_name_plural = "Группы процессов"
        ordering = ['order']


class KnowlegeField(models.Model):
    name = models.CharField('Название', max_length=100, unique=True, blank=False, null=False)
    order = models.PositiveSmallIntegerField('Порядок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Область знаний"
        verbose_name_plural = "Области знаний"
        ordering = ['order']
