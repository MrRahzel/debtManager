from django.shortcuts import render
from django.db import models

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib import messages
from .models import Usvers
from .models import Products
from .models import *
from .forms import RegisterUserForm
from .forms import *
from .apps import *
from .signal_for_products import update_product
from django.db.models import Sum

from .apps import model_st
import random
from statistics import mean
from collections import Counter

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.db import connection, reset_queries

def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            #phone = form.cleaned_data.get('phone')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user =authenticate(username=username,password=password, email=email, phone=phone, first_name=first_name, last_name=last_name)
            instance = Usvers(user = user, balance = 5, phone=phone)
            instance.save()
            login(request, user)
            
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request, 'signup.html', {'form': form})

def signupNKO(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            NKO = form.cleaned_data.get('NKO')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user =authenticate(username=username,password=password, email=email, phone=phone, first_name=first_name, last_name=last_name)
            instance = Usvers(user = user, balance = 5, phone=phone, is_NKO = True, NKO_name=NKO)
            instance.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterUserForm()
    return render(request, 'signupNKO.html', {'form': form})

def sign_b(request):

    return render(request, 'signup_before.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        query = ""
        msg=""
        if request.method == "POST":
            try:
                username = request.POST["username"]
                amount = request.POST["amount"]
                senderUser = User.objects.get(username=request.user.username)
                receiverrUser =  User.objects.get(username=username)
                sender = Usvers.objects.get(user = senderUser)
                receiverr = Usvers.objects.get(user = receiverrUser)
                if ((sender.balance > 0) and ((sender.balance - int(amount)) >= 0)):
                    sender.balance = sender.balance - int(amount)
                    receiverr.balance = receiverr.balance + int(amount)
                sender.save()
                receiverr.save()
                msg = "Transaction Success"
                return redirect('profile')
            except Exception as e:
                print(e)
                msg = "Transaction Failure, Please check and try again"
                return redirect('profile')
        data = Products.objects.all()
        databal = Usvers.objects.all().filter(is_superuser = False)
        #databal2 = databal.user_id > 1
        adm = User.objects.get(username='Admin1')
        adm2 = Usvers.objects.get(user=adm)
        #adm3 = databal - adm2
        total_sum = sum(data.values_list('price', flat=True))
        bal_sum = sum(databal.values_list('balance', flat=True))
        adm2.balance = total_sum - bal_sum
        adm2.save()
        usver = Usvers.objects.get(user=request.user)
        user2 = Usvers.objects.all()

        return render(request,'profile.html',{"balance":usver.balance, "NKO_name":usver.NKO_name, "is_NKO":usver.is_NKO, "phone":usver.phone,"msg":msg, "userlist" : user2, "query":query})

import datetime
def totaldonation(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        object_list = Products.objects.all()
        msg=""
        if request.method == "POST":
            try:
                username = request.POST["username"]
                amount = request.POST["amount"]
                senderUser = User.objects.get(username=request.user.username)
                receiverrUser =  User.objects.get(username=username)
                sender = Usvers.objects.get(user = senderUser)
                receiverr = Usvers.objects.get(user = receiverrUser)
                vr = datetime.datetime.now()
                tr = Transacts.objects.create(user11 = sender, user22 = receiverr, colvo1 = amount, time1 = vr)
                if ((sender.balance > 0) and ((sender.balance - int(amount)) >= 0)):
                    sender.balance = sender.balance - int(amount)
                    receiverr.balance = receiverr.balance + int(amount)
                sender.save()
                receiverr.save()
                tr.save()

                msg = "Transaction Success"
                return redirect('profile')
            except Exception as e:
                print(e)
                msg = "Transaction Failure, Please check and try again"
                return redirect('profile')

        return render(request,'totaldonation.html')

def totaldonation2(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        object_list = Products.objects.get(id=id)
        msg=""
        if request.method == "POST":
            try:
                username = request.POST["username"]
                amount = request.POST["amount"]
                senderUser = User.objects.get(username=request.user.username)
                receiverrUser =  User.objects.get(username=username)
                sender = Usvers.objects.get(user = senderUser)
                receiverr = Usvers.objects.get(user = receiverrUser)
                vr = datetime.datetime.now()
                tr = Transacts.objects.create(user11 = sender, user22 = receiverr, colvo1 = amount, time1 = vr)
                if ((sender.balance > 0) and ((sender.balance - int(amount)) >= 0)):
                    sender.balance = sender.balance - int(amount)
                    receiverr.balance = receiverr.balance + int(amount)
                sender.save()
                receiverr.save()
                tr.save()

                msg = "Transaction Success"
                return redirect('profile')
            except Exception as e:
                print(e)
                msg = "Transaction Failure, Please check and try again"
                return redirect('profile')

        return render(request,'totaldonation2.html', {"object_list":object_list})

def advertisement(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        object_list = Products.objects.get(id=id)
        vr = datetime.datetime.now()
        name = request.GET.get("prod")
        view_c = Product_views.objects.create(user = request.user, product = name, time = vr)
        view_c.save()
        tel = User.objects.select_related("Usvers").all()

        context = {
            "object_list":object_list, 
            "tel":tel,
        }
             
    return render(request,'advertisement.html', context)

def recomendations(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        object_list = Products.objects.get(id=id)
        tel = User.objects.select_related("Usvers").all()
        seeings = Product_views.objects.filter(user_id = request.user).values_list('product', flat=True)
        seeings_count = Product_views.objects.filter(user_id = request.user).count()


        


        #Рекомендации
        it = {}
        for p in range(511):
            instance = Products.objects.values_list('id', f'v{p}')
            object_list2 = Products.objects.values_list('id', f'v{p}').get(id=id)
            shet = Products.objects.all().count()

        
            for i in range(shet-1):
                iter = instance[i]
                if (abs(object_list2[1] - iter[1]) <= 0.011500):
                    #it.append(abs(object_list2 - iter))
                    it[iter[0]] = (abs(object_list2[1] - iter[1]))
        
        if seeings_count < 10:
            a = random.choice(list(it.items()))
            b = random.choice(list(it.items()))
            c = random.choice(list(it.items()))
            d = random.choice(list(it.items()))
            e = random.choice(list(it.items()))

            rec1 = Products.objects.get(id = a[0])
            rec2 = Products.objects.get(id = b[0]) 
            rec3 = Products.objects.get(id = c[0]) 
            rec4 = Products.objects.get(id = d[0]) 
            rec5 = Products.objects.get(id = e[0]) 
        else:
            seeings_arr = seeings[(len(seeings)-10):]
            seeings_arr2 = []
            for i in range(len(seeings_arr)):
                seeings_arr2.insert(i, Products.objects.filter(name = seeings_arr[i]).values_list('id', f'v{p}')[0])

            seeings_arr3 = random.choices(seeings_arr2, k=5)
            

            a = seeings_arr3[0][0]
            b = seeings_arr3[1][0]
            c = seeings_arr3[2][0]  
            d = seeings_arr3[3][0]  
            e = seeings_arr3[4][0]    

            rec1 = Products.objects.get(id = a)
            rec2 = Products.objects.get(id = b) 
            rec3 = Products.objects.get(id = c) 
            rec4 = Products.objects.get(id = d) 
            rec5 = Products.objects.get(id = e)

        context = {
            "object_list":object_list, 
            "object_list2":object_list2, 
            "tel":tel,
            "rec1":rec1,
            "rec2":rec2,
            "rec3":rec3,
            "rec4":rec4,
            "rec5":rec5
        }
       
           
    return render(request,'recomendations.html', context)

def chat_helper(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9, rec10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        shet = Products.objects.all().count()#Счёт вчех продуктов
        query = request.GET.get('q', '')
        print(query)

        def array_dist(arr1,arr2): #Функция прогонки расстояния двух массивов
            if len(arr1)!=len(arr2):
                raise TypeError('Length Difference')
            summ=0.0
            for i in range(len(arr1)):
                summ+= (arr1[i]-arr2[i])*(arr1[i]-arr2[i])
            return math.sqrt(summ)

        if query == "":
            print('Не введён запрос!')
            object_list = ''
        else:
            z = len(query) - 3
            if len(query) < 4:
                query += 'абв'   
            object_list = Products.objects.filter(name__iregex = query[z], is_saled = False)
            query2 = model_st.encode(query)

            #Рекомендации
            it1 = [] #Промежуточный массив для продуктов, с которыми сравниваем
            arr1 = [] #Vассив векторов описания для продуктов, с которыми сравниваем
            id_arr = []
            res = [] #Результат прогонки дистанции
            ids = Products.objects.values_list('id')
            for id in range(shet):
                id_arr.append(ids[id][0])
                for p in range(512):
                    instance = Products.objects.values_list('id', f'v{p}').get(id=id_arr[id])
                    it1.append(instance)
                    arr1.append(it1[p][1]) #Берём значение вектора
                res.append(array_dist(arr1,query2))
                arr1.clear()
                it1.clear()            
    
            #print(arr2)
            mass = dict(zip(id_arr, res)) #Соединяем массив idшников и массив результатов прогонки(чтобы определить товары в рекомендации)
            c = Counter(mass)
            #print(mass)
            #print(c)
            most_common = c.most_common(10) #10 наибольших значений в результате
            print(most_common)
            #print(object_list2)
            rec1 = Products.objects.get(id = most_common[0][0])
            rec2 = Products.objects.get(id = most_common[1][0]) 
            rec3 = Products.objects.get(id = most_common[2][0]) 
            rec4 = Products.objects.get(id = most_common[3][0]) 
            rec5 = Products.objects.get(id = most_common[4][0])
            rec6 = Products.objects.get(id = most_common[5][0])
            rec7 = Products.objects.get(id = most_common[6][0]) 
            rec8 = Products.objects.get(id = most_common[7][0]) 
            rec9 = Products.objects.get(id = most_common[8][0]) 
            rec10 = Products.objects.get(id = most_common[9][0])
             
        
        context = { 
            "object_list":object_list,
            "query":query,
            "rec1":rec1,
            "rec2":rec2,
            "rec3":rec3,
            "rec4":rec4,
            "rec5":rec5,
            "rec6":rec6,
            "rec7":rec7,
            "rec8":rec8,
            "rec9":rec9,
            "rec10":rec10
        }      
           
    return render(request,'test.html', context)

def transact(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        tr = Transacts.objects.all()
        selftr = Transacts.objects.filter(user11 = request.user.username)
        count = Transacts.objects.filter(user11 = request.user.username).count()
        context = {'transactions': tr, 'self_transactions': selftr, 'count':count}
        return render(request, 'transactions.html', context)


def cancel(request, id):
    #try:
    tran = Transacts.objects.get(id=id)
    us = Usvers.objects.all()
    a = tran.user11
    b = tran.user22
    a2 = User.objects.get(username = a)
    b2 = User.objects.get(username = b)
    a1 = Usvers.objects.get(user_id = a2.id)
    b1 = Usvers.objects.get(user_id = b2.id)

    c = tran.colvo1
    b1.balance = b1.balance - c
    a1.balance = a1.balance + c
    a1.save()
    b1.save()
    tran.delete()

    return redirect('transactions')

from django.http import HttpResponseRedirect

from .models import Products
from .forms import addProduct

def index(request):
    want = request.GET.get("want", 'sale')
    query = request.GET.get('search', '')
    z = len(query) - 3
    if query == '':
        if want == 'sale':
            posts = Products.objects.filter(wanttobuy="Продать").order_by('-id')
        elif want == 'buy':
            posts = Products.objects.filter(wanttobuy="Купить").order_by('-id')
    else:
        if want == 'sale':
            posts = Products.objects.filter(wanttobuy="Продать", name__iregex = query[z]).order_by('-id')
        elif want == 'buy':
            posts = Products.objects.filter(wanttobuy="Купить", name__iregex = query[z]).order_by('-id')
    if 'page' in request.GET:
        page = request.GET['page']
    else:
        page = 1
    paginator = Paginator(posts, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {"posts" : posts, "want": want, "page_c": page, 'query': query})


def product_views(request):
    views = Product_views.objects.all()
    count = Product_views.objects.all().count()
    return render(request, 'product_views.html', {'views': views, 'count':count})


def pj(request):
    
    return render(request, 'polojenie.html')


def pt(request):
    
    return render(request, 'partner.html')


def product(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        error = ''
        us = Usvers.objects.get(user=request.user)
        pr = Products.objects.all()
        if request.method == "POST":
            form = addProduct(request.POST, request.FILES)
            if form.is_valid():
                saving = form.save(commit=False)
                saving.user = request.user
                update_product(Products, saving)
                saving.save()
                #if (pr.description != form.cleaned_data["description"]):
                #    print('неккоректно')
                return redirect('ads')
            else:
                error = 'Некорректная форма'
        else:
            form = addProduct()
        context = {'form': form, 'error' : error, "is_NKO":us.is_NKO}
        return render(request, 'products.html', context)


def addcomplaint(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        error = ''
        if request.method == "POST":
            form = addComplaint(request.POST)
            if form.is_valid():
                saving = form.save(commit=False)
                saving.user = request.user
                saving.save()
                return redirect('profile')
            else:
                error = 'Некорректная форма'
        form = addComplaint()
        context = {'form': form, 'error' : error}
        return render(request, 'add_complaint.html', context)


def complaints(request):
    cmpl = Complaints.objects.all()
    count = Complaints.objects.all().count()
    return render(request,'complaints.html',{"cmpl" : cmpl, 'count':count})

def productreg(request):
    error = ''
    us = Usvers.objects.get(user=request.user)
    if request.method == "POST":
        for i in range(0, 3):
            print(i)
            form = addProduct(request.POST, request.FILES)
            if form.is_valid():
                saving = form.save(commit=False)
                saving.user = request.user
                saving.save()
                return redirect('profile')
            else:
                return redirect('productreg')
        return redirect('profile')
    form = addProduct()
    context = {'form': form, 'error' : error, "is_NKO":us.is_NKO}
    return render(request, 'productreg.html', context)

def ads(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        tovars = Products.objects.filter(user=request.user)
        count1 = Products.objects.filter(user=request.user, category="Товар", wanttobuy="Продать").count()
        count2 = Products.objects.filter(user=request.user, category="Услуга", wanttobuy="Продать").count()
        count3 = Products.objects.filter(user=request.user, wanttobuy="Купить").count()
        count4 = Products.objects.filter(user=request.user, category="Соц_задача").count()
        us = Usvers.objects.get(user=request.user)
        return render(request,'ads.html',{"tovars" : tovars, "is_NKO":us.is_NKO, "count1":count1, "count2":count2, "count3":count3, "count4":count4})


def edit(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        prod = Products.objects.get(id=id)

        if request.method == "POST":
            prod.name = request.POST.get("name")
            prod.price = request.POST.get("price")
            prod.description = request.POST.get("description")
            update_product(Products, prod)
            prod.save()
            return redirect('ads')
        else:
            print('Некорректная форма')

        return render(request, "edit.html", {"prod": prod})     


def delete(request, id):
    prod = Products.objects.get(id=id)
    prod.delete()

    return redirect('ads')


def changeS(request, id):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        prod = Products.objects.get(user=request.user, id=id)

        if request.method == "POST":
            prod.price = request.POST.get("price")
            prod.to_who = request.POST.get("to_who")
            prod.is_saled = True
            prod.save()
            return redirect('ads')
        else:
            print('Некорректная форма')

        return render(request, "changeS.html", {"prod": prod})

def search(request):
    if not request.user.is_authenticated:
        return redirect('signup_before')
    else:
        tovars = Products.objects.filter(user=request.user)
        query = request.GET.get('q', '')
        if query == "":
            object_list = ""
        else:
            z = len(query) - 3
            if len(query) < 4:
                query += 'абв'   
            ct = request.GET.get('ct')
            #display_type = request.GET.get("display_type", None)
            display_type = 'other'
            if (display_type == 'other'):
                x = request.GET.get('x')
                y = request.GET.get('y')
                if ((x == '') and (y == '')):
                    x = 0
                    y = 0
                    object_list = Products.objects.filter(name__iregex = query[z], category = ct, is_saled = False)
                else:
                    object_list = Products.objects.filter(name__iregex = query[z], price__range = (x, y), category = ct, is_saled = False)
            else:
                object_list = Products.objects.filter(name = query, category = ct, is_saled = False)

        return render(request, 'search.html',{"tovars" : tovars, 'object_list' : object_list, 'que' : query})

"""
class SearchResultsView(ListView):
    model = Products
    template_name = 'search.html'
    def get_queryset(self): # новый
        query = self.request.GET.get('q', '')
        if query != "":
            z = len(query) - 3
        ct = self.request.GET.get('ct')
        display_type = self.request.GET.get("display_type", None)
        #display_type = 'other'
        if (display_type == 'other'):
            x = self.request.GET.get('x')
            y = self.request.GET.get('y')
            if ((x == '') and (y == '')):
                x = 0
                y = 0
                object_list = Products.objects.filter(name__iregex = query[z], category = ct, is_saled = False)
            else:
                object_list = Products.objects.filter(name__iregex = query[z], price__range = (x, y), category = ct, is_saled = False)
        else:
            object_list = Products.objects.filter(name = query, category = ct, is_saled = False)
        return object_list
"""        

