from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Product, BlogPost


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


class BlogPostListView(ListView):
    model = BlogPost
    # По умолчанию использует 'blogpost_list.html'


class BlogPostDetailView(DetailView):
    model = BlogPost
    # По умолчанию использует 'blogpost_detail.html'


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'slug', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('catalog:blogpost_list')
    # По умолчанию использует 'blogpost_form.html'


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'slug', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('catalog:blogpost_list')
    # По умолчанию использует 'blogpost_form.html'


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:blogpost_list')
    # По умолчанию использует 'blogpost_confirm_delete.html'
