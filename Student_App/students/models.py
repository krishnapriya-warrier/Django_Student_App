from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    phone_number=models.PositiveIntegerField()
    course=models.CharField(max_length=100)
    profile_picture=models.ImageField(upload_to="profile_images")

    def __str__(self):
        return self.name
