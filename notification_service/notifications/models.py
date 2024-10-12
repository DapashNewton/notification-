from django.db import models

class Notification(models.Model):
    message = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()  
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
