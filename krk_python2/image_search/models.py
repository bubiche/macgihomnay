from django.db import models

# Create your models here.
class RequestImage(models.Model):
    content = models.ImageField(upload_to='images/%Y/%m/%d')
    request_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content.name
