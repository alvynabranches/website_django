from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from home.forms import DemoForm
from home.models import DemoModel


# Create your views here.
def index(request):
    show_variables = dict(
        title = 'Home',
        active = dict(home=True, create_account=False)
    )
    return render(request, 'home/index.html', context=show_variables)

@csrf_protect
def create_acc(request):
    form = DemoForm()
    if request.method == 'POST':
        form = DemoForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_no = form.cleaned_data['phone_no']
            profile_pic = form.cleaned_data['profile_pic']
            DemoModel(name=name, phone_no=phone_no, profile_pic=profile_pic).save()
            
            return HttpResponse('Form Successfully Submitted!')
        else:
            return HttpResponse('Form Not Successfully Submitted!')
    return render(request, 'home/create_account.html', 
                context=dict(
                            title = 'Create Account',
                            active = dict(home=False, create_account=True), 
                            form=form
                )
        )