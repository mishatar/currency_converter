from django.http import HttpResponse
from .parser import calc_rate


def index(request):
    from_currency = request.GET.get("from")
    to_currency = request.GET.get("to")
    value = request.GET.get("value")
    result = calc_rate(from_currency, to_currency, value)
    return HttpResponse(f"<h3>Result = {result}</h3>")