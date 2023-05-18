from django.db import models

# Create your models here.



class Domain(models.Model):
    d_name = models.CharField(max_length=200)
    d_desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.d_name
