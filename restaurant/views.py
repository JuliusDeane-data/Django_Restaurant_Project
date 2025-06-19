from http import HTTPStatus
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Meal, OrderTransaction
from .forms import UserLoginForm
# Create your views here.


def error_404_view(request, exception):
    return redirect('index')


class IndexView(View):
    def get(self, request):
        all_meals = Meal.objects.all().order_by('id')
        context = {'meals': all_meals}

        return render(request, 'restaurant/index.html', context)


class OrderView(View):
    def get(self, request, pk=None):
        if request.user != AnonymousUser():
            if pk:
                got_meal = Meal.objects.filter(id=pk).last()
                if got_meal and got_meal.stock > 0:
                    OrderTransaction.objects.create(meal=got_meal, customer=request.user, amount=got_meal.price)
                    got_meal.stock -= 1
                    got_meal.save()

                    return redirect('index')
        return HttpResponse(HTTPStatus.BAD_REQUEST)


class DetailsView(ListView):
    context_object_name = 'transactions'
    template_name = 'restaurant/details.html'

    def get_queryset(self):
        return OrderTransaction.objects.filter(customer=self.request.user)


class CustomLoginView(View):
    form_class = UserLoginForm
    template_name = 'restaurant/login.html'

    def get(self, request):
        form = self.form_class()
        form.fields['password'].widget.attrs['placeholder'] = 'Your Password'
        form.fields['password'].widget.attrs['id'] = 'password_id'
        context = {
            'login_form': form
        }

        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            authenticateUser = authenticate(request, username=username, password=password)

            if authenticateUser:
                login(request, authenticateUser)
                return redirect('index')

        context = {
                'login_form': form
            }
        return render(request=request, template_name=self.template_name, context=context)


def logoutUser(request):
    logout(request)
    return redirect('index')
