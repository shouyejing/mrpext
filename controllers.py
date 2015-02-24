# -*- coding: utf-8 -*-
from openerp import http



class Academy(http.Controller):
    @http.route('/mrpext/', auth='public')
    def index(self):
        return http.request.render('mrpext.index', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn","wangting"]})

    @http.route('/mrpext/links', auth='public')
    def links(self):
        return http.request.render('mrpext.links',
                                   {'links': [['腾讯','http://www.qq.com'],
                                              ['odoo','http://www.odoo.com'],
                                              ['百度','http://www.baidu.com'],
                                              ['谷歌','http://www.google.com']]})

    @http.route('/mrpext/myform',auth='public')
    def myform(self):
        return """<form action="/mrpext/myformdata" method="post"  enctype="multipart/form-data">
                    First name:
                    <input type="text" name="firstname" />
                    <br />
                    Last name:
                    <input type="text" name="lastname" />
                    <button>点这里POST</button>
                    </form>"""

    @http.route('/mrpext/myformdata',auth='public',type='http')
    def myformdata(self, **kwargs):
        return str(kwargs)