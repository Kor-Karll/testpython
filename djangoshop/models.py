from django.db import models

class Customer(models.Model):
    # 고객아이디
    CustID      = models.CharField(max_length=15)
    # 고객이름
    CustName    = models.TextField()
    # 고객패스워드
    CustPwd     = models.TextField()
    # 고객 이메일
    CustEmail   = models.TextField()
    # 고객 타입 A:관리자 B:판매자 C:소비자
    CustType    = models.CharField(max_length=1)
    
    def __str__(self):
        return self.CustID

# Create your models here.
