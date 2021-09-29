from .models import priceOfGold
import datetime

def message_processor(request):
    update1 = priceOfGold.objects.last()
    currentTime = datetime.datetime.now()
    if 5 <= currentTime.hour < 12:
        temp1 = 'morning'
    elif 12 <= currentTime.hour < 17:
        temp1 = 'afternoon'
    elif 17 <= currentTime.hour < 21:
        temp1 = 'evening'
    else:
        temp1 = 'night'
    return {
        'update1': update1, 'temp1': temp1
    }
