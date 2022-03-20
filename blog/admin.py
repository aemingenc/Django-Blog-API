from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin





from.models import Card,Comments,Likes



class LikesInline(SuperInlineModelAdmin,admin.TabularInline):
    model=Likes
#KAÇ TANE CEVAP SATIRI OLSUN
    extra = 1

class CommentsInline(SuperInlineModelAdmin,admin.StackedInline):
    model=Comments
    extra = 1
    

class CardAdmin(SuperModelAdmin):
    model=Card
    inlines = (CommentsInline,LikesInline)



admin.site.register(Card,CardAdmin)
admin.site.register(Comments)
admin.site.register(Likes)
