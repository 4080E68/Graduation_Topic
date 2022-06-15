from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.forms import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Sum
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from sqlalchemy import true
from myapp.models import *
from .filters import *
import time
import hashlib




def index(request):
    request.session.clear()

    return render(request, 'index.html', locals())

# ======商品列表===========================================================================


def CPU(request):
    cpu_all = cpu.objects.all()
    All_data = All.objects.all()
    cpu_Filter = cpuFilter(queryset=cpu_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        cpu_Filter = cpuFilter(request.POST, queryset=cpu_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'cpu_Filter': cpu_Filter,
        'All_Filter': All_Filter,
    }

    return render(request, 'cpu.html', context)


def HDD(request):
    hdd_all = hdd.objects.all()  # 變數=model的資料表
    All_data = All.objects.all()
    hdd_Filter = hddFilter(queryset=hdd_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        hdd_Filter = hddFilter(request.POST, queryset=hdd_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'hdd_Filter': hdd_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'hdd.html', context)


def SSD(request):
    ssd_all = ssd.objects.all()
    All_data = All.objects.all()
    ssd_Filter = ssdFilter(queryset=ssd_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        ssd_Filter = ssdFilter(request.POST, queryset=ssd_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'ssd_Filter': ssd_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'ssd.html', context)


def Display(request):
    display_all = display.objects.all()
    All_data = All.objects.all()
    display_Filter = displayFilter(queryset=display_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        display_Filter = displayFilter(request.POST, queryset=display_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'display_Filter': display_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'display.html', context)


def Chassis(request):
    chassis_all = chassis.objects.all()
    All_data = All.objects.all()
    chassis_Filter = displayFilter(queryset=chassis_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        chassis_Filter = displayFilter(request.POST, queryset=chassis_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'chassis_Filter': chassis_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'chassis.html', context)

# ===========登入、註冊============================


def Signup(request):
    if request.method == "POST":
        ID = request.POST['ID']
        mail = request.POST['mail']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        name = request.POST['name']
        sex = request.POST['rdo']
        if sex == "man":
            sex = True
        elif sex == "woman":
            sex = False
        if password != password1:
            messages = "請輸入相同密碼"
        else:
            if users.objects.filter(account=ID).exists():
                messages = "帳號已建立!"
            elif not users.objects.filter(account=ID).exists():
                user = users.objects.create(
                    account=ID, username=name, email=mail, password=password, sex=sex)
                user.save()
                messages = "註冊成功"

    return render(request, 'signup.html', locals())


def Login(request):
    if request.method == 'POST':
        ID = request.POST['username']
        userpassword = request.POST['password']
            
        user = users.objects.filter(
            account=ID, password=userpassword).exists()  # 比對帳號密碼
        print(user)
        if user == False:
            messages = "登入失敗請確認帳號或密碼"
            request.session["verify"] = False
        else:
            request.session["verify"] = True
            name = users.objects.filter(account=ID)  # 比對帳號
            for name in name:
                request.session["yourname"] = name.username
                request.session["account"] = name.account
            return redirect('/aftlogin')

    return render(request, 'login.html', locals())


# 登入後====================================================================

def aftlogin(request):
    verify = request.session["verify"]
    print(verify)
    print("debug", verify)
    # ======預設推薦
    likezero = cpu.objects.get(id=9)
    likecpu = cpu.objects.get(id=2)
    likemb = MB.objects.get(id=2)
    likessd = ssd.objects.get(id=3)
    likehdd = hdd.objects.get(id=4)
    likedisplay = display.objects.get(id=5)
    likememory = Memory.objects.get(id=6)
    likepower = Power.objects.get(id=7)
    likechassis = chassis.objects.get(id=8)

    if verify == True:
        yourname = request.session["yourname"]
        account = request.session["account"]

        result = prs.objects.raw(
            "SELECT id,account,type,count(*) as 次數 FROM graduation_topic.myapp_prs where account = %s group by type order by count(*) desc limit 1;", [account])
        #  透過以上SQL獲得使用者最高點擊次數的項目

        print("搜尋筆數為:"+str(len(result)))  # 查詢筆數
        print("最高點擊次數為:"+str(result[0].type))
        print("次數為:"+str(result[0].次數))

        if len(result) == 0:
            recommod = likezero
        elif result[0].type == "Button_cpu":  # 如果是"Button_cpu"推薦預設內容
            recommod = likecpu
        elif result[0].type == "Button_mb":
            recommod = likemb
        elif result[0].type == "Button_ssd":
            recommod = likessd
        elif result[0].type == "Button_hdd":
            recommod = likehdd
        elif result[0].type == "Button_display":
            recommod = likedisplay
        elif result[0].type == "Button_memory":
            recommod = likememory
        elif result[0].type == "Button_power":
            recommod = likepower
        else:
            result[0].type == "Button_chassis"
            recommod = likechassis
    else:
        yourname = "尚未登入"
    return render(request, 'aftlogin.html', locals())


def MB1(request):
    mb_all = MB.objects.all()
    All_data = All.objects.all()
    mb_Filter = displayFilter(queryset=mb_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        mb_Filter = displayFilter(request.POST, queryset=mb_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'mb_Filter': mb_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'MB.html', context)


def Memory1(request):
    memory_all = Memory.objects.all()
    All_data = All.objects.all()
    memory_Filter = displayFilter(queryset=memory_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        memory_Filter = displayFilter(request.POST, queryset=memory_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'memory_Filter': memory_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'Memory.html', context)


def Power1(request):
    power_all = Power.objects.all()
    All_data = All.objects.all()
    power_Filter = displayFilter(queryset=power_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        power_Filter = displayFilter(request.POST, queryset=power_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'power_Filter': power_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'Power.html', context)


def otcpu(request):
    cpu_all = cpu.objects.all()
    All_data = All.objects.all()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_cpu = prs.objects.create(
            account=account, type="Button_cpu", time=localtime)
        save_cpu.save()
    else:
        yourname = "尚未登入"

    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.get(name_all=cart)
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

        save_cartdb.save()  # 儲存資料

    cpu_Filter = cpuFilter(queryset=cpu_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        cpu_Filter = cpuFilter(request.POST, queryset=cpu_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'cpu_Filter': cpu_Filter,
        'All_Filter': All_Filter,
    }

    return render(request, 'otcpu.html', locals())


def otchassis(request):
    chassis_all = chassis.objects.all()
    All_data = All.objects.all()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_chassis = prs.objects.create(
            account=account, type="Button_chassis", time=localtime)
        save_chassis.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.get(name_all=cart)
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

        save_cartdb.save()  # 儲存資料
    chassis_Filter = displayFilter(queryset=chassis_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        chassis_Filter = displayFilter(request.POST, queryset=chassis_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'chassis_Filter': chassis_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otchassis.html', locals())


def otdisplay(request):
    display_all = display.objects.all()
    All_data = All.objects.all()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_display = prs.objects.create(
            account=account, type="Button_display", time=localtime)
        save_display.save()
    else:
        yourname = "尚未登入"

    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.get(name_all=cart)
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

        save_cartdb.save()  # 儲存資料
    display_Filter = displayFilter(queryset=display_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        display_Filter = displayFilter(request.POST, queryset=display_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'display_Filter': display_Filter,
        'All_Filter': All_Filter,
    }

    return render(request, 'otdisplay.html', locals())


def othdd(request):
    hdd_all = hdd.objects.all()  # 變數=model的資料表
    All_data = All.objects.all()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_hdd = prs.objects.create(
            account=account, type="Button_hdd", time=localtime)
        save_hdd.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.get(name_all=cart)
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

        save_cartdb.save()  # 儲存資料
    hdd_Filter = hddFilter(queryset=hdd_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        hdd_Filter = hddFilter(request.POST, queryset=hdd_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'hdd_Filter': hdd_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'othdd.html', context)


def otMB(request):
    mb_all = MB.objects.all()
    All_data = All.objects.all()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_mb = prs.objects.create(
            account=account, type="Button_mb", time=localtime)
        save_mb.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.get(name_all=cart)
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

        save_cartdb.save()  # 儲存資料
    mb_Filter = displayFilter(queryset=mb_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        mb_Filter = displayFilter(request.POST, queryset=mb_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'mb_Filter': mb_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otMB.html', context)


def otPower(request):
    power_all = Power.objects.all()
    All_data = All.objects.all()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_power = prs.objects.create(
            account=account, type="Button_power", time=localtime)
        save_power.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.get(name_all=cart)
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

        save_cartdb.save()  # 儲存資料
    power_Filter = displayFilter(queryset=power_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        power_Filter = displayFilter(request.POST, queryset=power_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'power_Filter': power_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otPower.html', context)


def otssd(request):
    ssd_all = ssd.objects.all()
    All_data = All.objects.all()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_ssd = prs.objects.create(
            account=account, type="Button_ssd", time=localtime)
        save_ssd.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.get(name_all=cart)
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

        save_cartdb.save()  # 儲存資料
    ssd_Filter = ssdFilter(queryset=ssd_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        ssd_Filter = ssdFilter(request.POST, queryset=ssd_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'ssd_Filter': ssd_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otssd.html', context)


def otMemory(request):
    memory_all = Memory.objects.all()
    All_data = All.objects.all()
    cart = request.POST.get('cart_name')
    verify = request.session["verify"]
    print("debud otcpu", verify)
    if verify == True:
        account = request.session["account"]
        localtime = time.ctime()
        save_memory = prs.objects.create(
            account=account, type="Button_memory", time=localtime)
        save_memory.save()
    else:
        yourname = "尚未登入"
    print(cart)
    if cart == 'NO' or None:
        pass
    elif All.objects.filter(name_all=cart).exists():
        cartname = All.objects.get(name_all=cart)
        CARTname = cartname.name_all
        CARTvendor = cartname.vendor
        CARTprice = cartname.price
        CARTcommodity = cartname.commodity
        CARTurl_list = cartname.url_list
        CARTpc_images = cartname.pc_images
        save_cartdb = cartdb.objects.create(
            vendor=CARTvendor, name=CARTname, price=CARTprice,
            commodity=CARTcommodity, url_list=CARTurl_list, pc_images=CARTpc_images,)  # 新增資料

        save_cartdb.save()  # 儲存資料
    memory_Filter = displayFilter(queryset=memory_all)
    All_Filter = ALLFilter(queryset=All_data)
    if request.method == "POST":
        memory_Filter = displayFilter(request.POST, queryset=memory_all)
        All_Filter = ALLFilter(request.POST, queryset=All_data)
    context = {
        'memory_Filter': memory_Filter,
        'All_Filter': All_Filter,
    }
    return render(request, 'otMemory.html', context)


def CART(request):  # 購物清單

    cart_all = cartdb.objects.all()
    total = cartdb.objects.aggregate(Sum('price'))

    if request.method == "POST":
        cart_result = request.POST.get('cart_del')
        defbutton = request.POST.get('button')

        if cart_result == 'NO' or "None":
            pass
        else:
            delcart = cartdb.objects.filter(name=cart_result).first()
            delcart.delete()

        print(defbutton)
        print(cart_result)
        if defbutton == 'Yes':
            delcart_all = cartdb.objects.all()
            delcart_all.delete()
        else:
            pass

    return render(request, "cart.html", locals())
# Create your views here.
