from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

class Tag(models.Model):
    lable = models.CharField(max_length=255)




class TaggedItem(models.Model):
    #using this class we caan find out what tag is applied to what object
    #to identify an app from different model we could import that but that would mean that our current app function is dependent on it
    #To generically identify an object, we need two pieces of information
    #Type of object(product, video, article)
    #ID
    #
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()