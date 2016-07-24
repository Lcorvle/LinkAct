from django import forms
from .models import MyUser
from .models import Activity
from .models import Interest
from .models import ListField
from datetime import date

INTERESTS_STYLE = (('1', '魔兽'), ('2', '明星'), ('3', '球类运动'), 
    ('4', '游泳'), ('5', '小说'), ('6', '旅行'), ('7', '烹饪'), ('8', '星座'), ('9', '萌宠'),
    ('10', '养生'), ('11', 'coding'), ('12', '电影'),('13', '动漫'), ('14', 'LOL'))

#注册信息
class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length = 20)
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='再次确认密码',widget=forms.PasswordInput())
    nickname = forms.CharField(label='昵称',max_length = 20)
    email = forms.EmailField(label='电子邮箱')
    birthday = forms.DateField(label='生日',initial=date.today)
    city = forms.CharField(label='城市',max_length = 20)
    interest = forms.MultipleChoiceField(label = u'爱好', choices = INTERESTS_STYLE, widget = forms.CheckboxSelectMultiple())

class PersonalInfoForm(forms.Form):
    nickname = forms.CharField(label='昵称',max_length = 20)
    email = forms.EmailField(label='电子邮箱')
    birthday = forms.DateField(label='生日')
    city = forms.CharField(label='城市',max_length = 20)
    interest = forms.CharField(label='爱好',max_length = 50)

class SetPasswordForm(forms.Form):
    origin_password = forms.CharField(label='原始密码',widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='新密码',widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='再次确认新密码',widget=forms.PasswordInput())

#创建活动信息
class ActForm(forms.Form):
    #状态
    status = forms.CharField(max_length = 20)
    #发起人ID
    creator = forms.IntegerField()
    #参与人ID
    participants = ListField(default = [])
    #地点
    locale = forms.CharField(max_length = 20)
    #主题
    theme = forms.CharField(max_length = 20)
    #发起时间
    create_date = forms.DateField(initial = date.today)
    #开始时间
    start_date = forms.DateField(initial = date.today)
    #结束时间
    end_data = forms.DateField(initial = date.today)
    #发起介绍
    introduction = forms.CharField(max_length= 200)
    #点赞人
    supporters = ListField(default = [])
        
#发起评论信息
class CommentForm(forms.Form):
    commenter = forms.IntegerField()
    score = forms.IntegerField()
    content = forms.CharField(max_length = 20)

class LogForm(forms.Form):
    username = forms.CharField(label='用户名',initial='',max_length=20)
    password = forms.CharField(label='密码',initial='',widget=forms.PasswordInput())
