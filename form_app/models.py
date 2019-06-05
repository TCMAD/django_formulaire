from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.
class Formulaire(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.DecimalField(max_digits=15,decimal_places=0)
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=50,choices=(
        ('male','Male'),
        ('female','Female')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('acceuil')

    class Meta:
        ordering = ['-id']