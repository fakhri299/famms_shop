from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from .forms import ContactForm
from paltar.models import Product,Category

# Create your views here.



def home(request):
   last_products=Product.objects.all().order_by('-add_date')[:12]

   categories=Category.objects.all()

   context={"last_products":last_products,"categories":categories}

   return render(request,'index.html',context)


def testimonial(request):
   return render(request,'testimonial.html')


def about(request):
   # categories=Category.objects.all()
   # context={'categories':categories}
   return render(request,'about.html')



def search(request):

   result=request.GET['search_product']
   
   products=Product.objects.filter(name__contains=result)
   

   context={'products':products}

   return render(request,'product.html',context)


class ContactView(SuccessMessageMixin,FormView):
    template_name='contact.html'
    form_class= ContactForm
    success_url=reverse_lazy('contact')
    success_message='We recieved your request'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

    