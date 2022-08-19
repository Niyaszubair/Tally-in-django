from django.shortcuts import render

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
    return render(request, 'stock/liststock.html')

def liststockgroupviews(request):
    return render(request, 'stock/liststockgroup.html')

def singlestockgroupanalysisview(request):
    return render(request, 'stock/singlestockgroupanalysis.html')

def querystockview(request):
    return render(request, 'stock/querystocks.html')

def purchasevoucheranalysisview(request):
    return render(request, 'stock/purchasevoucheranalysis.html')

def salevoucheranalysisview(request):
    return render(request, 'stock/salevoucheranalysis.html')
    
def itemmovementanalysisview(request):
    return render(request, 'stock/itemmovementanalysis.html')

def stockgroupanalysisview(request):
    return render(request, 'stock/stockgroupanalysis.html')

def stockgroupcreateview(request):
    return render(request, 'stock/stockgroupcreation.html')

def stockitmecreateview(request):
    return render(request, 'stock/stockitemcreation.html')





