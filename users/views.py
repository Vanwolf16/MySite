from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import NewUserForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp/products')
    form = NewUserForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html',context)