from django.shortcuts import render
from ecapp.models import Products
from ecapp.forms import DetailsForm


# Create your views here.


def fetch_data(request):
    product_list=Products.objects.all()

    item_name=request.GET.get('item_name')
    if item_name!='' and  item_name!=None:
        product_list=product_list.filter(name__contains=item_name)


    my_dict={'product_list':product_list}
    return render(request,"home.html",my_dict)



def displayView(request):
    form=DetailsForm()
    my_dict={'form':form}
    return render(request,"detail.html",my_dict)




def order(request):
    order_amount = 50000
    order_currency = '$'
    client=razorpay.Client(auth=('rzp_test_0jL0GaLT2hFewt','ts914s9Ndp0DeqY6Itt1DTDK'))

    client.order.create(amount=order_amount, currency=order_currency)




def success(request):
    return render(request,"success.html")


