from typing import Text
from django.db import models
from django.db.models.aggregates import Max


# Create your models here.
class Board(models.Model):
   
    #author = models.CharField(max_length=10, null=False)
    #title = models.CharField(max_length=100, null=False)
    #content = models.TextField(null=False)
    #created_date = models.DateTimeField(auto_now_add=True)
    #modified_date = models.DateTimeField(auto_now=True)
    no = models.AutoField(null=False, primary_key=True)
    name = models.CharField(max_length=10, null=True)
    phone = models.IntegerField(null=True) # 
    vdate = models.DateField(null=True) # 방문일자
    gdate = models.DateField(null=True) # 지급일자
    ap = models.IntegerField(null=True) #지급수량
    walletype = models.CharField(max_length=3,null=True)
    awAd = models.CharField(max_length=50,null=True) #a주소
    bwAd = models.CharField(max_length=50,null=True) #b주소
    stakingW = models.CharField(max_length=5,null=True) #스테이킹 여부
    stakingSD = models.DateField(null=True) #스테이킹 시작날짜
    stakingDate = models.DateField(null=True) #스테이킹 기간
    stakingV = models.CharField(max_length=5,null=True) #스테이킹 지급여부
    content = models.TextField(null=True) #비고

    def __str__(self):
        return str(self.no, self.name, self.phone, self.vdate, self.gdate, self.ap, self.walletype, self.awAd, self.bwAd, self.stakingW, self.stakingDate, self.stakingSD, self.stakingV, self.content)



