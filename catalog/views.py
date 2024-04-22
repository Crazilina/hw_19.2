from django.views.generic import ListView, DetailView, View
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog/contacts.html')

    @ensure_csrf_cookie
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Обработка данных формы

        print(f"Пользователь {name} с email {email} отправил следующее сообщение:")
        print(message)

        return HttpResponse("Спасибо за обратную связь!")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
