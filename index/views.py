from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm
from .models import MyJobExperience, MySkills, MyProject


# Create your views here.


def index(request):
    context = {
        'title': 'Головна',
        'user': request.user,
        'h1_header': 'Про мене',
        'p_header_english': 'About Me',
        'h3_description': 'Привіт. Я Захар, і я Junior Python Developer<br>'
                          'Цей сайт створений, як зразок, за допомогою фреймворка Django.<br>'
                          'Мені 18 і я вже маю досвід стажувань в комерційних проектах.<br>'
                          'Вивчаю Python, C/C++, C#, Java.',
        'p_header_english_card': 'Education',
        'h2_header_card': 'Освіта',
        'h3_description_card': 'В цих навчальних закладах я здобував знання',
        'educations': [
            {
                'image_src': 'img/book-half.svg',
                'title': 'Колегіум №16',
                'description': 'Навчався з 1 по 9 класи, з математичним напрямком.'
            },
            {
                'image_src': 'img/laptop-fill.svg',
                'title': 'Хмельницьки обласний ліцей',
                'description': 'Навчався з 10 по 11 класи на Інформаційно-технологічному профілі.'
            },
            {
                'image_src': 'img/pc-display.svg',
                'title': 'Хмельницький Національний Університет',
                'description': 'Курс Комп\'ютерна інженерія'
            }
        ]
    }

    return render(request, 'index/index.html', context)


def auth_page(request):
    context = {
        'title': 'Вхід',
    }

    if request.method == 'POST':
        if request.POST['type'] == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    context['error'] = 'Неправильний логін або пароль'

        elif request.POST['type'] == 'register':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                if not User.objects.filter(username=username).exists():
                    form.save()

                    user = authenticate(username=username, password=password)
                    login(request, user)

                    return redirect('home')
                else:
                    context['error'] = 'Користувач з таким ім\'ям вже існує'

    return render(request, 'index/auth.html', context)


def experience_job(request):
    context = {
        'title': 'Досвід роботи',
        'user': request.user,
        'h1_header': 'Досвід роботи',
        'p_header_english': 'Experience Job',
        'job_experiences': MyJobExperience.objects.all().order_by('-time_start')
    }

    return render(request, 'index/experience_job.html', context)


def detail_job(request, job_id: int):
    job = MyJobExperience.objects.get(id=job_id)

    context = {
        'title': job.title,
        'user': request.user,
        'h1_header': job.title,
        'p_header_english': f'З {job.time_start} по ' + 'Поточно' if job.time_end is None else job.time_end,
        'job': job
    }

    return render(request, 'index/detail_job.html', context)


def skills_page(request):
    context = {
        'title': 'Мої навички',
        'user': request.user,
        'h1_header': 'Мої навички',
        'p_header_english': 'My Skills',
        'skills': MySkills.objects.all().order_by('-rate')
    }

    return render(request, 'index/skills.html', context)


def skill_detail(request, skill_id: int):
    skill = MySkills.objects.get(id=skill_id)

    context = {
        'title': skill.title,
        'user': request.user,
        'h1_header': skill.title,
        'skill': skill
    }

    return render(request, 'index/detail_skill.html', context)


def projects_page(request):
    context = {
        'title': 'Мої проекти',
        'user': request.user,
        'h1_header': 'Мої проекти',
        'p_header_english': 'My projects',
        'projects': MyProject.objects.all().order_by('time_added')
    }

    return render(request, 'index/projects.html', context)


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home')
