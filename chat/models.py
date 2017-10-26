from django.db import models
# Create your models here.
class Chat(models.Model):
        name = models.CharField(max_length=120,unique=True)
        type = models.CharField(max_length=120)
        private = models.BooleanField(default=False)
        def __str__(self):
                return 'Chat name: ' + self.name

class Message(models.Model):
        from authentication.models import User
        chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
        from_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='from_user')
        to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='to_user',null=True,blank=True)
        message = models.TextField()
        private = models.BooleanField(default=False)
        sender_time = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
        server_time = models.DateField(auto_now=True, auto_now_add=False,)
        receiver_time = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
        def __str__(self):
                return 'mChat: ' + self.chat.name
