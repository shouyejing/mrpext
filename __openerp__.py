# -*- coding:utf-8 –*-
{
    'name': "mrpext",
    'version': '1.0',
    'depends': ['base', 'mrp', 'mrp_operations'],
    'author': "wangting",
    'category': 'custom',
    'data': [
        'views/productionrecord.xml',
        'views/workorder.xml',
        # 'security/security.xml',
        # 'security/ir.model.access.csv'
    ],
    'description': """
版本1.10

主要功能：

  给每个工单增加每日生产记录管理功能，用来分析每个工单的产量、次品率，每个员工生产效率等等。
  
  在生产菜单那里，你能找到生产记录相关的菜单。在work oder的form view里，会多出一页显示它的每日生产记录。
  
  如果你有兴趣，可以给我提建议(QQ:39181819)，让我们一起完善它。

2015.1.9 更新：

  1、生产记录操作工默认设置为当前登录的用户。操作工的数据类型由res.partner改为res.user
  
  2、录入生产记录的时候，日期默认设置为当前日期。

2015.1.10 更新：

  1、生产记录加入了search view功能：两个filter，默认filter为My Records。
  
2015.1.12 更新：

  1、加入多语言功能，支持英语、中文。

2015.1.13 更新：

  1、加入权限控制

    """

}
