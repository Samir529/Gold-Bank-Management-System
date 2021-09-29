import copy
import random

from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserProfileInfoForm, updatePriceForm, profilePicForm
from .models import priceOfGold, deposit, UserProfileInfo, bankMoney, loan, products, deposit_history, withdraw_history
from django.shortcuts import render
import datetime


def home(req):
    update = priceOfGold.objects.last()
    return render(req, 'home.html', {'update': update})


def base(req):
    return render(req, 'base.html')


def product(req):
    update = priceOfGold.objects.last()
    temp = 5 * float(update.gold_price)
    temp2 = float(5 * 87)
    temp3 = float(5 * 67)
    return render(req, 'buy_product.html',{'temp': temp, 'temp2': temp2, 'temp3': temp3})


def features(request):
    return render(request, 'features.html')


def adminPanel(request):
    return render(request, 'adminPanel.html')


def admin_login(request):
    isadmin = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_superuser:
                return HttpResponseRedirect(reverse('adminPanel'))

            else:
                isadmin = 'b'
                return render(request, 'admin_login.html',{'isadmin': isadmin})
        else:
            isadmin = 'c'
            return render(request, 'admin_login.html', {'isadmin': isadmin})
    return render(request, 'admin_login.html', {'isadmin': isadmin})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):
    isuser = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('features'))

            else:
                return HttpResponse("Account not actived.")
        else:
            isuser = 'b'
            return render(request, 'user_login.html',{'isuser': isuser})

    return render(request, 'user_login.html', {'isuser': isuser})



def about(request):
    return render(request, 'about.html')



def moneytogold(request):
    return render(request, 'moneytogold.html')



def conv(request):
    update = priceOfGold.objects.last()
    val1 = int(request.GET['num1'])
    res = (1 / update.gold_price) * val1
    return render(request, 'convert.html', {'result': res, 'amount': val1, 'update': update})



# def gold_price(request):
#     return render(request, 'gold_price.html')

def updatePrice(request):
    if request.method == 'POST':
        updatePrice_form = updatePriceForm(data=request.POST)

        if updatePrice_form.is_valid():
            profile = updatePrice_form.save(commit=False)
            profile.save()
            messages.info(request, 'Price Updated Successfully :)')

        else:
            print(updatePrice_form.errors)
    else:
        updatePrice_form = updatePriceForm()

    return render(request, 'gold_price.html',
                  {'updatePrice_form': updatePrice_form})


def updateProfile(request):
    registered = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobileNo = request.POST.get('mobileNo')
        location = request.POST.get('location')
        dateofbirth = request.POST.get('dateofbirth')
        mydata = UserProfileInfo()
        mydata.first_name = first_name
        mydata.last_name = last_name
        mydata.email = email
        mydata.mobileNo = mobileNo
        mydata.location = location
        mydata.dateofbirth = dateofbirth

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    t = UserProfileInfo.objects.get(user=request.user)
                    t2 = User.objects.get(username=username)
                    # t.first_name = first_name
                    # t.last_name = last_name
                    # t.email = email
                    t.mobileNo = mobileNo
                    t.location = location
                    t.dateofbirth = dateofbirth
                    t.save()
                    t2.first_name = first_name
                    t2.last_name = last_name
                    t2.email = email
                    t2.save()
                except UserProfileInfo.DoesNotExist:
                    z ='z'
                registered = 'b'
        else:
            registered = 'c'

    return render(request, 'update_profile.html', {'registered': registered})


def profile_pic(request):
    if request.method == 'POST':
        form = profilePicForm(request.POST, request.FILES)
        if form.is_valid():
            t = UserProfileInfo.objects.get(user=request.user)
            t.profile_pic = form.cleaned_data['profile_pic']
            t.save()
            #img_obj = form.instance
            return render(request, 'profile_pic.html', {'form': form, 't': t})
    else:
        form = profilePicForm()
    return render(request, 'profile_pic.html', {'form': form})



def show_gold_price(request):
    shgd = priceOfGold.objects.all()
    return render(request, 'show_gold_price.html', {'shgd': shgd})


def user_profile(request):
    return render(request, 'user_profile.html')


def show_account_info(request):
    if request.user.is_authenticated:
        try:
             acinfo = UserProfileInfo.objects.filter(user=request.user)
             t = UserProfileInfo.objects.get(user=request.user)

             date_format = '%Y-%m-%d'
             a = datetime.datetime.strptime(str(datetime.date.today()), date_format)
             b = datetime.datetime.strptime(str(t.currentdate), date_format)
             t.account_age = (a - b).days
             t.save()
             return render(request, 'show_account_info.html', {'acinfo': acinfo, 't': t})
        except UserProfileInfo.DoesNotExist:
             return render(request, 'show_account_info.html', {'acinfo': acinfo})
             #return None
    acinfo = 0
    return render(request, 'show_account_info.html', {'acinfo': acinfo})


def show_balance_info(request):
    if request.user.is_authenticated:
        try:
            bainfo = deposit.objects.filter(username=request.user)
            t = deposit.objects.get(username=request.user)

            t2 = UserProfileInfo.objects.get(user=request.user)
            date_format = '%Y-%m-%d'
            a = datetime.datetime.strptime(str(datetime.date.today()), date_format)
            b = datetime.datetime.strptime(str(t2.currentdate), date_format)
            t2.account_age = (a - b).days
            t2.save()
            if int(t2.account_age) >= 30 and int(t.trigger) == 0:
                t.monthly_interest_balance = (103 / 100) * float(t.interest_balance)
                t.trigger = 1
                t.save()
            if int(t2.account_age) >= 30 and int(t.trigger) == 1:
                update = priceOfGold.objects.last()
                t.interest_balance = (float(update.gold_price) / float(t.gold_price_at_creation)) * float(t.monthly_interest_balance)
                gram = (1 / update.gold_price) * float(t.monthly_interest_balance)
                t.balance_in_gold = gram
                t.save()
            if int(t2.account_age) >= 60 and int(t.trigger) == 1:
                t.monthly_interest_balance = (103 / 100) * float(t.interest_balance)
                t.trigger = 2
                t.save()
            if int(t2.account_age) >= 60 and int(t.trigger) == 2:
                update = priceOfGold.objects.last()
                t.interest_balance = (float(update.gold_price) / float(t.gold_price_at_creation)) * float(t.monthly_interest_balance)
                gram = (1 / update.gold_price) * float(t.monthly_interest_balance)
                t.balance_in_gold = gram
                t.save()
            if int(t2.account_age) >= 90 and int(t.trigger) == 2:
                t.monthly_interest_balance = (103 / 100) * float(t.interest_balance)
                t.trigger = 3
                t.save()
            if int(t2.account_age) >= 90 and int(t.trigger) == 3:
                update = priceOfGold.objects.last()
                t.interest_balance = (float(update.gold_price) / float(t.gold_price_at_creation)) * float(t.monthly_interest_balance)
                gram = (1 / update.gold_price) * float(t.monthly_interest_balance)
                t.balance_in_gold = gram
                t.save()
            if int(t2.account_age) >= 120 and int(t.trigger) == 3:
                t.monthly_interest_balance = (103 / 100) * float(t.interest_balance)
                t.trigger = 4
                t.save()
            if int(t2.account_age) >= 120 and int(t.trigger) == 4:
                update = priceOfGold.objects.last()
                t.interest_balance = (float(update.gold_price) / float(t.gold_price_at_creation)) * float(t.monthly_interest_balance)
                gram = (1 / update.gold_price) * float(t.monthly_interest_balance)
                t.balance_in_gold = gram
                t.save()
            if int(t2.account_age) < 30:
                update = priceOfGold.objects.last()
                t.interest_balance = (float(update.gold_price) / float(t.gold_price_at_creation)) * float(t.balance)
                gram = (1 / update.gold_price) * float(t.balance)
                t.balance_in_gold = gram
                t.save()
            return render(request, 'show_balance_info.html', {'bainfo': bainfo, 't2': t2})
        except deposit.DoesNotExist:
            bainfo = 'x'
            return render(request, 'show_balance_info.html', {'bainfo': bainfo})
            #return None
    bainfo = 0
    return render(request, 'show_balance_info.html', {'bainfo': bainfo})


def show_loan_info(request):
    if request.user.is_authenticated:
        try:
            lninfo = loan.objects.filter(username=request.user)
            if lninfo.count() == 0:
                lninfo = 'x'
            return render(request, 'show_loan_info.html', {'lninfo': lninfo})
        except loan.DoesNotExist:
            lninfo = 'x'
            return render(request, 'show_loan_info.html', {'lninfo': lninfo})
            #return None
    lninfo = 0
    return render(request, 'show_loan_info.html', {'lninfo': lninfo})


def show_purchase_info(request):
    if request.user.is_authenticated:
        try:
            acinfo = products.objects.filter(username=request.user)
            if acinfo.count() == 0:
                acinfo = 'x'
            return render(request, 'show_purchase_info.html', {'acinfo': acinfo})
        except products.DoesNotExist:
            acinfo = 'x'
            return render(request, 'show_purchase_info.html', {'acinfo': acinfo})
             #return None
    acinfo = 0
    return render(request, 'show_purchase_info.html', {'acinfo': acinfo})


def show_deposit_history(request):
    if request.user.is_authenticated:
        try:
            temp = deposit_history.objects.filter(username=request.user)
            if temp.count() == 0:
                temp = 'x'
            return render(request, 'show_deposit_history.html', {'temp': temp})
        except deposit_history.DoesNotExist:
            temp = 'x'
            return render(request, 'show_deposit_history.html', {'temp': temp})
            #return None
    temp = 0
    return render(request, 'show_deposit_history.html', {'temp': temp})


def show_withdraw_history(request):
    if request.user.is_authenticated:
        try:
            temp = withdraw_history.objects.filter(username=request.user)
            if temp.count() == 0:
                temp = 'x'
            return render(request, 'show_withdraw_history.html', {'temp': temp})
        except withdraw_history.DoesNotExist:
            temp = 'x'
            return render(request, 'show_withdraw_history.html', {'temp': temp})
            #return None
    temp = 0
    return render(request, 'show_withdraw_history.html', {'temp': temp})


def buy_gold(request):
    registered = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        quantity = request.POST.get('quantity')
        mydata = products()
        mydata.username = username
        mydata.password = password
        mydata.quantity = quantity

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    t = deposit.objects.get(username=username)
                    update = priceOfGold.objects.last()
                    temp = 5 * float(quantity) * float(update.gold_price)

                    t2 = UserProfileInfo.objects.get(user=request.user)
                    date_format = '%Y-%m-%d'
                    a = datetime.datetime.strptime(str(datetime.date.today()), date_format)
                    b = datetime.datetime.strptime(str(t2.currentdate), date_format)
                    t2.account_age = (a - b).days
                    t2.save()
                    if int(t2.account_age) < 30:
                        if t.balance >= temp:
                            t.balance = float(t.balance) - float(temp)
                            mydata.price = temp
                            mydata.currentdate = timezone.now()
                            mydata.coin_type = 'Gold Coin'
                            mydata.coin_picture = "/profiles_coin/gold.png"
                            t.save()
                            mydata.save()
                            registered = 'b'
                            return render(request, 'buy_gold.html', {'registered': registered, 'mydata': mydata})
                        else:
                            registered = 'd'
                            return render(request, 'buy_gold.html', {'registered': registered, 'mydata': mydata})
                    if int(t2.account_age) >= 30:
                        if t.monthly_interest_balance >= temp:
                            t.monthly_interest_balance = float(t.monthly_interest_balance) - float(temp)
                            mydata.price = temp
                            mydata.currentdate = timezone.now()
                            mydata.coin_type = 'Gold Coin'
                            mydata.coin_picture = "/profiles_coin/gold.png"
                            t.save()
                            mydata.save()
                            registered = 'b'
                            return render(request, 'buy_gold.html', {'registered': registered, 'mydata': mydata})
                        else:
                            registered = 'd'
                            return render(request, 'buy_gold.html', {'registered': registered, 'mydata': mydata})
                except deposit.DoesNotExist:
                    registered = 'e'
                    return render(request, 'buy_gold.html', {'registered': registered, 'mydata': mydata})
        else:
            registered = 'c'

    return render(request, 'buy_gold.html', {'registered': registered})


def buy_silver(request):
    registered = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        quantity = request.POST.get('quantity')
        mydata = products()
        mydata.username = username
        mydata.password = password
        mydata.quantity = quantity

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    t = deposit.objects.get(username=username)
                    temp = 5 * float(quantity) * 87

                    t2 = UserProfileInfo.objects.get(user=request.user)
                    date_format = '%Y-%m-%d'
                    a = datetime.datetime.strptime(str(datetime.date.today()), date_format)
                    b = datetime.datetime.strptime(str(t2.currentdate), date_format)
                    t2.account_age = (a - b).days
                    t2.save()
                    if int(t2.account_age) < 30:
                        if t.balance >= temp:
                            t.balance = float(t.balance) - float(temp)
                            mydata.price = temp
                            mydata.currentdate = timezone.now()
                            mydata.coin_type = 'Silver Coin'
                            mydata.coin_picture = "/profiles_coin/silver.png"
                            t.save()
                            mydata.save()
                            registered = 'b'
                            return render(request, 'buy_silver.html', {'registered': registered, 'mydata': mydata})
                        else:
                            registered = 'd'
                            return render(request, 'buy_silver.html', {'registered': registered, 'mydata': mydata})
                    if int(t2.account_age) >= 30:
                        if t.monthly_interest_balance >= temp:
                            t.monthly_interest_balance = float(t.monthly_interest_balance) - float(temp)
                            mydata.price = temp
                            mydata.currentdate = timezone.now()
                            mydata.coin_type = 'Silver Coin'
                            mydata.coin_picture = "/profiles_coin/silver.png"
                            t.save()
                            mydata.save()
                            registered = 'b'
                            return render(request, 'buy_silver.html', {'registered': registered, 'mydata': mydata})
                        else:
                            registered = 'd'
                            return render(request, 'buy_silver.html', {'registered': registered, 'mydata': mydata})
                except deposit.DoesNotExist:
                    registered = 'e'
                    return render(request, 'buy_gold.html', {'registered': registered, 'mydata': mydata})
        else:
            registered = 'c'

    return render(request, 'buy_silver.html', {'registered': registered})


def buy_bronze(request):
    registered = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        quantity = request.POST.get('quantity')
        mydata = products()
        mydata.username = username
        mydata.password = password
        mydata.quantity = quantity

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    t = deposit.objects.get(username=username)
                    temp = 5 * float(quantity) * 67

                    t2 = UserProfileInfo.objects.get(user=request.user)
                    date_format = '%Y-%m-%d'
                    a = datetime.datetime.strptime(str(datetime.date.today()), date_format)
                    b = datetime.datetime.strptime(str(t2.currentdate), date_format)
                    t2.account_age = (a - b).days
                    t2.save()
                    if int(t2.account_age) < 30:
                        if t.balance >= temp:
                            t.balance = float(t.balance) - float(temp)
                            mydata.price = temp
                            mydata.currentdate = timezone.now()
                            mydata.coin_type = 'Bronze Coin'
                            mydata.coin_picture = "/profiles_coin/bronze.png"
                            t.save()
                            mydata.save()
                            registered = 'b'
                            return render(request, 'buy_bronze.html', {'registered': registered, 'mydata': mydata})
                        else:
                            registered = 'd'
                            return render(request, 'buy_bronze.html', {'registered': registered, 'mydata': mydata})
                    if int(t2.account_age) >= 30:
                        if t.monthly_interest_balance >= temp:
                            t.monthly_interest_balance = float(t.monthly_interest_balance) - float(temp)
                            mydata.price = temp
                            mydata.currentdate = timezone.now()
                            mydata.coin_type = 'Bronze Coin'
                            mydata.coin_picture = "/profiles_coin/bronze.png"
                            t.save()
                            mydata.save()
                            registered = 'b'
                            return render(request, 'buy_bronze.html', {'registered': registered, 'mydata': mydata})
                        else:
                            registered = 'd'
                            return render(request, 'buy_bronze.html', {'registered': registered, 'mydata': mydata})
                except deposit.DoesNotExist:
                    registered = 'e'
                    return render(request, 'buy_gold.html', {'registered': registered, 'mydata': mydata})
        else:
            registered = 'c'

    return render(request, 'buy_bronze.html', {'registered': registered})


def depositamount(request):
    registered = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        balance = request.POST.get('balance')
        mydata = deposit()
        mydata.username = username
        mydata.password = password
        mydata.email = email
        mydata.balance = balance

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    t3 = UserProfileInfo.objects.get(user=request.user)
                    date_format = '%Y-%m-%d'
                    a = datetime.datetime.strptime(str(datetime.date.today()), date_format)
                    b = datetime.datetime.strptime(str(t3.currentdate), date_format)
                    t3.account_age = (a - b).days
                    t3.save()
                    if int(t3.account_age) < 30:
                        t = deposit.objects.get(username=username)
                        t.currentdate = timezone.now()
                        prev_obj = copy.copy(t)
                        res = float(balance) + float(prev_obj.balance)
                        t.email = email
                        t.balance = res

                        update = priceOfGold.objects.last()
                        gram = (1 / update.gold_price) * float(t.balance)
                        t.balance_in_gold = gram
                        t.save()

                        depo = deposit_history()
                        depo.username = username
                        depo.email = email
                        depo.currentdate = timezone.now()
                        depo.amount = balance
                        depo.save()
                    if int(t3.account_age) >= 30:
                        t = deposit.objects.get(username=username)
                        t.currentdate = timezone.now()
                        prev_obj = copy.copy(t)
                        res = float(balance) + float(prev_obj.monthly_interest_balance)
                        t.email = email
                        t.monthly_interest_balance = res

                        update = priceOfGold.objects.last()
                        gram = (1 / update.gold_price) * float(t.monthly_interest_balance)
                        t.balance_in_gold = gram
                        t.save()

                        depo = deposit_history()
                        depo.username = username
                        depo.email = email
                        depo.currentdate = timezone.now()
                        depo.amount = balance
                        depo.save()
                except deposit.DoesNotExist:
                    t3 = UserProfileInfo.objects.get(user=request.user)
                    date_format = '%Y-%m-%d'
                    a = datetime.datetime.strptime(str(datetime.date.today()), date_format)
                    b = datetime.datetime.strptime(str(t3.currentdate), date_format)
                    t3.account_age = (a - b).days
                    t3.save()

                    depo = deposit_history()
                    depo.username = username
                    depo.email = email
                    depo.currentdate = timezone.now()
                    depo.amount = balance
                    depo.save()
                    if int(t3.account_age) < 30:
                        update = priceOfGold.objects.last()
                        gram = (1 / update.gold_price) * float(mydata.balance)
                        mydata.balance_in_gold = gram
                        mydata.initial_balance = float(balance)

                        mydata.currentdate = timezone.now()
                        update = priceOfGold.objects.last()
                        mydata.gold_price_at_creation = update.gold_price
                        mydata.save()
                    if int(t3.account_age) >= 30:
                        update = priceOfGold.objects.last()
                        gram = (1 / update.gold_price) * float(mydata.monthly_interest_balance)
                        mydata.balance_in_gold = gram

                        mydata.currentdate = timezone.now()
                        update = priceOfGold.objects.last()
                        mydata.gold_price_at_creation = update.gold_price
                        mydata.save()
                registered = 'b'
        else:
            registered = 'c'

    return render(request, 'depositamount.html', {'registered': registered})



def withdrawamount(request):
    registered = 'a'
    y = 'x'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        balance = request.POST.get('balance')
        mydata = deposit()
        mydata.username = username
        mydata.password = password
        mydata.email = email
        mydata.balance = balance

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    t = deposit.objects.get(username=username)
                    t3 = UserProfileInfo.objects.get(user=request.user)

                    date_format = '%Y-%m-%d'
                    a = datetime.datetime.strptime(str(datetime.date.today()), date_format)
                    b = datetime.datetime.strptime(str(t3.currentdate), date_format)
                    t3.account_age = (a - b).days
                    t3.save()
                    if int(t3.account_age) < 30:
                        t.withdrawdate = timezone.now()
                        t.last_withdraw_amount = balance
                        prev_obj = copy.copy(t)
                        if float(prev_obj.balance) >= float(balance):
                            res = float(prev_obj.balance) - float(balance)
                            t.balance = res
                            t.save()

                            withhis = withdraw_history()
                            withhis.username = username
                            withhis.email = email
                            withhis.currentdate = timezone.now()
                            withhis.amount = balance
                            withhis.save()
                        else:
                            y = 'e'
                    if int(t3.account_age) >= 30:
                        t.withdrawdate = timezone.now()
                        t.last_withdraw_amount = balance
                        prev_obj = copy.copy(t)
                        if float(prev_obj.monthly_interest_balance) >= float(balance):
                            res = float(prev_obj.monthly_interest_balance) - float(balance)
                            t.monthly_interest_balance = res
                            t.save()

                            withhis = withdraw_history()
                            withhis.username = username
                            withhis.email = email
                            withhis.currentdate = timezone.now()
                            withhis.amount = balance
                            withhis.save()
                        else:
                            y = 'e'
                except deposit.DoesNotExist:
                    y = 'd'
                registered = 'b'
                if y == 'd':
                    registered = 'd'
                if y == 'e':
                    registered = 'e'
        else:
            registered = 'c'

    return render(request, 'withdrawamount.html', {'registered': registered})


def loanamount(request):
    registered = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        mydata = loan()
        mydata.username = username
        mydata.password = password
        mydata.email = email
        mydata.amount = amount

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    # t = loan.objects.get(username=username)
                    mydata.currentdate = timezone.now().date()
                    mydata.return_date = mydata.currentdate + datetime.timedelta(days=182)

                    # prev_obj = copy.copy(t)
                    res = float(amount)
                    mydata.return_amount = (105 / 100) * res
                    mydata.amount = res
                    mydata.status = 'Due'
                    mydata.save()

                    t2 = bankMoney.objects.get(serial=1)
                    t2.amount = float(t2.amount) - float(amount)
                    t2.save()
                except loan.DoesNotExist:
                    mydata.currentdate = timezone.now().date()
                    mydata.return_date = mydata.currentdate + datetime.timedelta(days=182)

                    t2 = bankMoney.objects.get(serial=1)
                    t2.amount = float(t2.amount) - float(amount)
                    t2.save()
                    mydata.return_amount = (105 / 100) * float(amount)
                    mydata.status = 'Due'
                    mydata.save()
                registered = 'b'
        else:
            registered = 'c'

    return render(request, 'loan.html', {'registered': registered})


def loan_return(request):
    # t3 = loan.objects.get(username=request.user)
    registered = 'a'
    temp = 'x'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        id = request.POST.get('id')
        mydata = loan()
        mydata.username = username
        mydata.password = password
        mydata.id = id

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    t = loan.objects.get(username=username,id=id)
                    if t.status == 'Returned':
                        temp = 'y'
                        return render(request, 'return_loan.html', {'registered': registered, 'temp': temp})
                    if t.status == 'Due':
                        t2 = bankMoney.objects.get(serial=1)
                        t2.amount = float(t2.amount) + float(t.return_amount)
                        t2.save()

                        t.bank_profit = float(t.return_amount) - float(t.amount)
                        t.status = 'Returned'
                        t.save()
                        temp = 'z'
                        # registered = 'b'
                        return render(request, 'return_loan.html', {'registered': registered, 'temp': temp})
                except loan.DoesNotExist:
                    registered = 'd'
                    return render(request, 'return_loan.html', {'registered': registered, 'id': id})
        else:
            registered = 'c'
    return render(request, 'return_loan.html', {'registered': registered})



def bankTotalMoney(request):
    add = 'a'
    if request.method == 'POST':
        serial = request.POST.get('serial')
        amount = request.POST.get('amount')

        mydatanew = bankMoney()
        mydatanew.serial = serial
        mydatanew.amount = amount

        mydatanew.save()
        add = 'b'
    return render(request, 'bank_money.html', {'add': add})


def transfer_gold(request):
    temp = 'a'
    if request.method == 'POST':
        username1 = request.POST.get('own_username')
        password1 = request.POST.get('own_pass')

        username2 = request.POST.get('another_username')


        amount = request.POST.get('gold_amount')

        mydata = deposit()
        mydata.username = username1
        mydata.password = password1

        mydata.username = username2


        user = authenticate(username=username1, password=password1)
        #user = authenticate(username=username2, password=password2)

        if user:
            if user.is_active:
                try:
                    t = deposit.objects.get(username=username2)
                    t2 = deposit.objects.get(username=username1)

                    t3 = UserProfileInfo.objects.get(user=request.user)
                    # t4 = UserProfileInfo.objects.get(user=request.user)


                    update1 = priceOfGold.objects.last()

                    res = float(update1.gold_price) * float(amount)

                    if int(t3.account_age) < 30:
                        if (float(t2.balance_in_gold) >= float(amount)):

                            update = float(amount) + float(t.balance_in_gold)
                            money_update = float(t.balance) + res
                            t.balance_in_gold = update
                            t.balance = money_update

                            t.save()

                            t2.balance_in_gold = float(t2.balance_in_gold) - float(amount)
                            money_update2 = float(t2.balance) - res
                            t2.balance = money_update2
                            t2.save()
                            temp = 'b'
                        else:
                            temp = 'c'
                    if int(t3.account_age) >= 30:
                        if (float(t2.balance_in_gold) >= float(amount)):

                            update = float(amount) + float(t.balance_in_gold)
                            money_update = float(t.balance) + res
                            t.balance_in_gold = update
                            t.balance = money_update

                            t.save()

                            t2.balance_in_gold = float(t2.balance_in_gold) - float(amount)
                            money_update2 = float(t2.monthly_interest_balance) - res
                            t2.monthly_interest_balance = money_update2
                            t2.save()
                            temp = 'b'
                        else:
                            temp = 'c'
                except deposit.DoesNotExist:
                    temp = 'd'
        else:
            temp = 'e'

    return render(request, 'transferGold.html', {'temp': temp})

