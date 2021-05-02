from django.db import models

# Create your models here.

# Creating a Agent table
class Skill(models.Model):
    #Map 1 User to 1 Agent
    skill_name = models.CharField(max_length=30)
    skill_percent = models.IntegerField(default=20)

    def __str__(self):
        return self.skill_name
