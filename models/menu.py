# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Online Exam'),XML('&nbsp;'),
                  _class="brand",_href="http://127.0.0.1:8000/onlineexam/")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [(T('Home'), False, URL('default', 'index'),[]),
     (SPAN('Profile'),False,URL('default','profile'),[(T('Edit'),False,URL('default','user',args='profile')),(T('View'),False,URL('default','profile'))]),
    (SPAN('Test'),False,URL('default','index'),[(T('IQ Level_1'),False,URL('default','iq1')),(T('IQ Level_2'),False,URL('default','iq2'))])
]
if "auth" in locals(): auth.wikimenu()
