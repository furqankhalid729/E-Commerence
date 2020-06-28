#import now as now
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
# Create your models here

class p(models.Model):
    P_id=models.AutoField(primary_key=True)
    P_name=models.CharField(max_length=50)
    P_price=models.IntegerField()
    P_Description=models.CharField(max_length=300)
    image=models.ImageField(null=True, blank=True)
    date=models.DateField(default=datetime.date.today)
    

    def __str__(self):
        return self.P_name


class order(models.Model):
    transaction_id=models.AutoField(primary_key=True)
    customer=models.ForeignKey(User,default=None,blank=True,null=True,on_delete=models.SET_NULL)
    date_order=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    complete=models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return str(self.customer)

    @property
    def add_to_cart(self, id):
        ps = p.objects.get(pk=id)
        try:
            preexisting_order = orderItem.objects.get(product=ps,order=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except p.DoesNotExist:
            new_order = orderItem.objects.create(
                product=ps,
                order=self,
                quantity=1
                )
            new_order.save()

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=0
        for i in orderitems:
            total+=i.pro_total
        return total


    @property
    def get_total_item(self):
        items=self.orderitem_set.all()
        total=0
        for i in items:
            total+=i.quantity
        return total

class shippingAddress(models.Model):
    T_id=models.ForeignKey(order,on_delete=models.CASCADE)
    address=models.CharField(max_length=150,blank=True,null=True)
    City=models.CharField(max_length=150,blank=True,null=True)
    Country=models.CharField(max_length=150,blank=True,null=True)
    Zipcode=models.CharField(max_length=150,blank=True,null=True)


    def __str__(self):
        return self.address

class orderItem(models.Model):
    order=models.ForeignKey(order,blank=True,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(p,blank=True,null=True,on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=0,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)

    @property
    def pro_total(self):
        total= self.quantity*self.product.P_price
        return total

    @property
    def Update_quan(self):
        self.quantity=self.quantity+1
        self.save()

    property
    def remove(self):
        self.delete()

    @property
    def des_quan(self):
        self.quantity=self.quantity-1
        self.save()

        if self.quantity<=0:
            self.delete()

class comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(p,on_delete=models.CASCADE)
    text=models.TextField(null=True,blank=True)