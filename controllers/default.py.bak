# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """     
    db.quiz.insert(Ans='B')
    db.quizb.insert(Ans='B')
    db.quizc.insert(Ans='A')
    db.quizd.insert(Ans='A')
    db.quize.insert(Ans='A')
    db.quiz2a.insert(Ans='D')
    db.quiz2b.insert(Ans='D')
    db.quiz2c.insert(Ans='D')
    db.quiz2d.insert(Ans='D')
    db.quiz2e.insert(Ans='B')
    response.flash = T("Welcome to Online exam.com!")
    return locals()

@auth.requires_login()
def profile():
     response.flash="Your Profile"
     rows = db(db.auth_user.id==auth.user.id).select()
     return locals()
    
@auth.requires_login()
def edit():
    form = SQLFORM(db.auth_).process()
    return locals()

@auth.requires_login()
def iq1():
    ans="A"
    form=SQLFORM(db.quiz).process()
    rows=db(db.quiz).select()
    form1b=SQLFORM(db.quizb).process()
    rows1b=db(db.quizb).select()
    form1c=SQLFORM(db.quizc).process()
    rows1c=db(db.quizc).select()
    form1d=SQLFORM(db.quizd).process()
    rows1d=db(db.quizd).select()
    form1e=SQLFORM(db.quize).process()
    rows1e=db(db.quize).select()
    return locals()

@auth.requires_login()
def iq2():
    ans="A"
    score=0
    form2a=SQLFORM(db.quiz2a).process()
    rows2a=db(db.quiz2a).select()
    form2b=SQLFORM(db.quiz2b).process()
    rows2b=db(db.quiz2b).select()
    form2c=SQLFORM(db.quiz2c).process()
    rows2c=db(db.quiz2c).select()
    form2d=SQLFORM(db.quiz2d).process()
    rows2d=db(db.quiz2d).select()
    form2e=SQLFORM(db.quiz2e).process()
    rows2e=db(db.quiz2e).select()
    return locals()

def marks():
    rows=db(db.quiz).select()
    rows1b=db(db.quizb).select()
    rows1c=db(db.quizc).select()
    rows1d=db(db.quizd).select()
    rows1e=db(db.quize).select()
    db.mytable.hello.writable=False
    db.mytable.hello.readable=False
    form1=SQLFORM(db.mytable)
    return locals()

def marks2():
    rows2a=db(db.quiz2a).select()
    rows2b=db(db.quiz2b).select()
    rows2c=db(db.quiz2c).select()
    rows2d=db(db.quiz2d).select()
    rows2e=db(db.quiz2e).select()
    return locals()

def test():
    session.flash=T("hiiiiii")
    return 'GGGG'

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
