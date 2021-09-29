from .models import priceOfGold
import datetime

def message_processor(request):
    update = 0
    try:
        update = priceOfGold.objects.last()
    except priceOfGold.DoesNotExist:
        pass
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
        'update': update, 'temp1': temp1
    }
