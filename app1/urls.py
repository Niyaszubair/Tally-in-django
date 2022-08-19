from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('liststockviews',views.liststockviews,name='liststockviews'),
    path('liststockgroupviews',views.liststockgroupviews,name='liststockgroupviews'),
    path('singlestockgroupanalysisview',views.singlestockgroupanalysisview,name='singlestockgroupanalysisview'),
    path('querystockview',views.querystockview,name='querystockview'),
    path('salevoucheranalysisview',views.salevoucheranalysisview,name='salevoucheranalysisview'),
    path('purchasevoucheranalysisview',views.purchasevoucheranalysisview,name='purchasevoucheranalysisview'),
    path('itemmovementanalysisview',views.itemmovementanalysisview,name='itemmovementanalysisview'),
    path('stockgroupanalysisview',views.stockgroupanalysisview,name='stockgroupanalysisview'),
    path('stockgroupcreateview',views.stockgroupcreateview,name='stockgroupcreateview'),
    path('stockitmecreateview',views.stockitmecreateview,name='stockitmecreateview'),
    
]