from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from .utils import sendSimpleEmail
from posts.models import Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def profile_list(request):
    users = Profile.objects.all()
    return render(request, 'accounts/profile_list.html', {'users':users})


def add_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile_list')
        
    else:
        form = ProfileEditForm()
        return render(request, 'accounts/profile_create.html', {"form" : form})


def user_details(request):
    user = request.user
    context = {
        'user':user,
    }
    return render(request, 'accounts/profile_details.html', context)


def company_detail(request, id):
    company = Company.objects.filter(id=id).last()
    vacancies = Post.objects.filter(company=company)
    v_quantity = len(vacancies)
    context = {'company':company, 'vacancies':vacancies, "v_quantity":v_quantity}
    return render(request, 'Company/company_details.html', context)


def arizani_yuborish(reuqest, company=None):
    if reuqest.method == 'POST':
        title = "Yangi ariza !"
        name = reuqest.POST.get('name')
        message = reuqest.POST.get('message')
        contact = reuqest.POST.get('contact')
        company = reuqest.POST.get("company")
        sent = False
        if company:
            comp = Company.objects.get(id=company)
            reciever = comp.email
            sent = sendSimpleEmail(title, name, message, contact, reciever)
        else:
            context = {
            'text' : 'Kompaniya kiritilmadi',
            'about' : "Yuborishda xatolik ! Kompaniya aniq kiritilmadi !",
            'button' : 'Bosh menuga'
            }
            return render(reuqest, '404.html', context)       
        if sent:
            return redirect('posts:home_page')
        else:
            context = {
            'text' : 'Xabar yuborilmadi',
            'about' : "Yuborishda xatolik ! Iltimos qayta urinib ko'ring",
            'button' : 'Bosh menuga'
            }
            return render(reuqest, '404.html', context)
    else:
        form = ArizaForm()
        context = {"company" : company, 'form':form}
        return render(reuqest, 'Company/ariza.html', context)
    

def register(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return redirect('accounts:login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/account_create.html',{'user_form':user_form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('posts:home_page')
            else:
                context = {
                'text' : 'Malumot topilmadi !',
                'about' : "Berilgan malumotlar bo'yicha Foydalanuvchi profili topilmadi \"Username\" yoki \"Parol\" xato bo'lishi mumkin tekshirib qaytadan kiriting !",
                'button' : 'Bosh menuga qaytish'
                }
                return render(request, '404.html', context)
            
        else:
            context = {
                'text' : 'Malumot topilmadi !',
                'about' : "Berilgan malumotlar bo'yicha Foydalanuvchi profili topilmadi \"Username\" yoki \"Parol\" xato bo'lishi mumkin tekshirib qaytadan kiriting !",
                'button' : 'Bosh menuga qaytish'
                }
            return render(request, '404.html', context)
            
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})


@login_required
def edit(request, id):
    profile = Profile.objects.filter(id=id).last()
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('posts:home_page')
    else:
        iden = id
        profile_form = ProfileEditForm(instance=profile)
        context = {
            'iden':iden,
            'profile_form':profile_form
        }
    return render(request, 'accounts/profile_edit.html', context)


@login_required
def user_edit(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserEditForm(instance=user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('posts:home_page')
    else:
        user_form = UserEditForm(instance=user)
    return render(request, 'accounts/user_edit.html', locals())





@login_required
def confirm_delete(request):
    return render(request, "accounts/confirm_to_delete.html")

@login_required
def user_delete(request):
    user = request.user
    user.delete()
    return redirect("posts:home_page")


def company_create(request):
    user = request.user
    if request.method == 'POST':
        form = CompanyForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_details')
        else:
            conn = {
                'text' : "Malumotlar to'g'ri kiritlmadi",
                'about' : "Kompaniya malumotlari talabga javob bermaydi tekshirib qaytadan kiriting !",
                'button' : 'Bosh menuga qaytish'
                }
            return render(request, '404.html', conn)
    else:
        form = CompanyForm(instance=user)
        return render(request, "company_create.html", {'form':form})




