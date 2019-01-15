from django.contrib import admin

from .models import BookInfo, HeroInfo

# class HeroInfoStackInline(admin.StackedInline):
class HeroInfoTabularInline(admin.TabularInline):
    model = HeroInfo
    extra = 1


# 定义模型站点管理类(管理模型数据在admin界面的展示)
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id', 'btitle', 'pub_date', 'bread']
    #fields = ['btitle', 'bpub_date']
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date', 'image']}),
        ('高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)
        })
    )
    # inlines = [HeroInfoTabularInline]


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hbook', 'read']
    list_filter = ['hbook', 'hgender']
    search_fields = ['hname']


admin.site.site_header = 'XIXI'
admin.site.site_title = 'gugu_city'
admin.site.index_title = 'welcome'

admin.site.register(BookInfo, BookInfoAdmin)



