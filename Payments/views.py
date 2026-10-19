from django.shortcuts import render
from . import services
# Create your views here.
def home_view(request):
    if request.method=="POST":
        clean_phone=request.POST.get("phone")
        phone=clean_phone.lstrip('+')
        amount=request.POST.get("amount")
        stk=services.STKPUSH(phone, amount)
        stk.stkpush()
        print(f"You are about to receive {amount} from {phone}")
    return render(request, "payments/mpesa.html")

def save_pay_records(request):
    pass
