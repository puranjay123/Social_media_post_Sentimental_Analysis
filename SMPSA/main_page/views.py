from django.shortcuts import render

# Create your views here.
# Landing view of the website
def landing_page(request):
    return render(request,"main_page/html/main_page.html")