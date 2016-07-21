from django.db import models
from django.contrib.auth.models import User
from datetime import date
import ast
import json
import types
import string

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
	head = models.ImageField(upload_to = 'image/', default = 'image/no_img.jpg')
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
		if isinstance(self.friends, str):
			return json.loads(self.friends)
		return self.friends
	def get_website(self):
		return self.website
	def get_email(self):
		return self.user.email
	def get_city(self):
		return self.city
	def get_participate_terminative_acts(self):
		if isinstance(self.participate_terminative_acts, str):
			return json.loads(self.participate_terminative_acts)
		return self.participate_terminative_acts
	def get_create_terminative_acts(self):
		if isinstance(self.create_terminative_acts, str):
			return json.loads(self.create_terminative_acts)
		return self.create_terminative_acts
	def get_participate_ongoing_acts(self):
		if isinstance(self.participate_ongoing_acts, str):
			return json.loads(self.participate_ongoing_acts)
		return self.participate_ongoing_acts
	def get_create_ongoing_acts(self):
		if isinstance(self.create_ongoing_acts, str):
			return json.loads(self.create_ongoing_acts)
		return self.create_ongoing_acts
	def get_commented_acts(self):
		if isinstance(self.commented_acts, str):
			return json.loads(self.commented_acts)
		return self.commented_acts
	def get_gender(self):
		return self.gender
	def get_interests(self):
		if isinstance(self.interests, str):
			return json.loads(self.interests)
		return self.interests


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
		f = self.get_friends()
		if friend_id not in f:
			f.append(friend_id)
			self.friends = f
			self.save()
			return True
		self.friends = f
		self.save()
		return False
	def remove_friends(self, friend_id):
		f = self.get_friends()
		if friend_id in f:
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
		pta = self.get_participate_terminative_acts()
		if act_id not in pta:
			pta.append(act_id)
			self.participate_terminative_acts = pta
			self.save()
			return True
		self.participate_terminative_acts = pta
		self.save()
		return False
	def remove_participate_terminative_acts(self, act_id):
		pta = self.get_participate_terminative_acts()
		if act_id in pta:
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
		cta = self.get_create_terminative_acts()
		if act_id not in cta:
			cta.append(act_id)
			self.create_terminative_acts = cta
			self.save()
			return True
		self.create_terminative_acts = cta
		self.save()
		return False
	def remove_create_terminative_acts(self, act_id):
		cta = self.get_create_terminative_acts()
		if act_id in cta:
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
		poa = self.get_participate_ongoing_acts()
		if act_id not in poa:
			poa.append(act_id)
			self.participate_ongoing_acts = poa
			self.save()
			return True
		self.participate_ongoing_acts = poa
		self.save()
		return False
	def remove_participate_ongoing_acts(self, act_id):
		poa = self.get_participate_ongoing_acts()
		if act_id in poa:
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
		coa = self.get_create_ongoing_acts()
		if act_id not in coa:
			coa.append(act_id)
			self.create_ongoing_acts = coa
			self.save()
			return True
		self.create_ongoing_acts = coa
		self.save()
		return False
	def remove_create_ongoing_acts(self, act_id):
		coa = self.get_create_ongoing_acts()
		if act_id in coa:
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
		ca = self.get_commented_acts()
		if act_id not in ca:
			ca.append(act_id)
			self.commented_acts = ca
			self.save()
			return True
		self.commented_acts = ca
		self.save()
		return False
	def remove_commented_acts(self, act_id):
		ca = self.get_commented_acts()
		if act_id in ca:
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
		ite = self.get_interests()
		if interest_id not in ite:
			ite.append(interest_id)
			self.interests = ite
			self.save()
			return True
		self.interests = ite
		self.save()
		return False
	def remove_interests(self, interest_id):
		ite = self.get_interests()
		if interest_id in ite :
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
	def set_gender(self, gender):
		if gender == '男' or gender == '女':
			self.gender = gender
			self.save()
			return True
		return False

	#tools
	def check_password(self, raw_password):
		return self.user.check_password(raw_password)
	def email_user(self, subject, message, from_email = None, **kwargs):
		self.user.email_user(subject, message, from_email, kwargs)

	def create_user(self, nickname, usernames, passwords):
                flag = True
                temp = User.objects.all()
                for item in temp:
                        if item.username == usernames:
                                flag = False
                                break
                if flag:
                        u = User.objects.create_user(username=usernames,password=passwords)
                        self.user = u
                        self.nickname = nickname
                        u.save()
                        self.save()
                        return True
                else:
                        return False
	def delete_user(self):
		a = self.user
		a.delete()
		self.delete()
	def create_activity(self, theme):
		if not isinstance(theme, list):
			return false
		a = Activity(theme = theme, creator = self.id)
		a.save()
		flag =  self.append_create_ongoing_acts(a.id)
		return flag
	def get_activities(self, kinds, order_base):
		acts = Activity.objects.order_by(order_base)
		if not isinstance(kinds, str):
			return []
		results = []
		if kinds == 'participate_terminative_acts':
			pta = self.get_participate_terminative_acts()
			results = [var for var in acts if var.id in pta]
		elif kinds == 'create_terminative_acts':
			cta = self.get_create_terminative_acts()
			results = [var for var in acts if var.id in cta]
		elif kinds == 'participate_ongoing_acts':
			poa = self.get_participate_ongoing_acts()
			results = [var for var in acts if var.id in poa]
		elif kinds == 'create_ongoing_acts':
			coa = self.get_create_ongoing_acts()
			results = [var for var in acts if var.id in coa]
		return results
	
	#data是一个act数组，在该数组中查找同时符合reference中theme的act，满足的项数越多越靠前
	def activity_theme_filter(self, data, reference):
		if not isinstance(reference, list):
			return []
		results = {}
		for item in data:
			temp = [var for var in item.get_theme() if var in reference]
			results[item] = temp
		return sorted(results.items(), key = lambda asd:asd[1], reverse = True)

	#data是一个MyUser数组，在该数组中进行查找，同时符合reference中的各种属性的MyUser,
	#reference中的属性不固定，例如：{'city':'重庆'}和{'city':'重庆', 'nickname': '偷心的鱼'}皆可,
	#属性可选范围是MyUser和User的所有属性
	def user_filter(self, data, reference):
		results = []
		for item in data:
			results.append(item)
		if 'username' in reference:
			i = 0
			while(i < len(results)):
				if results[i].get_username() != reference['username']:
					del results[i]
				else:
					i += 1
		if 'id' in reference:
			i = 0
			while(i < len(results)):
				if results[i].get_id() != reference['id']:
					del results[i]
				else:
					i += 1
		#birthday的值的类型是string，格式是'2016-07-21'
		if 'birthday' in reference:
			i = 0
			while(i < len(results)):
				if str(results[i].get_birthday()) != reference['birthday']:
					del results[i]
				else:
					i += 1
		if 'friends' in reference:
			i = 0
			while(i < len(results)):
				temp = results[i].get_friends()
				for x in reference['friends']:
					if x not in temp:
						del results[i]
						i -= 1
						break
				i += 1
		if 'website' in reference:
			i = 0
			while(i < len(results)):
				if results[i].get_website() != reference['website']:
					del results[i]
				else:
					i += 1
		if 'email' in reference:
			i = 0
			while(i < len(results)):
				if results[i].get_email() != reference['email']:
					del results[i]
				else:
					i += 1
		if 'nickname' in reference:
			i = 0
			while(i < len(results)):
				if results[i].get_nickname() != reference['nickname']:
					del results[i]
				else:
					i += 1
		if 'city' in reference:
			i = 0
			while(i < len(results)):
				if results[i].get_city() != reference['city']:
					del results[i]
				else:
					i += 1
		if 'gender' in reference:
			i = 0
			while(i < len(results)):
				if results[i].get_gender() != reference['gender']:
					del results[i]
				else:
					i += 1
		if 'interests' in reference:
			i = 0
			while(i < len(results)):
				temp = results[i].get_interests()
				for x in reference['interests']:
					if x not in temp:
						del results[i]
						i -= 1
						break
				i += 1
		return results

		




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
	theme = ListField(default = [])
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
		if isinstance(self.participants, str):
			return json.loads(self.participants)
		return self.participants
	def get_locale(self):
		return self.locale
	def get_theme(self):
		if isinstance(self.theme, str):
			return json.loads(self.theme)
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
		if isinstance(self.supporters, str):
			return json.loads(self.supporters)
		return self.supporters

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
		p = self.get_participants()
		if participant_id not in p:
			p.append(participant_id)
			self.participants = p
			self.save()
			return True
		self.participants = p
		self.save()
		return False
	def remove_participants(self, participant_id):
		p = self.get_participants()
		if participant_id in p:
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
	def append_theme(self, theme_id):
		t = self.get_theme()
		if theme_id not in t:
			t.append(theme_id)
			self.theme = t
			self.save()
			return True
		self.theme = t
		self.save()
		return False
	def remove_theme(self, theme_id):
		t = self.get_theme()
		if theme_id in t:
			t.remove(theme_id)
			self.theme = t
			self.save()
			return True
		self.theme = t
		self.save()
		return False
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
		s = self.get_supporters()
		if supporter_id not in s:
			s.append(supporter_id)
			self.supporters = s
			self.save()
			return True
		self.supporters = s
		self.save()
		return False
	def remove_supporters(self, supporter_id):
		s = self.get_supporters()
		if supporter_id in s:
			s.remove(supporter_id)
			self.supporters = s
			self.save()
			return True
		self.supporters = s
		self.save()
		return False
	def get_theme_content(self):
		results = []
		for item in self.get_theme():
			results.append(Theme.objects.get(id = item).content)
		return ','.join(results)

	def __str__(self):
		return self.get_theme_content()

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

class Theme(models.Model):
	content = models.CharField(max_length = 100)
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
