from django.db import models

# Create your models here.

class CreateStockGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.CharField(max_length=100)
    quantities=models.CharField(max_length=100)

class CreateStockItem(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.ForeignKey(CreateStockGrp,on_delete=models.CASCADE)
    unit=models.CharField(max_length=100)
    gst=models.CharField(max_length=100)
    supply=models.CharField(max_length=100)
    rduty=models.CharField(max_length=100)
    quantity=models.IntegerField()
    rate=models.CharField(max_length=100)
    per=models.CharField(max_length=100)
    value=models.CharField(max_length=100)

class analysis_view(models.Model):
    particular=models.ForeignKey(CreateStockItem,on_delete=models.CASCADE)
    # stgroup=models.ForeignKey(CreateStockGrp,on_delete=models.CASCADE)
    iquantity=models.IntegerField(null=True)
    ieff_rate=models.IntegerField(null=True)
    ivalue=models.IntegerField(null=True)
    oquantity=models.IntegerField(null=True)
    oeff_rate=models.IntegerField(null=True)
    ovalue=models.IntegerField(null=True)

class group_ananysis_view(models.Model):
    particular=models.ForeignKey(CreateStockGrp,on_delete=models.CASCADE)
    iquantity=models.IntegerField(null=True)
    ieff_rate=models.IntegerField(null=True)
    ivalue=models.IntegerField(null=True)
    oquantity=models.IntegerField(null=True)
    oeff_rate=models.IntegerField(null=True)
    ovalue=models.IntegerField(null=True)

class godown_model(models.Model):
    name=models.CharField(max_length=255)
    itm=models.ForeignKey(CreateStockItem,on_delete=models.CASCADE)

class purchase_model(models.Model):
    itm=models.ForeignKey(CreateStockItem,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)
    qnt=models.IntegerField()
    brate=models.IntegerField()
    bvalue=models.IntegerField()
    addcost=models.IntegerField()
    totalvalue=models.IntegerField()

class sale_model(models.Model):
    itm=models.ForeignKey(CreateStockItem,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)
    qnt=models.IntegerField()
    brate=models.IntegerField()
    bvalue=models.IntegerField()
    addcost=models.IntegerField()
    totalvalue=models.IntegerField()

class category_model(models.Model):
    itm=models.ForeignKey(CreateStockItem,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    qnt=models.IntegerField()
    cost=models.IntegerField()
    saleprice=models.IntegerField()


# class group_ananysis_view(models.Model):
#     particular=models.ForeignKey(CreateStockItem,on_delete=models.CASCADE)
#     iquantity=models.IntegerField(null=True)
#     ieff_rate=models.IntegerField(null=True)
#     ivalue=models.IntegerField(null=True)
#     oquantity=models.IntegerField(null=True)
#     oeff_rate=models.IntegerField(null=True)
#     ovalue=models.IntegerField(null=True)

    