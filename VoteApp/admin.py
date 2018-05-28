from django.contrib import admin

# Register your models here.
from VoteApp.models import User, VoteType, Candidate, ChatRecord, UserVoteRecord

#注册用户表、投票类型、候选者表、聊天记录
admin.site.register(User)
admin.site.register(VoteType)
admin.site.register(Candidate)
admin.site.register(ChatRecord)
admin.site.register(UserVoteRecord)
