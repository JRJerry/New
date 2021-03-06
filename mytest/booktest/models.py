from django.db import models

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_data=models.DateTimeField()
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    #外建
    hbook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.hname