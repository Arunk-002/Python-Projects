from django.db import models

# Create your models here.
class skills(models.Model):
    skill=models.CharField(max_length=100)
    skill_pic=models.ImageField(blank=False)

    def __str__(self):
        return self.skill
