from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import CreateView, View, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.utils import json
from xhtml2pdf import pisa
from .forms import *
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from django.urls import reverse_lazy
from django.http import HttpResponse
from io import BytesIO


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()           # выборка данных, которую приложение будет возвращать
    serializer_class = CategorySerializer       # класс сериализатора для модели


class TypeWorkView(ModelViewSet):
    queryset = TypeWork.objects.all()
    serializer_class = TypeWorkSerializer


#@csrf_exempt
def OrderList(request):
    if request.method == 'POST':
        data_str = request.body.decode('utf-8')     # request.body - сами данные, отправленные клиентом в бинарном представлении, которые мы переводим в строку
        data_dict = json.loads(data_str)            # перводим строку в json

        id_user = data_dict['order']['id_user']     # получаем order, затем id_user
        user = User(id=id_user)                     # находим соответствующего пользователя в таблице User
        order = Order(id_user=user)                 # делаем объект в таблице Order
        order.save()                                # и сохраняем

        for work in data_dict['order_works']:
            id_work=work['id_work']                 # берем текущую работу
            type_work = TypeWork(id=id_work)        # находим соответствующую работу в таблице TypeWork
            order_work = OrderWork(id_order=order, id_work=type_work)     # делаем объект в таблице OrderWorks
            order_work.save()                       # и сохраняем

    return JsonResponse({'status': 'success'})      # возврат на клиент (отклик)


def render_app(request):
    сlient = User.objects.all()
    return render(request, 'calculation.html', {'сlient': сlient})


def render_thanks(request):
    return render(request, 'thanks.html')


def render_category(request):
    categories = Category.objects.all()
    return render(request, 'admin_category.html', {'categories': categories})


def render_work(request):
    works = TypeWork.objects.all()
    return render(request, 'admin_work.html', {'works': works})


def render_estimate(request):
    """Вывод сметы"""
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    orders = Order.objects.get(id_user=user_id)
    works = OrderWork.objects.filter(id_order=orders.id)
    types = TypeWork.objects.all()
    categories = Category.objects.all()
    return render(request, 'estimates.html', {'user': user, 'orders': orders, 'works': works, 'types': types, 'categories': categories})


def render_to_pdf(template_src, context_dict={}):
    """Преобразование в PDF"""
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result, encoding='utf-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePdf(View):
    """Вывод PDF-файла"""
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        orders = Order.objects.get(id_user=user_id)
        works = OrderWork.objects.filter(id_order=orders.id)
        types = TypeWork.objects.all()
        categories = Category.objects.all()
        pdf = render_to_pdf('estimates.html', {'user': user, 'orders': orders, 'works': works, 'types': types, 'categories': categories})
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPdf(View):
    """Загрузка PDF-файла"""
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        orders = Order.objects.get(id_user=user_id)
        works = OrderWork.objects.filter(id_order=orders.id)
        types = TypeWork.objects.all()
        categories = Category.objects.all()
        pdf = render_to_pdf('estimates.html', {'user': user, 'orders': orders, 'works': works, 'types': types, 'categories': categories})
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Estimate.pdf'
        content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response


class CategoryCreateView(CreateView):
    template_name = 'add.html'
    form_class = CategoryForm
    permission_required = ''
    raise_exception = True      # для вывода ошибки

    def get_success_url(self):
        # для возвращения на главную страницу
        return reverse_lazy('calculation')


class CategoryUpdateView(UpdateView):
    template_name = 'add.html'
    model = Category
    form_class = CategoryForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('calculation')


class CategoryDeleteView(DeleteView):
    template_name = 'add.html'
    model = Category
    form_class = CategoryForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('calculation')


class TypeWorkCreateView(CreateView):
    template_name = 'add.html'
    form_class = TypeWorkForm
    permission_required = ''
    raise_exception = True      # для вывода ошибки

    def get_success_url(self):
        # для возвращения на главную страницу
        return reverse_lazy('calculation')


class TypeWorkUpdateView(UpdateView):
    template_name = 'add.html'
    model = Category
    form_class = TypeWorkForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('calculation')


class TypeWorkDeleteView(DeleteView):
    template_name = 'add.html'
    model = Category
    form_class = TypeWorkForm
    permission_required = ''
    raise_exception = True

    def get_success_url(self):
        return reverse_lazy('calculation')


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        # получение данных
        form = UserLoginForm(request.POST or None)
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # отправка данных в БД
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')                # если все правильно возвращаем на главную страницу
        return render(request, 'login.html', {'form': form})


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
