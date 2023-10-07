from django.db import models

# Create your models here.
class skills(models.Model):
    skill=models.CharField(max_length=100)
    skill_pic=models.ImageField(blank=False)

    def __str__(self):
        return self.skill
class about(models.Model):
    about_sec=models.TextField()
    self_pic=models.ImageField()

    def __str__(self):
        return self.about_sec