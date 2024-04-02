from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


@ensure_csrf_cookie
def contacts(request):
    if request.method == 'POST':
        # Если запрос - POST, значит пользователь отправил данные формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Теперь можно обрабатывать данные формы, например, отправить их на почту или сохранить в базе данных

        # В данном примере просто выведем данные на экран
        print(f"Пользователь {name} с email {email} отправил следующее сообщение:")
        print(message)

        # Далее можно добавить код для отправки письма администратору или сохранения данных в базу данных

        # После обработки формы, можно перенаправить пользователя
        # на страницу "Спасибо за обратную связь" или что-то подобное
        return HttpResponse("Спасибо за обратную связь!")
    else:
        # Если запрос - GET, просто показываем страницу контактов
        return render(request, 'contacts.html')
