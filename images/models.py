from django.db import models


# Create your models here.
class Images(models.Model):
    Url = models.TextField()
    CreateDate = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'Images'
    def __str__(self):
        return self.Url
    
class Stock6Sign202212(models.Model):
    #Url = models.TextField()
    
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    
    CreateDate = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'Stock6Sign202212'
    def __str__(self):
        return self.cStockID
    
class Stock6Sign202301(models.Model):
    #Url = models.TextField()
    
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    
    CreateDate = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'Stock6Sign202301'
    def __str__(self):
        return self.cStockID
