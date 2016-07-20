from django.db import models
from django.contrib.auth.models import User
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
	
class MyUser(models.Model):
	#与其关联的默认User
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	#昵称
	nickname = models.CharField(max_length = 20)
	#生日
	birthday = models.DateField(default = date.today)
	#好友
	friends = ListField(default = [])
	#主页地址
	website = models.URLField()
	#所在城市
	city = models.CharField(max_length = 20)
	#头像
	head = models.ImageField(upload_to = 'image/')
	#已完成活动：参与&发起
	participate_terminative_acts = ListField(default = [])
	create_terminative_acts = ListField(default = [])
	#进行中活动：参与&发起
	participate_ongoing_acts = ListField(default = [])
	create_ongoing_acts = ListField(default = [])
	#评论过的活动
	commented_acts = ListField(default = [])
	#性别
	gender = models.CharField(max_length = 20)
	#兴趣
	interests = ListField(default = [])

	#get attribute
	def get_username(self):
		return self.user.get_username()
	def get_nickname(self):
		return self.nickname
	def get_id(self):
		return self.user.id
	def get_birthday(self):
		return self.birthday
	def get_friends(self):
		return json.loads(self.friends)
	def get_website(self):
		return self.website
	def get_email(self):
		return self.user.email
	def get_city(self):
		return self.city
	def get_participate_terminative_acts(self):
		return json.loads(self.participate_terminative_acts)
	def get_create_terminative_acts(self):
		return json.loads(self.create_terminative_acts)
	def get_participate_ongoing_acts(self):
		return json.loads(self.participate_ongoing_acts)
	def get_create_ongoing_acts(self):
		return json.loads(self.create_ongoing_acts)
	def get_commented_acts(self):
		return json.loads(self.commented_acts)
	def get_gender(self):
		return self.gender
	def get_interests(self):
		return json.loads(self.interests)


	#set attribute
	def set_username(self, username):
		self.user.username = username
		self.user.save()
		self.save()
	def set_nickname(self, nickname):
		self.nickname = nickname
		self.save()
	def set_birthday(self, birthday):
		self.birthday = birthday
		self.save()
	def set_friends(self, friends):
		self.friends = friends
		self.save()
	def append_friends(self, friend_id):
		f = json.loads(self.friends)
		if(friend_id not in f):
			f.append(friend_id)
			self.friends = f
			self.save()
			return True
		self.friends = f
		self.save()
		return False
	def remove_friends(self, friend_id):
		f = json.loads(self.friends)
		if(friend_id in f):
			f.remove(friend_id)
			self.friends = f
			self.save()
			return True
		self.friends = f
		self.save()
		return False
	def set_website(self, website):
		self.website = website
		self.save()
	def set_email(self, email):
		self.user.email = email
		self.user.save()
		self.save()
	def set_city(self, city):
		self.city = city
		self.save()
	def set_participate_terminative_acts(self, participate_terminative_acts):
		self.participate_terminative_acts = participate_terminative_acts
		self.save()
	def append_participate_terminative_acts(self, act_id):
		pta = json.loads(self.participate_terminative_acts)
		if(act_id not in pta):
			pta.append(act_id)
			self.participate_terminative_acts = pta
			self.save()
			return True
		self.participate_terminative_acts = pta
		self.save()
		return False
	def remove_participate_terminative_acts(self, act_id):
		pta = json.loads(self.participate_terminative_acts)
		if(act_id in pta):
			pta.remove(act_id)
			self.participate_terminative_acts = pta
			self.save()
			return True
		self.participate_terminative_acts = pta
		self.save()
		return False
	def set_create_terminative_acts(self, create_terminative_acts):
		self.create_terminative_acts = create_terminative_acts
		self.save()
	def append_create_terminative_acts(self, act_id):
		cta = json.loads(self.create_terminative_acts)
		if(act_id not in cta):
			cta.append(act_id)
			self.create_terminative_acts = cta
			self.save()
			return True
		self.create_terminative_acts = cta
		self.save()
		return False
	def remove_create_terminative_acts(self, act_id):
		cta = json.loads(self.create_terminative_acts)
		if(act_id in cta):
			cta.remove(act_id)
			self.create_terminative_acts = cta
			self.save()
			return True
		self.create_terminative_acts = cta
		self.save()
		return False
	def set_participate_ongoing_acts(self, participate_ongoing_acts):
		self.participate_ongoing_acts = participate_ongoing_acts
		self.save()
	def append_participate_ongoing_acts(self, act_id):
		poa = json.loads(self.participate_ongoing_acts)
		if(act_id not in poa):
			poa.append(act_id)
			self.participate_ongoing_acts = poa
			self.save()
			return True
		self.participate_ongoing_acts = poa
		self.save()
		return False
	def remove_participate_ongoing_acts(self, act_id):
		poa = json.loads(self.participate_ongoing_acts)
		if(act_id in poa):
			poa.remove(act_id)
			self.participate_ongoing_acts = poa
			self.save()
			return True
		self.participate_ongoing_acts = poa
		self.save()
		return False
	def set_create_ongoing_acts(self, create_ongoing_acts):
		self.create_ongoing_acts = create_ongoing_acts
		self.save()
	def append_create_ongoing_acts(self, act_id):
		coa = json.loads(self.create_ongoing_acts)
		if(act_id not in coa):
			coa.append(act_id)
			self.create_ongoing_acts = coa
			self.save()
			return True
		self.create_ongoing_acts = coa
		self.save()
		return False
	def remove_create_ongoing_acts(self, act_id):
		coa = json.loads(self.create_ongoing_acts)
		if(act_id in coa):
			coa.remove(act_id)
			self.create_ongoing_acts = coa
			self.save()
			return True
		self.create_ongoing_acts = coa
		self.save()
		return False
	def set_commented_acts(self, commented_acts):
		self.commented_acts = commented_acts
		self.save()
	def append_commented_acts(self, act_id):
		ca = json.loads(self.commented_acts)
		if(act_id not in ca):
			ca.append(act_id)
			self.commented_acts = ca
			self.save()
			return True
		self.commented_acts = ca
		self.save()
		return False
	def remove_commented_acts(self, act_id):
		ca = json.loads(self.commented_acts)
		if(act_id in ca):
			ca.remove(act_id)
			self.commented_acts = ca
			self.save()
			return True
		self.commented_acts = ca
		self.save()
		return False
	def set_gender(self, gender):
		self.gender = gender
		self.save()
	def set_interests(self, interests):
		self.interests = interests
		self.save()
	def append_interests(self, interest_id):
		ite = json.loads(self.interests)
		if(interest_id not in ite):
			ite.append(interest_id)
			self.interests = ite
			self.save()
			return True
		self.interests = ite
		self.save()
		return False
	def remove_interests(self, interest_id):
		ite = json.loads(self.interests)
		if(interest_id in ite):
			ite.remove(interest_id)
			self.interests = ite
			self.save()
			return True
		self.interests = ite
		self.save()
		return False
	def set_password(self, raw_password):
		self.user.set_password(raw_password)
		self.user.save()
		self.save()

	#tools
	def check_password(self, raw_password):
		return self.user.check_password(raw_password)
	def email_user(self, subject, message, from_email = None, **kwargs):
		self.user.email_user(subject, message, from_email, kwargs)
	def create_user(self, nickname, username, password):
		flag = True
		temp = User.objects.all()
		for item in temp:
			if item.username == username:
				flag = False
				break
		if flag:
			u = User(username = username, password = password)
			u.save()
			self.user = u
			self.nickname = nickname
			self.save()
			return True
		else:
			return False
	


	def __str__(self):
		return self.nickname
		
class Activity(models.Model):
	#状态
	status = models.CharField(max_length = 20)
	#发起人ID
	creator = models.IntegerField()
	#参与人ID
	participants = ListField(default = [])
	#地点
	locale = models.CharField(max_length = 20)
	#主题
	theme = models.CharField(max_length = 20)
	#发起时间
	create_date = models.DateField(default = date.today)
	#开始时间
	start_date = models.DateField(default = date.today)
	#结束时间
	end_data = models.DateField(default = date.today)
	#发起介绍
	introduction = models.TextField()
	#点赞人
	supporters = ListField(default = [])

	#get attribute
	def get_status(self):
		return self.status
	def get_id(self):
		return self.id
	def get_creator(self):
		return self.creator
	def get_participants(self):
		return json.loads(self.participants)
	def get_locale(self):
		return self.locale
	def get_theme(self):
		return self.theme
	def get_create_date(self):
		return self.create_date
	def get_start_date(self):
		return self.start_date
	def get_end_date(self):
		return self.end_date
	def get_introduction(self):
		return self.introduction
	def get_supporters(self):
		return json.loads(self.supporters)

	#set
	def set_status(self, status):
		self.status = status
		self.save()
	def set_creator(self, creator):
		self.creator = creator
		self.save()
	def set_participants(self, participants):
		self.participants = participants
		self.save()
	def append_participants(self, participant_id):
		p = json.loads(self.participants)
		if(participant_id not in p):
			p.append(participant_id)
			self.participants = p
			self.save()
			return True
		self.participants = p
		self.save()
		return False
	def remove_participants(self, participant_id):
		p = json.loads(self.participants)
		if(participant_id in p):
			p.remove(participant_id)
			self.participants = p
			self.save()
			return True
		self.participants = p
		self.save()
		return False
	def set_locale(self, locale):
		self.locale = locale
		self.save()
	def set_theme(self, theme):
		self.theme = theme
		self.save()
	def update_start_date(self):
		self.start_date = date.today
		self.save()
	def update_end_date(self):
		self.end_date = date.today
		self.save()
	def set_introduction(self, introduction):
		self.introduction = introduction
		self.save()
	def set_supporters(self, supporters):
		self.supporters = supporters
		self.save()
	def append_supporters(self, supporter_id):
		s = json.loads(self.supporters)
		if(supporter_id not in s):
			s.append(supporter_id)
			self.supporters = s
			self.save()
			return True
		self.supporters = s
		self.save()
		return False
	def remove_supporters(self, supporter_id):
		s = json.loads(self.supporters)
		if(supporter_id in s):
			s.remove(supporter_id)
			self.supporters = s
			self.save()
			return True
		self.supporters = s
		self.save()
		return False

	def __str__(self):
		return self.theme

class Interest(models.Model):
	content = models.CharField(max_length = 20)
	#get attribute
	def get_content(self):
		return self.content
	#set
	def set_content(self, content):
		self.content = content
		self.save()
	def __str__(self):
		return self.content

class Comment(models.Model):
	commenter = models.IntegerField()
	score = models.IntegerField()
	content = models.CharField(max_length = 20)
	#get attribute
	def get_content(self):
		return self.content
	def get_id(self):
		return self.id
	def get_commenter(self):
		return self.commenter
	def get_score(self):
		return self.score
	#set
	def set_content(self, content):
		self.content = content
		self.save()
	def set_score(self, score):
		self.score = score
		self.save()
	def set_commenter(self, commenter):
		self.commenter = commenter
		self.save()
	def __str__(self):
		return self.content
