from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Agenda(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    title = models.CharField(max_length=100)
    description = models.TextField()

    status_choices = [('Pending','Pending') , ('In Progress','In Progress'), ('Completed','Completed')]
    status = models.CharField(max_length = 20, choices=status_choices)

    due_date = models.DateField()

    updated  = models.DateTimeField(auto_now= True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title




    


