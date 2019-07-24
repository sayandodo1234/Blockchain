from django.contrib import admin
from .models import Block,Blockchain,Node

# Register your models here.
admin.site.register(Block)
admin.site.register(Blockchain)
admin.site.register(Node)