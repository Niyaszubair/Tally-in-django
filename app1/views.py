from django.shortcuts import redirect, render
from app1 import models
from app1.models import *
from django.db.models import *

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

# stocks

def liststockviews(request):
    data=CreateStockItem.objects.all()
    context={'data':data}
    return render(request, 'stock/liststock.html',context)

def liststockgroupviews(request):
    data=CreateStockGrp.objects.all()
    context={'data':data}
    return render(request, 'stock/liststockgroup.html',context)


def singlestockgroupanalysisview(request,pk):
    data1=CreateStockGrp.objects.get(id=pk)
    data2=CreateStockItem.objects.get(under=data1)
    data=analysis_view.objects.filter(particular=data2)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    for a in data:
        sum1 += a.iquantity
    for b in data:
        sum2 += b.ieff_rate
    for c in data:
        sum3 += c.ivalue
    for d in data:
        sum4 += d.oquantity
    for e in data:
        sum5 += e.oeff_rate
    for f in data:
        sum6 += f.ovalue
    context={'data':data,'data1':data1,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'sum5':sum5,'sum6':sum6}
    return render(request, 'stock/singlestockgroupanalysis.html',context)

def itemmovementanalysisview(request):
    data1=purchase_model.objects.all()
    data2=sale_model.objects.all()
    context={'data1':data1,'data2':data2}
    return render(request, 'stock/itemmovementanalysis.html',context)
    
def querystockview(request,pk):
    data=CreateStockItem.objects.get(id=pk)
    # ndata=godown_model.objects.all()
    ndata=godown_model.objects.filter(itm=data)
    total_sum = 0
    for item in ndata:
        total_sum += item.itm.quantity
    # sums=godown_model.objects.filter(ndata).sum()
    # purchase=purchase_model.objects.all()
    purchase=purchase_model.objects.filter(itm=data)
    # sale=sale_model.objects.all()
    sale=sale_model.objects.filter(itm=data)
    # cat=category_model.objects.all()
    cat=category_model.objects.filter(itm=data)
    
    context={'data':data,'ndata':ndata,'purchase':purchase,'sale':sale,'cat':cat,'total_sum':total_sum}
    return render(request, 'stock/querystocks.html',context)


def purchasevoucheranalysisview(request,pk):
    data=purchase_model.objects.get(id=pk)
    context={'data':data}
    return render(request, 'stock/purchasevoucheranalysis.html',context)

def salevoucheranalysisview(request,pk):
    data=sale_model.objects.get(id=pk)
    context={'data':data}
    return render(request, 'stock/salevoucheranalysis.html',context)
    


def stockgroupanalysisview(request):
    data=analysis_view.objects.all()
    # var1=analysis_view.objects.get(ivalue)
    # list1=list(var1)
    # sums=sum(list1)
    # for ivalue in data:
    #     list1=sum(ivalue)
    #     print(list1)
    # sums=analysis_view.objects.aggregate(Sum('ivalue'))
    # ModelName.objects.filter(field_name__isnull=True).aggregate(Sum('field_name'))
    sum1 = 0
    sum2 = 0
    for a in data:
        sum1 += a.ivalue
    for b in data:
        sum2 += b.ovalue
    context={'data':data,'sum1':sum1,'sum2':sum2}
    return render(request, 'stock/stockgroupanalysis.html',context)

def stockgroupcreateview(request):
    data=CreateStockGrp.objects.all()
    context={'data':data}
    return render(request, 'stock/stockgroupcreation.html',context)

def stockitmecreateview(request):
    data=CreateStockGrp.objects.all()
    context={'data':data}
    return render(request, 'stock/stockitemcreation.html',context) 


def savestockgroup(request):
    if request.method == 'POST':
        gpname=request.POST['name']
        gpalias=request.POST['alias']
        gpunder=request.POST.get('und')
        gpquantity=request.POST.get('qty')
        data=CreateStockGrp(name=gpname,alias=gpalias,under=gpunder,quantities=gpquantity)
        data.save()
        return redirect('liststockgroupviews')


def savestockitem(request):
    if request.method == 'POST':
        iname=request.POST['name']
        ialias=request.POST['alias']
        iunder=request.POST['under']
        und=CreateStockGrp.objects.get(id=iunder)
        iunitr=request.POST.get('unit')
        igst=request.POST.get('gst')
        isupply=request.POST.get('supply')
        iduty=request.POST.get('rduty')
        iquantity=request.POST.get('qnt')
        irate=request.POST.get('rate')
        iper=request.POST.get('per')
        ivalue=request.POST.get('value')
        data=CreateStockItem(name=iname,alias=ialias,under=und,gst=igst,supply=isupply,rduty=iduty,quantity=iquantity,rate=irate,per=iper,value=ivalue)
        data.save()
        
        return redirect('liststockviews')








