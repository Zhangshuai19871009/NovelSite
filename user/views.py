from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth import get_user_model
from .forms import LoginForm, RegForm, ChangeNicknameForm, ChangePasswordForm
from readStatistics.utils import get_statistics_info


User = get_user_model()

# 登录
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from'), reverse('home'))
    else:
        login_form = LoginForm()
    context = get_statistics_info(request)
    context['login_form'] = login_form
    return render(request, 'user/login.html', context)

# 注册
def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST, request=request)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            # 用户登录
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from'), reverse('home'))
    else:
        reg_form = RegForm()

    context = get_statistics_info(request)
    context['reg_form'] = reg_form
    return render(request, 'user/register.html', context)

# 退出登录
def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))

# 用户信息
def user_info(request):
    context = get_statistics_info(request)
    context['user'] = request.user
    return render(request, 'user/user_info.html', context)

# 修改昵称
def change_nickname(request):
    redirect_to = request.GET.get('from', reverse('home'))

    if request.method == 'POST':
        user = request.user
        form = ChangeNicknameForm(request.POST, user=user)
        if form.is_valid():
            nickname_new = form.cleaned_data['nickname_new']
            user.nickname = nickname_new
            user.save()
            return redirect(redirect_to)
    else:
        form = ChangeNicknameForm()

    context = get_statistics_info(request)
    context['page_title'] = '修改昵称'
    context['form_title'] = '修改昵称'
    context['submit_text'] = '修改'
    context['form'] = form
    context['return_back_url'] = redirect_to
    return render(request, 'form.html', context)

# 修改密码
def change_password(request):
    redirect_to = reverse('home')
    if request.method == 'POST':
        user = request.user
        form = ChangePasswordForm(request.POST, user=user)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            auth.logout(request)
            return redirect(redirect_to)
    else:
        form = ChangePasswordForm()

    context = get_statistics_info(request)
    context['page_title'] = '修改密码'
    context['form_title'] = '修改密码'
    context['submit_text'] = '修改'
    context['form'] = form
    context['return_back_url'] = redirect_to
    return render(request, 'form.html', context)
