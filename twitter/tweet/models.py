from django.db import models

# Create your models here.
class Tweet(models.Model):
  # db_table = 'twitter_django'
  parent_tweet_id = models.IntegerField(default=None,null=True)
  name = models.CharField(max_length=60)
  text = models.CharField(max_length=280)
  image_path = models.CharField(max_length=280,null=True)
  created_at = models.DateTimeField('created_at')
  
  
  def __str__(self):
    return self.name
  
  
 