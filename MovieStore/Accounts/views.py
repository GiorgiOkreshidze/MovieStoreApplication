from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect

# Create your views here.
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data' : template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('home.index')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data' : template_data})
