from django.db import models
from datetime import datetime
import ast

# Create your models here.
#show what front page need
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"
 
    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)
 
    def to_python(self, value):
        if not value:
            value = []
 
        if isinstance(value, list):
            return value
 
        return ast.literal_eval(value)
 
    def get_prep_value(self, value):
        if value is None:
            return value
 
        return unicode(value) # use str(value) in Python 3
 
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class Front(models.Model):
	a = ''
	
class User(models.Model):
	#用户名
	username = models.CharField(max_length = 20)
	#密码
	password = models.CharField(max_length = 20)
	#ID
	id = models.CharField(max_length = 50)
	#生日
	birthday = models.DateField(default = date.today)
	#好友
	friends = ListField(default = [])
	#主页地址
	website = models.URLField()
	#邮箱
	email = models.EmailField()
	#所在城市
	city = models.CharField(max_length = 20)
	#头像
	head = models.ImageField(upload_to = 'image/')
	#已完成活动：参与&发起
	participate_terminative_acts = ListField(default = [])
	create_ongoing_acts = ListField(default = [])
	#进行中活动：参与&发起
	participate_terminative_acts = ListField(default = [])
	create_ongoing_acts = ListField(default = [])
	#评论过的活动
	commented_acts = ListField(default = [])
	#性别
	gender = models.CharField(max_length = 20)
	#兴趣
	interests = ListField(default = [])

	def __str__(self):
		return self.username
		
class activity(models.Model):
	#状态
	status = models.CharField(max_length = 20)
	#发起人ID
	creator = models.CharField(max_length = 20)
	#参与人ID
	participants = ListField(default = [])
	#地点
	locale = models.CharField(max_length = 20)
	#主题
	theme = models.CharField(max_length = 20)
	#发起时间
	create_date = models.DateField(default = datetime.today)
	#开始时间
	start_date = models.DateField(default = datetime.today)
	#结束时间
	end_data = models.DateField(default = datetime.today)
	#发起介绍
	introduction = models.TextField()
	#点赞人
	supporters = ListField(default = [])

class interest(models.Model):
	id = models.CharField(max_length = 50)
	content = models.CharField(max_length = 20)

