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
    sale下的 views.py文件中
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
    4.4、路由拆分思路：每一个应用（如sale应用）,在该应用下创建一个urls.py专门用来处理这个应用下的路由地址和函数方法处理该路由，再将该文件暴露出去，在根目录下的urls.py文件中引入sale应用中的urls.py文件，那么sale应用的所有路由，就全部添加到根目录下的urls.py中，达到分层的效果，当然也可以继续嵌套（推荐两级路由就够用了！）
    在sale目录下创建二级路由文件urls.py
    from django.urls import path
    from sale.views import index,index1,index2  //从sale中引入所有该应用的路由，并挂在urls.py中，一起暴露出去
    urlpatterns = [
        path('index/', index),
        path('index1/', index1),
        path('index2/', index2),
        ......
    ]
    在根目录中的urls.py(相当于一级路由)中引入该二级路由以及该二级路由下的所有子路由（因为该应用下的路由，都挂在在该文件的二级路由下了）
    from django.urls import path,include //注意这时的根urls.py中需要引入include(用于引入所有的二级路由)
    urlpatterns = [
        ......
        path('sale/', include('sale.urls')), 
    ]

5、数据库的创建（先使用python自带的sqllite3）
    执行初始化数据库:python manage.py migrate // 会在根目录下创建一个db.sqlite3的数据库文件
    使用navicat可视化数据库视图，查看该数据库。
    创建连接，创建数据库名称myProgramme，用户名：luoliang，密码：123456
    注意：执行python manage.py migrate后，创建的应用都会有apps.py和models.py文件，每一个应用都有单独对应的数据库

6、数据库的操作ORM（Object relational mapping）对象映射


