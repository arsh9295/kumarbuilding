from django.db import models


class itemlist(models.Model):
    itemname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    quantity = models.EmailField(max_length=100)
    unitprice = models.CharField(max_length=100)
    dateitem = models.CharField(max_length=100)
    totalprice = models.CharField(max_length=100)

    def __str__(self):
        return self.itemname


class InventoryList(models.Model):
    itemname = models.CharField(max_length=100)
    quantity = models.EmailField(max_length=100)
    todayprice = models.CharField(max_length=100)

    def __str__(self):
        return self.itemname


class CustomerList(models.Model):
    customername = models.CharField(max_length=100)
    customeremail = models.CharField(max_length=100)
    customermobile = models.CharField(max_length=100)
    customeraddress = models.CharField(max_length=100)
    customerid = models.CharField(max_length=100)
    borrow = models.CharField(max_length=100)
    advance = models.CharField(max_length=100)
    # customerpurchage = models.ForeignKey(CustomerPurchage, on_delete=models.CASCADE)

    def __str__(self):
        return self.customername


class CustomerPurchage(models.Model):
    purchageid = models.CharField(max_length=100)
    purchagedate = models.CharField(max_length=100)
    borrowt = models.CharField(max_length=100)
    advancet = models.CharField(max_length=100)
    totalprice = models.CharField(max_length=100)
    received = models.CharField(max_length=100)
    customerlist = models.ForeignKey(CustomerList, on_delete=models.CASCADE)

    def __str__(self):
        return self.purchageid


class ItemPurchaged(models.Model):
    purchageitem = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    unitprice = models.CharField(max_length=100)
    customerpurchage = models.ForeignKey(CustomerPurchage, on_delete=models.CASCADE)
    # customerlist = models.ForeignKey(CustomerList, on_delete=models.CASCADE)

    def __str__(self):
        return self.purchageitem

    # class Meta:
    #     db_table = "item_details"
