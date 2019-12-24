from django.shortcuts import render
from .forms import CustomForm
# Create your views here.


def home(request):
    context = {
        'form':CustomForm(),
    }
    if request.method=='POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
        context['form']=form
    return render(request,'forms.html',context)
