# myProgramme-back
个人学习总结后端，项目知识点摘要

1、基于django创建项目目录
django-admin startproject '项目目录名称'
2、启动项目（在项目根目录下）
python manage.py runserver // 默认使用8000端口
python manage.py runserver 8080 // 修改访问端口为8080

一般可以通过localhost访问，如果要通过本机ip访问，需要修改settings中的配置
ALLOWED_HOSTS = [192.168.1.6]

3、创建一个应用
python manage.py startapp sale // sale为应用名称(注意该sale目录与根目录并行，但是他们是上下级的关系)

4、在每个应用中的views中创建路由
    4.1
    sale下的 views
        from django.http import HttpResponse // 引入django的HttpResponse
        def index(request): // 定义一个index函数
            return HttpResponse("Hello, world. You're at the polls index.")

    4.2、在项目的根目录下找到urls.py，这里配置路由
        from sale.views import index; // 引入刚才sale下的views文件下的 index 函数
        path('sale/index/', index),  // 配置路由地址 'sale/index/'，并指向刚才引入的index函数。
    这样一个sale下的index路由就创建成功了
    4.3、python manage.py runserver  //打开python服务
    在地址栏输入http://127.0.0.1:8000/sale/index/ 就可以看到index函数返回的 "Hello, world. You're at the polls index."

    上面的方法创建几个、或者几十个小型项目路由地址还可以，但是大型项目这样创建的话，根目录下的urls.py文件就会显得很臃肿，解决办法就是路由拆分组合。

