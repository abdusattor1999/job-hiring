from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from accounts.models import Company, Profile
from django.db.models import Count, Q

def home_page(request):
    categories = Category.objects.all()
    companies = Company.objects.all()

    context = {
        'categories':categories,
        'companies':companies,
        'amount':len(companies)
    }
    return render(request, 'home.html',context)



def post_list(request, category_slug=None, company=None):
    if category_slug:
        category = Category.objects.filter(slug=category_slug).last()
        posts = Post.objects.filter(category=category, status=True)

    elif company:
        posts = Post.objects.filter(company_id=company, status=True)
    else:
        posts = Post.objects.filter(status=True)
    
    if len(posts) == 0:
        context = {
            "text": "Mavjud emas !",
            "about" : "Bu kategoriya bo'yicha vakansiyalar mavjud emas. " ,
            "button":"Bosh menuga"
        }
        return render(request, '404.html', context)
    
    return render(request, 'Posts/post_list.html', {'posts':posts})


def post_detail(request, id):
    post = Post.objects.filter(id=id, status=True) 
    if len(post) > 0:
        post = post.last()
    else:
        context = {
            'text' : "Mavjud emas ",
            "about" : "Berilgan Malumotlar bo'yicha vakansiya topilmadi",
            'button' : "Orqaga qaytish"
        }
        return render(request, '404.html', context)
    owner = post.company
    context =  {'post':post, 'owner':owner}

    return render(request, 'Posts/post_detail.html', context)



def search_view(request):
    profiles = Profile.objects.all()
    vacancies = Post.objects.filter(status=True)         
    search = request.GET

    error_context = {
        'text' : "Malumot topilmadi",
        "about" : "Berilgan Kalitso'z bo'yicha xech qanday vakansiya yoki profil topilmadi",
        'button' : "Orqaga qaytish"
    }

    if len(search['title']) == 0:
            return render(request, '404.html', error_context)


    if 'title' in search:
        profiles = profiles.filter(
            Q(first_name__icontains=search['title']) | Q(last_name__icontains=search['title']) |\
            Q(kasbi__icontains=search['title']) | Q(degree__icontains=search['title'])
            ).all()
        profile_bor = len(profiles)


        vacancies = vacancies.filter(
            Q(name__icontains=search['title']) | Q(description__icontains=search['title']) |\
            Q(job_type__icontains=search['title'])).all()
        vacancy_bor = len(vacancies)


        if vacancy_bor==0 and profile_bor == 0:
            return render(request, '404.html', error_context)
        
        context ={
            'users':profiles, 
            'posts':vacancies,
            'profile_bor':profile_bor,
            'vacancy_bor':vacancy_bor
        }
        return render(request, 'Posts/search.html', context)
