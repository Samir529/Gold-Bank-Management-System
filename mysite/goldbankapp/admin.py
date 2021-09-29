
from django.contrib import admin
from .models import UserProfileInfo, priceOfGold, deposit, bankMoney, loan, products, withdraw_history, deposit_history

admin.site.site_header = 'Gold Bank admin'
admin.site.site_title = 'Gold Bank admin'
admin.site.index_title = 'Gold Bank administration'

admin.site.register(UserProfileInfo)
admin.site.register(priceOfGold)
admin.site.register(deposit)
admin.site.register(loan)
admin.site.register(bankMoney)
admin.site.register(products)
admin.site.register(deposit_history)
admin.site.register(withdraw_history)
