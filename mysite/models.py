from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) #最大可儲存字元200
    slug = models.CharField(max_length=200) #最大可儲存字元200
    body = models.TextField() #會超過255字元都這樣表示
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title