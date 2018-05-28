from django.db import models
# Create your models here.

# 自定义的Manager对象
from django.db.models import Manager


class CandidateManager(Manager):
	# 查询所有时默认不包含被逻辑删除的记录
	def get_queryset(self):
		return super().get_queryset().exclude(isDelete=True)#.order_by('-cVotes')

# 用户表
class User(models.Model):
	'''用户表：用户名、密码、电脑IP'''
	uName = models.CharField(max_length=20,unique=True)
	uPass = models.CharField(max_length=20,default=None,null=True)
	uIP = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)

	class Meta:
		# 自定义表名
		db_table = 'userTable'



# 投票类型表
class VoteType(models.Model):
	'''投票种类、种类简介'''
	pType = models.CharField(max_length=20, unique=True)
	pInfo = models.CharField(max_length=200)
	isDelete = models.BooleanField(default=False)

	class Meta:
		db_table = 'voteType'

	def __str__(self):
		return self.pType


#候选者表
class Candidate(models.Model):
	'''名称、年龄，竞选宣言，选票数,候选者图片名称,第几次竞选'''
	cName = models.CharField(max_length=20,unique=True)
	cAge = models.IntegerField(default=0)
	cDeclaration = models.CharField(max_length=300,default='')
	cVotes = models.IntegerField(default=0)
	cImgName = models.CharField(max_length=20,default='who.jpg')
	cTimes = models.IntegerField(default=1)
	isDelete = models.BooleanField(default=False)

	# 外键 与投票类型表形成一对多关系，一个投票类型对应多个候选者
	cVoteType = models.ForeignKey(VoteType,on_delete=models.SET_NULL,blank=True,null=True)


	# 给Buyer设置Manager类型的属性,名称任意
	# 设置以后,框架将不在为Buyer生成隐式属性objects
	# 定义管理器对象的目的,在于:1修改框架的默认查询设置 2为Buyer增加新的自定义功能
	cmanager = CandidateManager()

	class Meta:
		db_table = 'candidate'
		ordering= ['-cVotes']
		# 自定义输出
	def __str__(self):
		return self.cName

	# 外键 与用户形成多对多关系，一个用户可以投多个候选者，一个候选者可以被多个用户投


# 用户投票记录表
class UserVoteRecord(models.Model):
	'''用户名称、投票时间，投票给谁，投票类型，备注(如果是分享打分系统，就是分数),给候选者第几次投票'''
	uNameId = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
	uDate = models.DateField(auto_now=True)
	uRemark = models.CharField(max_length=20,default=None)
	uType = models.ForeignKey(VoteType, on_delete=models.SET_NULL, blank=True, null=True)
	uWhoId = models.ForeignKey(Candidate,on_delete=models.SET_NULL,blank=True,null=True)
	isDelete = models.BooleanField(default=False)
	uTimes = models.IntegerField(default=1)
	def getUSer(self):
		return self.uNameId

	class Meta:
		db_table = 'userVoteRecord'

	# 自定义输出
	# def __str__(self):
	# 	return str(self.uNameId.uName) +" "+ str(self.uDate)+" 投票给 "+str(self.uWhoId)


# 聊天记录表
class ChatRecord(models.Model):
	'''发送者、时间、内容、话题(候选者)，投票类型'''
	crName = models.CharField(max_length=20)
	# 设置时间字段为自动获取当前时间
	crTime = models.DateTimeField(auto_now=True)
	crInfo = models.CharField(max_length=200)
	crTopic = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)

	# 外键 与用户表是一对多、与候选者表是一对多、与投票类型是一对多的关系
	crUser = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
	crCandidate = models.ForeignKey(Candidate,on_delete=models.SET_NULL,blank=True,null=True)
	crType = models.ForeignKey(VoteType,on_delete=models.SET_NULL,blank=True,null=True)

	class Meta:
		db_table = 'chatRecord'

	# 自定义输出
	def __str__(self):
		return  str(self.crTime) + self.crName + ':'+ self.crInfo