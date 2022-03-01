from django.forms.models import model_to_dict
from django.http import JsonResponse

from inventory.models import Product

# Create your views here.
def validate(request, code):
    item = Product.objects.filter(serial=code).first()
    data = {'result':'fake'}
    if item:
        data = model_to_dict(item)
        data['result'] = 'original'
    return JsonResponse(data)