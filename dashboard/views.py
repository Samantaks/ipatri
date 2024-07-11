from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login-page')
def dashboardpage(request):
    return render(request, "app/dashboard.html")
