from django.db import models
from datetime import date
import ast
import json

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

		return str(value)

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
	friends = models.ListField(default = [])
	#主页地址
	website = models.URLField()
	#邮箱
	email = models.EmailField()
	#所在城市
	city = models.CharField(max_length = 20)
	#头像
	head = models.ImageField(upload_to = 'image/')
	#已完成活动：参与&发起
	participate_terminative_acts = models.ListField(default = [])
	create_terminative_acts = models.ListField(default = [])
	#进行中活动：参与&发起
	participate_ongoing_acts = models.ListField(default = [])
	create_ongoing_acts = models.ListField(default = [])
	#评论过的活动
	commented_acts = models.ListField(default = [])
	#性别
	gender = models.CharField(max_length = 20)
	#兴趣
	interests = models.ListField(default = [])

	args = {'friends': friends}

	def get(self, arg):
		if arg == "friends":
			return json.loads(self.friends)
		else if arg == "participate_terminative_acts":
			return json.loads(self.participate_terminative_acts)
		else if arg == "create_terminative_acts":
			return json.loads(self.create_terminative_acts)
		else if arg == "participate_ongoing_acts":
			return json.loads(self.participate_ongoing_acts)
		else if arg == "create_ongoing_acts":
			return json.loads(self.create_ongoing_acts)
		else if arg == "commented_acts":
			return json.loads(self.commented_acts)
		else if arg == "interests":
			return json.loads(self.interests)
		else:
			return None

	def __str__(self):
		return self.username
		
class activity(models.Model):
	#状态
	status = models.CharField(max_length = 20)
	#发起人ID
	creator = models.CharField(max_length = 20)
	#参与人ID
	participants = models.ListField(default = [])
	#地点
	locale = models.CharField(max_length = 20)
	#主题
	theme = models.CharField(max_length = 20)
	#发起时间
	create_date = models.DateField()
	#开始时间
	start_date = models.DateField()
	#结束时间
	end_data = models.DateField()
	#发起介绍
	introduction = models.TextField()
	#点赞人
	supporters = models.ListField(default = [])

	def get(self, arg):
		if arg == "participants":
			return json.loads(self.participants)
		else if arg == "supporters":
			return json.loads(self.supporters)
		else:
			return None

	def __str__(self):
		return self.theme

class interest(models.Model):
	id = models.CharField(max_length = 50)
	content = models.CharField(max_length = 20)

	def __str__(self):
		return self.content
