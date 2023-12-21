from django.contrib.auth import login , authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        
            # return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request , username = username, password= password)

#         if user is not None:
#             login(request, user)
#             return redirect('room:room.html')
#         else:
#             return render(request, 'login.html', {'error_message': 'Invalid credentials'})
        
#     return render(request, 'login.html')