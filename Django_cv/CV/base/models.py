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
class carousel(models.Model):
    p_image=models.ImageField()
    p_description=models.TextField()
    p_link=models.CharField(blank=False,max_length=200)

    def __str__(self):
        return self.p_description

class footer(models.Model):
    s_links=models.CharField(max_length=200)
    s_photo=models.ImageField()
    def __str__(self):
        return self.s_links
    
class contact(models.Model):
    name=models.CharField(blank=False,max_length=150)
    email=models.EmailField(blank=False)
    message=models.TextField()
    def __str__(self):
        return self.name