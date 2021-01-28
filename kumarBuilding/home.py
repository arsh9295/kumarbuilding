from django.shortcuts import render, redirect
from kumarBuilding.models import itemlist, InventoryList, CustomerList, ItemPurchaged, CustomerPurchage
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime


def index(request):
    return render(request, 'kumarBuilding/home.html')


def billing(request):
    itemi = [None]
    item = [None]
    itemq = [None]
    itemt = [None]
    items = InventoryList.objects.all()
    context = {"items": items}
    if request.method == 'POST':
        # print(request.POST['item6i'])
        # print(request.POST.getlist('item1i'))
        borr = request.POST['due']
        borr = str(abs(int(borr)))
        customermobile = request.POST['customermobile']
        customername = request.POST['customername']
        customeremail = request.POST['customeremail']
        customeraddress = request.POST['customeraddress']
        checkboxvalue = request.POST.get("returncheck", "off")
        if checkboxvalue == "off":
            advance = request.POST['return']
        else:
            advance = 0
        customerpurchagenumber = CustomerPurchage.objects.all()
        customeridone = CustomerList.objects.all().filter(Q(customermobile=customermobile))
        # print(customerid)
        # print(customerid[0].borrow)
        if customeridone:
            totalborrow = int(customeridone[0].borrow) + int(borr)
        else:
            totalborrow = int(borr)
        if customeridone:
            advancetotal = int(customeridone[0].advance) + int(advance)
        else:
            advancetotal = int(advance)
        bortowadvance = advancetotal - abs(totalborrow)
        if bortowadvance < 0:
            totalborrow = str(abs(bortowadvance))
            advancetotal = "0"
        elif bortowadvance > 0:
            advancetotal = str(bortowadvance)
            totalborrow = "0"
        else:
            totalborrow = "0"
            advancetotal = "0"
        totaltran = request.POST['tp']
        receive = request.POST['receive']
        clickscnt = request.POST['clickscnt']
        if customeridone:
            customerid = customeridone.reverse()[0]
            customerid = customerid.customerid
            customerid = int(customerid) + 1
        else:
            customerid = "1"
        if customerpurchagenumber:
            customerpurchagenumber.reverse()[0]
            customerpurchagenumber = customerpurchagenumber[0]
            print(type(customerpurchagenumber))
            purchageid = int(str(customerpurchagenumber)) + 1
        else:
            purchageid = "1"
        if clickscnt:
            clickscnt = clickscnt
        else:
            clickscnt = 7
        for i in range(1, int(clickscnt) + 1):
            # print("Utkarsh")
            print(request.POST['item'+str(i)+'i'])
            if request.POST['item'+str(i)+'i'] and request.POST['item'+str(i)] and request.POST['item'+str(i)+'q'] and request.POST['item'+str(i)+'t']:
                print(request.POST['item' + str(i) + 'i'])
                itemi.append(request.POST['item'+str(i)+'i'])
                item.append(request.POST['item'+str(i)])
                itemq.append(request.POST['item'+str(i)+'q'])
                itemt.append(request.POST['item'+str(i)+'t'])
                itempurched = ItemPurchaged(purchageitem=itemi[i], unitprice=item[i], quantity=itemq[i])
                itempurched.save()
                # customerpurchage = CustomerPurchage(purchageid=purchageid, purchagedate=datetime.today().strftime('%Y-%m-%d'))
                # customerpurchage.save()
                # itempurched.customerpurchage_set.all()
                # customerpurchage = itempurched.customerpurchage_set.create(purchageid=str(purchageid), purchagedate=datetime.today().strftime('%Y-%m-%d'), borrowt=)
                # # customerpurchage.save()
                # customerpurchage.customerlist_set.all()
                # customerlist = customerpurchage.customerlist_set.create(customername=customername, customeremail=customeremail,customermobile=customermobile, customerid=customerid)
                # customerlist = CustomerList(customername=customername, customeremail=customeremail,customermobile=customermobile, customerid=customerid)
                # customerlist.save()
                itemsfatch = InventoryList.objects.all().filter(Q(itemname=itemi[i]))
                print(itemsfatch)
                # itemsfatch = InventoryList.objects.all().get_or_create(Q(itemname=request.POST['item'+str(i)]))
                # print(itemsfatch)
                if itemsfatch:
                    quantityo = itemsfatch[0].quantity
                    quantityt = int(quantityo) - int(itemq[i])
                    itemsfatch.update(quantity=str(quantityt))
                    # memberone = InventoryList(itemname=request.POST['item'+str(i)], quantity=str(quantityt))
                    # memberone.save()
                # else:
                #     memberone = InventoryList(itemname=request.POST['item'+str(i)], quantity=request.POST['quantity'+str(i)])
                #     memberone.save()
        itempurched.customerpurchage_set.all()
        customerpurchage = itempurched.customerpurchage_set.create(purchageid=str(purchageid), purchagedate=datetime.today().strftime('%Y-%m-%d'), borrowt=borr, advancet=advance, totalprice=totaltran, received=receive)
        if customeridone:
            print("ping")
            customeridone.update(borrow=totalborrow, advance=advancetotal)
            # customerpurchage.customerlist_set.all()
            # customerlist = customerpurchage.customerlist_set.update(customername=customername,
            #                                                         customeremail=customeremail,
            #                                                         customeraddress=customeraddress,
            #                                                         customerid=customerid, borrow=totalborrow,
            #                                                         advance=advancetotal)
        else:
            print("pong")
            customerpurchage.customerlist_set.all()
            customerlist = customerpurchage.customerlist_set.create(customername=customername, customeremail=customeremail, customermobile=customermobile, customeraddress=customeraddress, customerid=customerid, borrow=totalborrow, advance=advancetotal)



        # if clickscnt:
        #     for i in range(8, int(clickscnt) + 1):
        #         if request.POST['item' + i + 'i'] is None & request.POST['item' + i] is None & request.POST['item' + i + 'q'] is None & request.POST['item' + i + 't']:
        #             itemi[i] = request.POST['item' + i + 'i']
        #             item[i] = request.POST['item' + i]
        #             itemq[i] = request.POST['item' + i + 'q']
        #             itemt[i] = request.POST['item' + i + 't']

    return render(request, 'kumarBuilding/billing.html', context)


def products(request):
    items = itemlist.objects.all()
    context = {"items": items}
    # print(context)
    # return render(request, 'kumarBuilding/product.html')
    return render(request, 'kumarBuilding/product.html', context)


def customer(request):
    return render(request, 'kumarBuilding/customer.html')


def board(request):
    return render(request, 'kumarBuilding/board.html')


def additem(request):
    if request.method == 'POST':
        totalitemnumber = request.POST['clickscnt']
        # xyz=request.POST['totalprice']
        # print(xyz)
        if totalitemnumber:
            totalitemnumber = int(totalitemnumber)
            for i in range(1, totalitemnumber+1):
                member = itemlist(itemname=request.POST['item'+str(i)], address=request.POST['dealeradd'+str(i)], mobile=request.POST['mobile'+str(i)], quantity=request.POST['quantity'+str(i)], unitprice=request.POST['unitprice'+str(i)], dateitem=request.POST['datereceived'+str(i)], totalprice=request.POST['totalprice'+str(i)])
                member.save()
                itemsfatch = InventoryList.objects.all().filter(Q(itemname=request.POST['item'+str(i)]))
                # print(itemsfatch)
                # itemsfatch = InventoryList.objects.all().get_or_create(Q(itemname=request.POST['item'+str(i)]))
                # print(itemsfatch)
                if itemsfatch:
                    quantityo = itemsfatch[0].quantity
                    quantityt = int(quantityo) + int(request.POST['quantity'+str(i)])
                    itemsfatch.update(quantity=str(quantityt))
                    # memberone = InventoryList(itemname=request.POST['item'+str(i)], quantity=str(quantityt))
                    # memberone.save()
                else:
                    memberone = InventoryList(itemname=request.POST['item'+str(i)], quantity=request.POST['quantity'+str(i)])
                    memberone.save()
        else:
            member = itemlist(itemname=request.POST['item1'], address=request.POST['dealeradd1'],
                              mobile=request.POST['mobile1'],
                              quantity=request.POST['quantity1'], unitprice=request.POST['unitprice1'],
                              dateitem=request.POST['datereceived1'], totalprice=request.POST['totalprice1'])
            member.save()
            itemsfatch = InventoryList.objects.all().filter(Q(itemname=request.POST['item1']))
            # print(itemsfatch)
            if itemsfatch:
                quantityo = itemsfatch[0].quantity
                quantityt = int(quantityo) + int(request.POST['quantity1'])
                itemsfatch.update(quantity=str(quantityt))
                # memberone = InventoryList(itemname=request.POST['item1'], quantity=str(quantityt))
                # memberone.save()
            else:
                memberone = InventoryList(itemname=request.POST['item1'], quantity=request.POST['quantity1'])
                memberone.save()
        return redirect('/')

    # itemname: $item,
    # address: $dealeradd,
    # quantity: $quantity,
    # unitprice: $unitprice,
    # dateitem: $datareceived,
    # totalprice: $total,
    # if request.method == 'POST':
    #     allitems =itemlist()
    #     itemname1 = request.GET['item']
    #     address1 = request.GET['dealeradd']
    #     quantity1 = request.GET['quantity']
    #     unitprice1 = request.GET['unitprice']
    #     dateitem1 = request.GET['datereceived']
    #     totalprice1 = request.GET['totalprice']
    #     allitems.itemname = itemname1
    #     allitems.address = address1
    #     allitems.quantity = quantity1
    #     allitems.unitprice = unitprice1
    #     allitems.dateitem = dateitem1
    #     allitems.totalprice = totalprice1
    #     allitems.save()
    #     return HttpResponse('true')
