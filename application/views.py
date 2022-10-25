from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import UsersInfo
from .form import Userform
# Create your views here.


def home(request):
    form = Userform()
    context = {'form': form}
    return render(request, 'home.html', context)


@require_POST
def viewresult(request):
    t6 = request.POST.get('t6')
    t7 = request.POST.get('t7')
    t8 = request.POST.get('t8')
    t9 = request.POST.get('t9')
    t10 = request.POST.get('t10')
    t11 = request.POST.get('t11')
    t12 = request.POST.get('t12')
    form = Userform(request.POST)
    pol = request.POST.get('pol')
    lst = [t6, t7, t8, t9, t10, t11, t12]
    resultball1 = 0
    for i in lst:
        resultball1 += int(i)
    resultball1 = resultball1/7
    if pol == 'Мужской':
        if (resultball1 >= 0 and resultball1 <= 0.99):
            r1 = 'Низкий'
        elif (resultball1 >= 1 and resultball1 <= 1.99):
            r1 = 'Средний'
        else:
            r1 = 'Высокий'
    else:
        if (resultball1 >= 0 and resultball1 <= 1.17):
            r1 = 'Низкий'
        elif (resultball1 >= 1.18 and resultball1 <= 2.7):
            r1 = 'Средний'
        else:
            r1 = 'Высокий'
    if form.is_valid():
        new = UsersInfo(fio=request.POST['fio'])
        new.save()
    context = {'form': form, 'r1': r1}
    return render(request, 'result.html', context)


def viewresult2(request):
    try:
        form = Userform(request.POST)
        t1 = request.POST.get('flexRadioDefault')
        t2 = request.POST.get('flexRadioDefault2')
        t3 = request.POST.get('flexRadioDefault3')
        t4 = request.POST.get('flexRadioDefault4')
        t5 = request.POST.get('flexRadioDefault5')
        lst2 = [t1, t2, t3, t4, t5]
        resultball2 = 0
        for i in lst2:
            resultball2 += int(i)
        if resultball2 <= 5:
            r2 = 'Нет нарушений'
        elif resultball2 > 5 and resultball2 <= 10:
            r2 = 'Умеренные нарушения здоровья'
        else:
            r2 = 'Выраженные нарушения здоровья'
        if form.is_valid():
            new = UsersInfo(fio=request.POST['fio'])
            new.save()
        context2 = {'form': form, 'r2': r2}
        return render(request, 'result2.html', context2)
    except:
        return render(request, 'home.html')
