from django.db import models
from django.core import validators


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    # email = models.EmailField(initial = 'Enter your email', required=True, validators=[validators.EmailValidator(message="Invalid Email")])
    desc = models.CharField(max_length=500)
    date = models.DateField()
    
    def __str__(self):
        return self.name