#搜索部分网址格式http://192.168.55.33:8000/search/?search_class=nickname&search_content=u&search_page=1
#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#


from .models import MyUser
from .models import Activity
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from django.core.mail import send_mail
from .forms import RegisterForm
from .forms import LogForm
from .forms import PersonalInfoForm
from .forms import SetPasswordForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from LinkAct.models import Img, Interest
import string
from datetime import date
from .forms import ActForm
from django.utils import timezone

base_url = 'http://127.0.0.1:8000'



#   search_class表示搜索类别，search_content表示搜索内容,search_content表示搜索的页码号，要在template中动态生成
#
#ERROR_INDEX
#
#用户注册
#0 -----  输入正确
#1 -----  两次输入密码不一致
#2 -----  用户名已存在
#3 -----  信息不完整
#4 -----  密码错误
#5 -----  用户不存在

#修改密码
#6 -----  修改密码成功
#7 -----  两次输入密码不一致
#8 -----  原密码错误

#修改个人信息
#9 -----  修改信息成功

#用户登录
#10 ----- 用户登录成功
#11 ----- 不存在该用户
#12 ----- 用户密码不匹配

#-1 ----  未知错误

# user attr #
# user basic attr:
# username
# password
# email

# extension:MyUser
# nickname
# birthday
# friends
# city
# head
# participate_terminative_acts
# create_terminative_acts
# participate_ongoing_acts
# create_ongoing_acts
# commented_acts
# gender
# interests



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
#页面按钮绑定
# def user_manage(request):
#     if request.method == 'POST':
#         if request.POST.get('submit') == "register":
#             return HttpResponseRedirect('register/')
#         elif request.POST.get('submit') == "login":
#             return HttpResponseRedirect('login/')
#         elif request.POST.get('submit') == 'check':
#             return HttpResponseRedirect('check/')
#         else:
#             form = LogForm()
#             return render(request, 'msgboard/login.html', {'form':form})
	
#     return render(request, 'msgboard/user_manage.html', {})
def start_page_show(request):
	#-----------登录判定----------#
	has_login = False
	
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/start_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#


	

def linker_page_show(request):
	#-----------登录判定----------#
	has_login = False

	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/linker_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#

	

def explore_page_show(request):
	#-----------登录判定----------#
	has_login = False
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/explore_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#

	

def share_page_show(request):
	#-----------登录判定----------#
	has_login = False
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/share_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#

	

def activities_page_show(request):
	#-----------登录判定----------#
	has_login = False
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	if request.user.username == AnonymousUser.username:
		has_login = False
		return render(request, 'LinkAct/activities_page.html',
		{'user_name':user.username, 'has_login':has_login})
	else:
		has_login = True
		imgs = Img.objects.filter(id = user.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})
	#-----------登录判定----------#

	

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
		interests = params.getlist('interest', '')
		#一系列合法性判定
		
		if usernames == None or password1 == None or password2 == None or email == None or nickname == None or birthday == None or city == None:
			#信息不完整
			print('incomplete info')
			return render(request, 'LinkAct/result_page.html', {'error_index':3})
		if password1 != password2:
			print('password1 is not equal to password2')
			return render(request, 'LinkAct/result_page.html', {'error_index':1})
		if len(User.objects.filter(username=usernames)):
			#用户名已存在
			print('username already exists')
			return render(request, 'LinkAct/result_page.html', {'error_index':2})
		#判定完毕
		myUser = MyUser()
		myUser.create_user(usernames, password1, email)
		user = auth.authenticate(username=usernames, password=password1)
		auth.login(request,user)
		return render(request, 'LinkAct/result_page.html', {'error_index':0})
 
	return render(request, 'LinkAct/register_page.html', {'form':form})
		


#创建完成
#创建完成
def create_act(request):
    #在全局绑定函数中判断按下了哪个按钮，此处需知道当前用户名，默认活动form为ActForm
    if request.method == 'POST':
        params = request.POST
        new_act = Activity()
        new_act.status = '0'
        new_act.creator = request.user.id
        new_act.locale = params.get('locale', '')
        new_act.theme = params.getlist('theme', '')
        new_act.create_date = timezone.now()
        new_act.start_date = params.get('start_date', '')
        new_act.end_date = params.get('end_date', '')
        new_act.introduction = params.get('introduction', '')
        new_act.save()
         
        return HttpResponseRedirect('../search/?search_class=create_time&search_content=None&search_order=1&search_page=1')
    else:
        form = ActForm()
        return render(request, 'msgboard/createAct.html', {form, 'form'})

#参加活动，传入活动id，如何根据request获取当前用户id，此处还未判断是否人满
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

#修改活动信息，仅活动创建人能进入此页面，修改完成后用input按钮提交，用hidden的input标签传回id及last_page
def check_act_msg(request):
    if request.method == 'GET':
        i = request.GET['id']
        last_page = request.GET['last_page']
        to_check_act = Activity.objects.get(id=i)
        
        form = ActForm()
        
        return render(request, 'msgboard/actShow.html', {'form': form, 'act_obj':to_check_act, 'last_page':last_page, 'id':i})
    else:
        params = request.POST
        i = request.POST['id']
        last_page = request.POST['last_page']
        to_check_act = Activity.objects.get(id=i)
        to_check_act.set_locale(params.get('locale', ''))
        to_check_act.set_theme(params.get('theme', ''))
        to_check_act.update_start_date(params.get('start_date', ''))
        to_check_act.update_end_date(params.get('end_date', ''))
        to_check_act.set_introduction(params.get('introduction', ''))

        return HttpResponseRedirect(last_page)

#登录
def log_in(request):

	if request.method == "POST":
		#根据用户名找到对应用户信息及信息网页
		log_username = request.POST['username']

		log_password = request.POST['password']

		user = auth.authenticate(username=log_username, password=log_password)
		
		if len(User.objects.filter(username=log_username)) == 0:
			return render(request, 'LinkAct/result_page.html', {'error_index':11})
 
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('../')
 
		else:
			return render(request, 'LinkAct/result_page.html', {'error_index':12})
 
		
	form = LogForm()
	return render(request, 'LinkAct/login_page.html', {'form':form})

#登出
def log_out(request):
	auth.logout(request)

#查看个人信息--可以通过使用request.user.myuser.nickname获取附加信息
def check_personal_msg(request):
	#-----------登录判定----------#
	has_login = True
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')
	#-----------登录判定----------#


	if request.method == 'POST':
		params = request.POST
		obj = User.objects.get(username=request.user.username)
		obj.myuser.set_email(params.get('email', ''))
		obj.myuser.set_nickname(params.get('nickname', ''))
		#obj.myuser.set_birthday(params.get('birthday', ''))
		obj.myuser.set_city(params.get('city', ''))

		imgs = Img.objects.filter(id = obj.myuser.get_head())
		if len(imgs) != 0:
			img = imgs[0]
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'img': img, 'has_own_avatar':True})
		else:
			return render(request, 'LinkAct/linker_page.html',
			{'user_name':user.username, 'has_login':has_login, 'has_own_avatar':False})

	#default render#
	else :       
		imgs = Img.objects.filter(id = request.user.myuser.get_head())
		has_own_avatar = False
		if len(imgs) != 0:
			img = imgs[0]
			has_own_avatar = True
		form = PersonalInfoForm()
		form.email = request.user.email
		form.nickname = request.user.myuser.nickname
		#form.birthday = request.user.myuser.birthday
		form.city = request.user.myuser.city
		print("here")
		temp = request.user.myuser.get_interests()
		print(type(temp))
		print(temp)
		interest_msg = ""
		for s in temp:
			if len(interest_msg) != 0:
				interest_msg += '，'
			interest_msg += Interest.objects.get(id = int(s)).get_content()
		if interest_msg == "":
			interest_msg = "未填写"
			

		print(interest_msg)
		# print(form)
		# print(form.nickname)
		# #print(form.birthday)
		# print(form.city)
		# print(form.email)
		if has_own_avatar:
			return render(request, 'LinkAct/user_info.html', {'form':form, 'has_login':True, 
			'user_name':request.user.username, 'personal_msg':request.user, 'interest_msg':interest_msg, 'img': img, 'has_own_avatar':has_own_avatar})
		else:
			return render(request, 'LinkAct/user_info.html', {'form':form, 'has_login':True, 
			'user_name':request.user.username, 'personal_msg':request.user, 'interest_msg':interest_msg, 'has_own_avatar':has_own_avatar})

def set_password_func(request):

	#-----------登录判定----------#
	has_login = True
	user = request.user
	if request.method == 'GET':
		login_status = request.GET.get('user_login','-1')
		if login_status=='0':
			log_out(request)
			print('logout successfully')

	#-----------------------------#
	imgs = Img.objects.filter(id = user.myuser.get_head())
	if len(imgs) != 0:
		img = imgs[0]
		has_own_avatar = True
	else:
		has_own_avatar = False
	#-----------------------------#

	#应该修改这里#
	if request.user.username == AnonymousUser.username:
		has_login = False
	else:
		has_login = True
	#-----------登录判定----------#

	form = SetPasswordForm()

	if request.method == 'POST':
		params = request.POST
		obj = User.objects.get(username=request.user.username)
		origin_password = params.get('origin_password','')
		new_password1 = params.get('new_password1','')
		new_password2 = params.get('new_password2','')
		if auth.authenticate(username=request.user.username, password=origin_password) == None:
			return render(request, 'LinkAct/result_page.html',{'error_index':8, 'img': img})
		if new_password1 != new_password2:
			return render(request, 'LinkAct/result_page.html',{'error_index':7, 'img': img})

		obj.myuser.set_password(new_password1)
		log_out(request)
		return render(request, 'LinkAct/result_page.html', {'error_index':6, 'has_login':False, 'img': img})
	else:        
		return render(request, 'LinkAct/user_password.html', {'form':form, 'has_login':True, 
			'user_name':request.user.username, 'img': img})

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
		
def show_people(request):
    if request.method == 'GET':
        index = int(request.GET['id'])
        current_page = request.GET['last_page']
        obj = MyUser.objects.filter(id=index)

        new_obj = []
        for index in range(0, len(obj)):
            if obj[index].user.username != request.user.username:
                new_obj.append(obj)

        return render(request, 'LinkAct/showPeople.html', {'form':form, 'obj':new_obj, 'last_page':current_page})

def search_people(request):
    if request.method == 'GET':                                  
        search_class = request.GET['search_class']
        search_content = request.GET['search_content']                                  
        search_page = request.GET['search_page']
        search_order = request.GET['search_order']
        
        if search_order == '1':
            answer = MyUser.objects.all().order_by('id')
        
        elif search_class == 'nickname':
            answer = MyUser.objects.filter(nickname=search_content)

        
        startPos = (int(search_page) - 1) * 10
        endPos = int(search_page) * 10
        if endPos >= len(answer):
            endPos = len(answer)

        result = answer[startPos:endPos]

        temp_url = request.get_full_path()

        next_page = int(search_page) + 1
        
        next_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=" + str(next_page)
        
        return render(request, 'msgboard/show_people.html', {'result':result, 'current_page':int(search_page), 'current_url':request.get_full_path(), 'next_page_url':next_page_url})    

	
#查找活动   //搜索页面不同于主页面 默认每页10条，所有展示活动的界面都绑定此函数
                #urls.py r'^searchActs/'    绝对路径为127.0.0.0.1/searchActs/      因而展示界面上的各详情链接为  <a href='../showActs/?id='+ {{ result[index].id }} + '&last_page=' + {{ current_url }}>
                #“下一页”按钮链接应为<a href={{ next_page_url }}>
def search_act(request):
    if request.method == 'GET':
        #搜索类别
        search_class = request.GET['search_class']
        #搜索内容
        search_content = request.GET['search_content'] 
        #搜索页码
        search_page = request.GET['search_page']
        #排序方法，为1时表示按照类别倒序排序，不搜索只排序
        search_order = request.GET['search_order']

        if search_order == '1':
            answer = Activity.objects.all().order_by(search_class)

        #不同检索方式
        elif search_class == 'theme':
            answer = Activity.objects.all()[0].activity_theme_filter(Activity.objects.all(), [search_class])

        elif search_class == '':
            return
        
        startPos = (int(search_page) - 1) * 10
        endPos = int(search_page) * 10
        if endPos >= len(answer):
            endPos = len(answer)
        
        result = answer[startPos:endPos]

        next_page = int(search_page) + 1

        temp_url = request.get_full_path()
        next_page_url = request.path + "?search_class=" + search_class + "&search_content=" + search_content + "&search_order=" + search_order + "&search_page=" + (int(search_page) + 1)

        return render(request, 'msgboard/searchActs.html', {'result':result, 'current_page':int(search_page), 'current_url':request.get_full_path(), 'next_page_url':next_page_url})


#展示具体活动的界面，返回按钮的链接应为<a href={{ last_page }}>， 若是创建者，则应存在链接“修改活动信息”，应为<a href=this_page_no_para + 'change/?id=' + act_obj.id + '&last_page=' + this_page>
def show_act(request):
    if request.method == 'GET':
        index = int(request.GET['id'])
        current_page = request.GET['last_page']
        act_obj = Activity.objects.filter(id=index)

        this_page = request.get_full_path()
        this_page_no_para = request.path

        actForm = ActForm()

        #是否活动发起人，决定了是否能修改活动信息
        isCreator = False
        if request.user.id == act_obj.creator:
            isCreator = True

        return render(request, 'LinkAct/showAct.html', {'form':actForm, 'act_obj':act_obj, 'last_page':current_page, 'this_page':this_page, 'this_page_no_para':this_page_no_para, 'isCreator':isCreator})

#添加好友
def request_for_friend(request):
	return render(request, '??弹窗或新页面', {})

def send_emails(email_from, email_to, title, content):
	send_mail('wf', 'wf', "Louyk14@163.com", "Louyk14@163.com", fail_silently=False)


# Create your views here.
def upload_img(request):
	if request.method == 'POST':
		new_img = Img(img = request.FILES.get('img'))
		new_img.save()
		request.user.myuser.set_head(new_img.get_id())
	return render(request, 'LinkAct/uploadimg.html')
