# coding:utf-8
from django.contrib import admin
from .models import Article


# Register your models here.


# 只需要这三行代码，我们就可以拥有一个强大的后台！
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)
    search_fields = ('title', 'content',)

    def save_model(self, request, obj, form, change):
        if change:  # 更改的时候
            obj_oeiginal = self.model.objects.get(pk=obj.pk)
        else:  # 新增的时候
            obj_oeiginal = None
        obj.user = request.user
        obj.save()

    def delete_model(self, request, obj):
        obj.detele()

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(ArticleAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_char = chr(search_term)
            queryset |= self.model.objects.filter(title=search_term_as_char)
        except:
            pass
        return queryset, use_distinct


class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)


# list_display 就是来配置要显示的字段的admin.site.register(Article)
admin.site.register(Article, ArticleAdmin)
