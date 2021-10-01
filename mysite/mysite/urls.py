"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from goldbankapp import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('goldbankapp.urls')),
        path('base/',views.base,name='base'),
        path('features/',views.features,name='features'),
        path('adminPanel/',views.adminPanel,name='adminPanel'),
        path('',views.home,name='home'),
        #path('goldbankapp/', include('goldbankapp.urls')),
        path('logout/', views.user_logout, name='logout'),
        path('about/',views.about, name="about"),
        path('moneytogold/',views.moneytogold, name='moneytogold'),
        path('moneytogold/conv/',views.conv, name='conv'),
        #path('gold_price/',views.gold_price, name='gold_price'),
        path('gold_price/',views.updatePrice, name='updatePrice'),
        path('update_profile/',views.updateProfile, name='updateProfile'),
        path('profile_pic/',views.profile_pic, name='profile_pic'),
        path('show_gold_price/',views.show_gold_price, name='show_gold_price'),
        path('user_profile/',views.user_profile, name='user_profile'),
        path('show_account_info/',views.show_account_info, name='show_account_info'),
        path('show_balance_info/',views.show_balance_info, name='show_balance_info'),
        path('show_loan_info/',views.show_loan_info, name='show_loan_info'),
        path('show_purchase_info/',views.show_purchase_info, name='show_purchase_info'),
        path('show_deposit_history/',views.show_deposit_history, name='show_deposit_history'),
        path('show_withdraw_history/',views.show_withdraw_history, name='show_withdraw_history'),
        #path('acc_no/',views.acc_no,name='acc_no'),
        path('depositamount/',views.depositamount,name='depositamount'),
        path('withdrawamount/',views.withdrawamount,name='withdrawamount'),
        path('bankTotalMoney/',views.bankTotalMoney,name='bankTotalMoney'),
        path('loan/',views.loanamount,name='loanamount'),
        path('return_loan/',views.loan_return,name='loan_return'),
        path('transfer_gold/',views.transfer_gold,name='transfer_gold'),
        path('admin_login/',views.admin_login,name='admin_login'),
        path('buy_product/',views.product,name='product'),
        path('buy_gold/',views.buy_gold,name='buy_gold'),
        path('buy_silver/',views.buy_silver,name='buy_silver'),
        path('buy_bronze/',views.buy_bronze,name='buy_bronze'),
        path('myPanel/',views.myPanel, name='myPanel')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


