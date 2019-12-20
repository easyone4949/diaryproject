from django.shortcuts import render, get_object_or_404, redirect
from .models import Zimon, Mum
from django.utils import timezone
import PIL.Image as pilimg
import numpy as np
# Create your views here.

def main(request):
    star = Zimon.objects.count() + Mum.objects.count()
    return render(request, 'main.html', {'star': star, 'range': range(star)})

def home(request):
    zimon = Zimon.objects
    mum = Mum.objects
    return render(request, 'home.html', {'zimon': zimon, 'mum':mum})

def zimonList(request):
    zimon = Zimon.objects
    return render(request, 'zimonList.html', {'zimon':zimon})

def z_detail(request, zimon_id):
    zimon_detail = get_object_or_404(Zimon, pk = zimon_id)
    return render(request, 'z_detail.html', {'zimon_detail': zimon_detail})

def z_new(request): #글쓰기 화면으로 보내줌
    return render(request, 'z_new.html')

def z_create(request): #글쓰기 버튼 누르면 실행시킴
    zimon = Zimon()
    zimon.title = request.GET['title'] #ziom.title 하면 multiKeyValueError뜸 
    zimon.body = request.GET['content']
    zimon.pub_date = timezone.datetime.now()
    zimon.save()
    return redirect('/couple/zimonList/' + str(zimon.id))

def mumList(request):
    mum = Mum.objects
    return render(request, 'mumList.html', {'mum':mum})

def m_detail(request, mum_id):
    mum_detail = get_object_or_404(Mum, pk = mum_id)
    return render(request, 'm_detail.html', {'mum_detail': mum_detail})

def m_new(request): #글쓰기 화면으로 보내줌
    return render(request, 'm_new.html')

def m_create(request): #글쓰기 버튼 누르면 실행시킴
    mum = Mum()
    mum.title = request.GET['title'] 
    mum.body = request.GET['content']
    mum.pub_date = timezone.datetime.now()
    mum.save()
    return redirect('/couple/mumList/' + str(mum.id))