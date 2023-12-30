from django.shortcuts import render

# Create your views here.

def IndexView(request):
  return render(request,'app/index.html')
def Forms(request):
  return render(request,'app/forms.html')