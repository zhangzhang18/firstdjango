#!/usr/bin/env python
# coding:utf-8


import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdjango.settings")

django.setup()


def main():
    from blog.models import Article
    f = open('oldblog.txt')
    BlogList = []
    for line in f:
        title, content = line.split('****')
        article = Article(title=title, content=content)
        BlogList.append(article)
        # Article.objects.get_or_create(title=title, content=content)

        # django.db.models 中还有一个函数叫 get_or_create() 有就获取过来，没有就创建，
        # 用它可以避免重复
    f.close()
    Article.objects.bulk_create(BlogList)


# 导出
# python manage.py dumpdata blog > blog_dump.json
# 导入
# python manage.py loaddata blog_dump.json
# python manage.py dumpdata auth > auth.json # 导出用户数据


if __name__ == '__main__':
    main()
    print ('Done')


# 数据库的迁移
