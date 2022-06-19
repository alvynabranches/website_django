from django.db import models
from django.utils import timezone
# Create your models here.
class DemoModel(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=256)
    phone_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to='img/%Y/%m/%d/', max_length=1024, default=True)
    
    def __str__(self) -> str:
        return f'{self.id}'