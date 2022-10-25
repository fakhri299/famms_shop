from django.shortcuts import get_object_or_404
from django.shortcuts import render
from paltar.models import Category
from paltar.models import Product
from django.views.generic import ListView



# Create your views here.


def products(request,category_slug=None):

   categories=Category.objects.all()
   
   # category_paltar=Paltar.objects.filter(kategoriya__slug=kategoriya_slug)
   
   if category_slug!=None:
      category_page=get_object_or_404(Category,slug=category_slug)
      products = Product.objects.filter(category=category_page)

   else:
      products=Product.objects.all().order_by('-add_date')
   

   context={
        
         "products":products,
         "categories":categories,
         
         
   }

   return render(request,'product.html',context)


def product_detail(request,product_id):
   product=Product.objects.get(id=product_id)
   current_user=request.user
   

   if current_user.is_authenticated:
        bought_products = current_user.product_client.all()

   else:
         
      bought_products = product


   context={"product":product,
            "bought_products":bought_products,}


   return render(request,"paltar.html",context)





class ProductListView(ListView):
    model = Product      # shorthand for setting queryset = models.Car.objects.all()
    template_name = 'product.html'  # optional (the default is app_name/modelNameInLowerCase_list.html; which will look into your templates folder for that path and file)
    context_object_name = "products"    #default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 5  #and that's it !!
