from django.db import models

# Create your models here.
# Creating a Skill table
class Testimonial(models.Model):
    testimonial_name = models.CharField(max_length=30)
    testimonial_title = models.CharField(max_length=100)
    testimonial_content = models.TextField()

    testimonial_collapsed = models.BooleanField(default=True)

    testimonial_number = models.CharField(max_length=30)

    def __str__(self):
        return self.testimonial_name