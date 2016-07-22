#搜索部分网址格式http://192.168.55.33:8000/search/?search_class=nickname&search_content=u&search_page=1
#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#
#ERROR_INDEX
#
#0 -----  输入正确
#1 -----  两次输入密码不一致
#2 -----  用户名已存在
#3 -----  信息不完整
#4 -----  密码错误或用户不存在
#-1 ----  未知错误

from .models import MyUser
from .models import Activity
from django.shortcuts import render
from django.contrib import auth
from django.core.mail import send_mail
from .forms import RegisterForm
from .forms import LogForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

base_url = 'http://127.0.0.1:8000'

#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#
#ERROR_INDEX
#
#0 -----  输入正确
#1 -----  两次输入密码不一致
#2 -----  用户名已存在
#3 -----  信息不完整
#4 -----  密码错误
#5 -----  用户不存在
#-1 ----  未知错误
 

#
#搜索部分网址格式http://192.168.55.33:8000/search/?search_class=nickname&search_content=u&search_page=1
#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#
#
#def install(request):
#    '''服务安装'''
#    iplist = IP.objects.all()
#    server_list = AddServer.objects.all()
#	mserver_list = MServer.objects.all()
#    if request.method == "POST":
#        if request.POST.has_key('install'):    #这里判断，如果是name值为install的，则执行此段代码
#           ……代码段省略……
#        else:   #这里判断，如果不是name值为install的，则执行此段代码，因为我们就只有2个name，所以就不用elif request.POST.has_key('server'):了

# Create your views here.
#导航栏
def start_page_show(request):
	user_name = 'test'
	current_user = MyUser()
    # request.user
    # has_login=?
	return render(request, 'LinkAct/start_page.html',
		{})

def linker_page_show(request):
	return render(request, 'LinkAct/linker_page.html', 
		{})

def explore_page_show(request):
	return render(request, 'LinkAct/explore_page.html', 
		{})

def share_page_show(request):
	return render(request, 'LinkAct/share_page.html', 
		{})

def activities_page_show(request):
	return render(request, 'LinkAct/activities_page.html', 
		{})

#用户注册
def user_register(request):
    form = RegisterForm()

    if request.method == "POST":
        params = request.POST
        usernames = params.get('username', '')
        password1 = params.get('password1', '')
        password2 = params.get('password2', '')
        email = params.get('email', '')
        nickname = params.get('nickname', '')
        birthday = params.get('birthday', '')
        city = params.get('city', '')
        
        #一系列合法性判定
	if usernames == None or password1 == None or password2 == None or email == None or nickname == None or birthday == None or city == None:
	    #信息不完整
	    print('incomplete info')
	    return render(request, 'LinkAct/register_result_page.html', {'form':form, 'error_index':3})
	if password1 != password2:
	    print('password1 is not equal to password2')
	    return render(request, 'LinkAct/register_result_page.html', {'form':form, 'error_index':1})
	if len(User.objects.filter(username=usernames)):
	    #用户名已存在
	    print('username already exists')
	    return render(request, 'LinkAct/register_result_page.html', {'form':form, 'error_index':2})
	#判定完毕
	myUser = MyUser()
	myUser.create_user(nickname, usernames, password1)
	return render(request, 'LinkAct/register_result_page.html', {'form':form,'error_index':0})
            
    return render(request, 'LinkAct/register_page.html', {'form':form})
        

#创建完成
def over_create_act(request):
    #在全局绑定函数中判断按下了哪个按钮，此处需知道当前用户名，默认活动form为ActForm
    if request.method == 'POST':
        params = request.POST
        form = ActForm()
        form.status = params.get('status', '')
        form.creator = request.user.id
        form.locale = params.get('locale', '')
        form.theme = params.get('theme', '')
        form.create_date = params.get('create_date', '')
        form.start_date = params.get('start_date', '')
        form.end_date = params.get('end_date', '')
        form.introduction = params.get('introduction', '')
        form.save()
         
        return HttpResponseRedirect('search/?search_class=create_time&search_content=None&search_page=1&search_order=1')
    else:
        form = ActForm()
        return render(request, 'msgboard/createAct.html')

#参加活动，传入活动id，如何根据request获取当前用户id，此处还未判断是否人满
def enter_act(request):
    if request.method == 'GET':
        i = request.GET['id']
        to_enter_act = Activity.objects.get(id=i)
        to_enter_act.append_participants(request.user.id)
        request.user.myuser.append_participate_ongoing_acts(to_enter_act.id)

        return render(requset, '同上', {'无参数'})

#退出活动
def exit_act(request):
    if request.method == 'GET':
        i = request.GET['id']
        to_exit_act = Activity.objects.get(id=i)
        to_exit_act.remove_participants(request.user.id)
        request.user.myuser.remove_participate_ongoing_acts(to_enter_act.id)

        #从用户正参加列表中删除
        return render(requset, '同上', {'无参数'})

#查看活动信息——id写在网址上，通过链接获得，<a href="">
def check_act_msg(request):
    if request.method == 'GET':
        is_in_act = False
        i = request.GET['id']
        to_check_act = Activity.objects.get(id=i)

        if request.user.id in to_check_act.get_participants:
            is_in_act = True
        
        form = ActForm()
        form.status = to_check_act.get_status()
        form.creator = to_check_act.get_creator()
        form.locale = to_check_act.get_locale()
        form.theme = to_check_act.get_theme()
        form.create_date = to_check_act.get_create_date()
        form.start_date = to_check_act.get_start_date()
        form.end_date = to_check_act.get_end_date()
        form.introduction = to_check_act.get_introduction()
        
        return render(request, 'msgboard/actShow.html', {'form': form, 'is_in_act':is_in_act})
    else:
        params = request.POST
        i = request.GET['id']
        to_check_act = Activity.objects.get(id=i)
        to_check_act.set_status(params.get('status', ''))
        to_check_act.set_creator(params.get('creator', ''))
        to_check_act.set_locale(params.get('locale', ''))
        to_check_act.set_theme(params.get('theme', ''))
        to_check_act.update_start_date(params.get('start_date', ''))
        to_check_act.update_end_date(params.get('end_date', ''))
        to_check_act.set_introduction(params.get('introduction', ''))

        return  #跳转页面

#登录
def log_in(request):
    if request.method == "POST":
        #根据用户名找到对应用户信息及信息网页
        log_username = request.POST['username']
        log_password = request.POST['password']
        user = auth.authenticate(username=log_username, password=log_password)
        
        if user is not None:        
            auth.login(request, user)
            return render(request, 'msgboard/success.html', {'username':request.user.username})         
        else:
            return render(request, 'msgboard/login_page.html', {'form':form, 'error_index':4})
    form = LogForm()
    return render(request, 'msgboard/login_page.html', {'form':form})
    
#登出
def log_out(request):
    auth.logout(request)
    return render(request, '', {})

#查看个人信息--可以通过使用request.user.myuser.nickname获取附加信息
def check_personal_msg(request):
    if request.method == 'POST':
        params = request.POST
        obj = User.objects.get(username=request.user.username)
        #obj.myuser.set_email(params.get('email', ''))
        obj.myuser.set_nickname(params.get('nickname', ''))
        #obj.myuser.set_birthday(params.get('birthday', ''))
        #obj.myuser.set_city(params.get('city', ''))
        
        return render(request, 'msgboard/success.html', {'username':request.user.username})
    else:        
        form = RegisterForm()
        form.username = request.user.username
        form.password = request.user.password
        #form.email = request.user.email
        form.nickname = request.user.myuser.nickname
        return render(request, 'msgboard/register.html', {'form':form, 'personal_msg':personal_msg})

#评价活动——需要评价Form，先定义为CommentForm

#完成评价
def evaluate_act(request):
    if request.method == 'POST':
        params = request.POST
        newComment = Comment()
        newComment.commenter = request.user.id
        newComment.score = params['score']
        newComment.content = params['content']
        newComment.save()

        itemID = request.POST['itemID']
        #活动评论列表append这条新评论
        
        return #跳转评论成功
    elif request.method == 'GET':
        params = request.GET
        itemID = params['id']
        return render(request, '任务信息界面', {'itemID':itemID})
        
        
def search_people(request):
    if request.method == 'GET':                                  
        search_class = request.GET['search_class']
        search_content = request.GET['search_content']                                  
        search_page = request.GET['search_page']
        search_order = request.GET['search_order']
        
        if search_order == '1':
            answer = MyUser.objects.order()
        
        elif search_class == 'nickname':
            answer = MyUser.objects.filter(nickname=search_content)

        startPos = (int(search_page) - 1) * 10
        endPos = int(search_page) * 10
        result = answer[startPos:endPos]
        return render(request, 'msgboard/explore_page.html', {'answer':answer})    


                                
#查找活动   //搜索页面不同于主页面 默认每页10条
def search_act(request):
    if request.method == 'GET':
        search_class = request.GET['search_class']
        search_content = request.GET['search_content'] 
        search_page = request.GET['search_page']

        #不同检索方式
        if search_class == 'theme':
            answer = Activity.objects.all()[0].activity_theme_filter(Activity.objects.all(), [search_class])

        startPos = (int(search_page) - 1) * 10
        endPos = int(search_page) * 10
        result = answer[startPos:endPos]

        return render(request, 'msgboard/explore_page.html', {'result':result})

#添加好友
def request_for_friend(request):
    return render(request, '??弹窗或新页面', {})

def send_emails(email_from, email_to, title, content):
    send_mail('wf', 'wf', "Louyk14@163.com", "Louyk14@163.com", fail_silently=False)

def user_manage(request):
    if request.method == 'POST':
        if request.POST.get('submit') == "register":
            return HttpResponseRedirect('register/')
        elif request.POST.get('submit') == "login":
            return HttpResponseRedirect('login/')
        elif request.POST.get('submit') == 'check':
            return HttpResponseRedirect('check/')
        else:
            form = LogForm()
            return render(request, 'msgboard/login.html', {'form':form})
    
    return render(request, 'msgboard/user_manage.html', {})

def act_show_page(request):
    if request.method == 'GET':
        page_num = request.GET['page_num']
        #按create_date排序    acts = sorted()

        startPos = (int(page_num) - 1) * 10
        endPos = int(page_num) * 10
        answer = acts[startPos:endPos]
        
        return render(request, 'msgboard/show.html', {'answer':answer})


# Create your views here.
