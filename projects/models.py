from django.db import models

# Create your models here.

# Creating a Skill table
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_link = models.CharField(max_length=100)
    project_order = models.IntegerField(default = 1)

    def __str__(self):
        return self.project_name

# Creating a WebPage table
class Detail(models.Model):
    detail_description = models.CharField(max_length=100)
    detail_project = models.ForeignKey(Project,default="detail",verbose_name="Project",on_delete = models.CASCADE)
    detail_number = models.IntegerField(default = 1)

    def __str__(self):
        return self.detail_description