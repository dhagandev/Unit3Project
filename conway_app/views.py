from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin


# signup view function
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
	return render(request, 'home.html')

def rules(request):
	return render(request, 'rules.html')

def consim_create(request):
	return render(request, 'consim/createconsim.html')

def consim_detail(request):
	return render(request, 'consim/viewconsim.html')

def user_profile(request):
	user = User.objects.get(id=user_id)
	return render(request, 'users/profile.html', {'user': user})

