from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("email")
            messages.success = (request, f"Hey {username}, You have successfully logged in")
            new_user = authenticate(username = form.cleaned_data['username'],
                                   password = form.cleaned_data['password1']
            )
            login =(request, new_user)
            return redirect("core:index")
        
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form,
    }
    return render(request, 'sign_up.html', context)
