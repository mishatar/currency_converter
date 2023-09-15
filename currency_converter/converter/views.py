from django.http import HttpResponse
from .services import calc_rate
from rest_framework.response import Response
from rest_framework.views import APIView


class Index(APIView):

    def get(self, request):
        from_currency = request.GET.get("from")
        to_currency = request.GET.get("to")
        value = request.GET.get("value")
        result = calc_rate(from_currency, to_currency, value)
        return Response(
            {"Result": result},
        )
        # return HttpResponse(f"<h3>Result = {result}</h3>")