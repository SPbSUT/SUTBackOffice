# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.pageTitle = T("Dashboard")
    response.pageSubtitle = T("overview of the application")
    response.flash = T("Hello World")
    response.active=1
    return dict(message=T('Welcome to web2py!'))

def rooms():
    rooms="test"


    rooms = items.Query.all()

    form = FORM(DIV(
                INPUT(_name='title', _class="form-control", _placeholder="Name" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='content', _class="form-control", _placeholder="Description of the room" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='floor', _class="form-control", _placeholder="Floor" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='number', _class="form-control", _placeholder="Number" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='workhours', _class="form-control", _placeholder="Work Hours ex: 10h00-16h00" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='phone', _class="form-control", _placeholder="Tel ex: +7 (812) 305-12-37" ,requires=IS_NOT_EMPTY()),

                INPUT(_type='submit', _class="btn btn-primary")
                ))

    if form.process().accepted: 
        message = 'form accepted'
        room = items()
        room.title = form.vars.title
        room.content = form.vars.content
        room.floor = int(form.vars.floor)
        room.number = int(form.vars.number)
        room.workhours = form.vars.workhours
        room.phone = form.vars.phone
        room.save()
    elif form.errors:
        message = 'form has errors'
    else:
        message = 'please fill out the form'

    response.pageTitle = T("Rooms management")
    response.pageSubtitle = T("All information about rooms in university")
    response.active=2
    return dict(rooms=rooms, form=form, message=message)


def editRoom():
    rooms = items.Query.all()

    room = items.Query.get(objectId=request.args[0])
    form = FORM(DIV(
                INPUT(_name='title', _class="form-control", _placeholder="Name" ,requires=IS_NOT_EMPTY(), value=room.title),
                INPUT(_name='content', _class="form-control", _placeholder="Description of the room" ,requires=IS_NOT_EMPTY(), value=room.content),
                INPUT(_name='floor', _class="form-control", _placeholder="Floor" ,requires=IS_NOT_EMPTY(), value=room.floor),
                INPUT(_name='number', _class="form-control", _placeholder="Number" ,requires=IS_NOT_EMPTY(), value=room.number),
                INPUT(_name='workhours', _class="form-control", _placeholder="Work Hours ex: 10h00-16h00" ,requires=IS_NOT_EMPTY(), value=room.workhours),
                INPUT(_name='phone', _class="form-control", _placeholder="Tel ex: +7 (812) 305-12-37" ,requires=IS_NOT_EMPTY(), value=room.phone),

                INPUT(_type='submit', _class="btn btn-primary")
                ))

    if form.process().accepted:
        message = 'form accepted'
        room.title = form.vars.title
        room.content = form.vars.content
        room.floor = int(form.vars.floor)
        room.number = int(form.vars.number)
        room.workhours = form.vars.workhours
        room.phone = form.vars.phone
        room.save()
        redirect(URL('default', 'rooms'))

    elif form.errors:
        message = 'form has errors'
    else:
        message = 'please fill out the form'

    response.pageTitle = T("Rooms management")
    response.pageSubtitle = T("All information about rooms in university")
    response.active=2
    return dict(rooms=rooms, form=form, message=message)


def deleteRoom():
    objectId = request.args[0]
    room = items.Query.get(objectId=objectId)
    room.delete()
    redirect(URL('default', 'rooms'))


def dormitory():
    category = categories.Query.get(name="Dormitory")
    infos = information.Query.filter(categoriesId=category.objectId)

    response.view = 'default/information.html'
    response.pageTitle = T("Information overview")
    response.pageSubtitle = T("All information about administrative information")
    response.active=33
    return dict(items=infos)


def immigration():
    category = categories.Query.get(name="Immigration")
    infos = information.Query.filter(categoriesId=category.objectId)

    response.view = 'default/information.html'
    response.pageTitle = T("Information overview")
    response.pageSubtitle = T("All information about administrative information")
    response.active=34
    return dict(items=infos)


def transport():
    category = categories.Query.get(name="Transport")
    infos = information.Query.filter(categoriesId=category.objectId)

    response.view = 'default/information.html'
    response.pageTitle = T("Information overview")
    response.pageSubtitle = T("All information about administrative information")
    response.active=35
    return dict(items=infos)


def university():
    category = categories.Query.get(name="University")
    infos = information.Query.filter(categoriesId=category.objectId)

    response.view = 'default/information.html'
    response.pageTitle = T("Information overview")
    response.pageSubtitle = T("All information about administrative information")
    response.active=36
    return dict(items=infos)


def newInformation():
    category = categories.Query.all()
    cat = ["Select a category"]
    for c in category:
        cat.append(c.name)

    form = FORM(DIV(
                INPUT(_name='title', _class="form-control", _placeholder="title" ,requires=IS_NOT_EMPTY()),
                SELECT(cat, value=cat[0], _class="form-control", _name="category"),
                TEXTAREA(_id="content", _name='content', _class="form-control", _placeholder="Write your content here" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='description', _class="form-control", _placeholder="Short description of the content" ,requires=IS_NOT_EMPTY()),
                INPUT(_type="hidden"),
                INPUT(_type='submit', _class="btn btn-primary")
                ))

    if form.process().accepted:
        message = 'form accepted'
        info = information()

        info.title = form.vars.title
        info.description = form.vars.description
        info.content = form.vars.content
        info.categoriesId = categories.Query.get(name=form.vars.category).objectId
        info.save()
        #redirect(URL('default', 'rooms'))


    elif form.errors:
        message = 'form has errors'
    else:
        message = 'please fill out the form'


    response.pageTitle = T("New Information")
    response.pageSubtitle = T("Here you can see and edit administrative information")
    response.active=32
    return dict(form=form, message=message)

def editInformation():
    category = categories.Query.all()
    cat = ["Select a category"]
    for c in category:
        cat.append(c.name)

    cati = 0

    info = information.Query.get(objectId=request.args[0])
    i = 1
    for c in category:
        if c.objectId == info.categoriesId:
            cati = i
        i = i + 1


    form = FORM(DIV(
        INPUT(_name='title', _class="form-control", _placeholder="title" ,requires=IS_NOT_EMPTY(), value=info.title),
        SELECT(cat, value=cat[cati], _class="form-control", _name="category"),
        TEXTAREA(_id="content", _name='content', _class="form-control", _style="height: 800px",_placeholder="Write your content here" , requires=IS_NOT_EMPTY(), value=info.content),
        INPUT(_name='description', _class="form-control", _placeholder="Short description of the content" ,requires=IS_NOT_EMPTY(), value=info.description),

        INPUT(_type='submit', _class="btn btn-primary")
    ))

    if form.process().accepted:

        message = 'form accepted'

        info.title = form.vars.title
        info.description = form.vars.description
        info.content = form.vars.content
        info.categoriesId = categories.Query.get(name=form.vars.category).objectId
        info.save()
        redirect(URL('default', 'index'))


    elif form.errors:
        message = 'form has errors'
    else:
        message = 'please fill out the form'

    response.view = 'default/newInformation.html'
    response.pageTitle = T("edit Information")
    response.pageSubtitle = T("Here you can see and edit administrative information")
    response.active=32
    return dict(form=form, message=message)

def deleteInformation():
    objectId = request.args[0]
    info = information.Query.get(objectId=objectId)
    info.delete()
    redirect(URL('default', 'index'))


def contacts():
    cont = contact.Query.all()

    response.view = 'default/contact.html'
    response.pageTitle = T("Contact overview")
    response.pageSubtitle = T("All information about contact")
    response.active=4
    return dict(items=cont)

def newContact():

    form = FORM(DIV(
                INPUT(_name='firstname', _class="form-control", _placeholder="First Name" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='lastname', _class="form-control", _placeholder="Last Name" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='job', _class="form-control", _placeholder="Job" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='telephone', _class="form-control", _placeholder="Telephone" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='email', _class="form-control", _placeholder="email" ,requires=IS_NOT_EMPTY()),
                INPUT(_name='photo', _class="form-control", _placeholder="photo" ,requires=IS_NOT_EMPTY()),
                INPUT(_type='submit', _class="btn btn-primary")
                ))

    if form.process().accepted:
        message = 'form accepted'
        info = contact()

        info.firstName = form.vars.firstname
        info.lastName = form.vars.lastname
        info.job = form.vars.job
        info.tel = form.vars.telephone
        info.email = form.vars.email
        info.photo = form.vars.photo
        info.save()
        #redirect(URL('default', 'rooms'))


    elif form.errors:
        message = 'form has errors'
    else:
        message = 'please fill out the form'


    response.pageTitle = T("New contact")
    response.pageSubtitle = T("Here you can create a new")
    response.active=32
    return dict(form=form, message=message)

def editContact():

    c = contact.Query.get(objectId=request.args[0])

    form = FORM(DIV(
                INPUT(_name='firstname', _class="form-control", _placeholder="First Name" ,requires=IS_NOT_EMPTY(), value=c.firstName),
                INPUT(_name='lastname', _class="form-control", _placeholder="Last Name" ,requires=IS_NOT_EMPTY(), value=c.lastName),
                INPUT(_name='job', _class="form-control", _placeholder="Job" ,requires=IS_NOT_EMPTY(), value=c.job),
                INPUT(_name='telephone', _class="form-control", _placeholder="Telephone" ,requires=IS_NOT_EMPTY(), value=c.tel),
                INPUT(_name='email', _class="form-control", _placeholder="email" ,requires=IS_NOT_EMPTY(), value=c.email),
                INPUT(_name='photo', _class="form-control", _placeholder="photo" ,requires=IS_NOT_EMPTY(), value=c.photo),
                INPUT(_type='submit', _class="btn btn-primary")
                ))

    if form.process().accepted:
        message = 'form accepted'

        c.firstName = form.vars.firstname
        c.lastName = form.vars.lastname
        c.job = form.vars.job
        c.tel = form.vars.telephone
        c.email = form.vars.email
        c.photo = form.vars.photo
        c.save()
        redirect(URL('default', 'contacts'))


    elif form.errors:
        message = 'form has errors'
    else:
        message = 'please fill out the form'

    response.view = 'default/newContact.html'
    response.pageTitle = T("Edit Contact")
    response.pageSubtitle = T("Here you can see and edit contact")
    response.active=4
    return dict(form=form, message=message)

def vkInternationalCooperation():
    import vk_api
    import json
    login, password = 'cygrosjean@gmail.com', ''
    try:
        vk = vk_api.VkApi(login, password)
    except vk_api.AuthorizationError as error_msg:
        print(error_msg) 
        return

    values = {
        'count': 5, # Получаем только один пост
        'domain' : 'international_cooperation_spbsut'
    }
    jsonVk = vk.method('wall.get', values)
    news=[]
    for (val) in jsonVk["items"]:
        new = {}
        new['id'] = val["id"]
        if not val["text"]:
            for copy_history in val["copy_history"]:
                new['text'] = copy_history["text"];
            new['repost'] = 1
        else:
            new['text'] = val["text"]
            new['repost'] = 0
        news.append(new)
    response.pageTitle = T("VK InternationnalCooperation")
    response.pageSubtitle = T("Yep it's VK ;)")
    response.active=5
    return dict(news=news, message="")

def vkNewsEnglish():
    import vk_api
    import json
    login, password = 'cygrosjean@gmail.com', ''
    try:
        vk = vk_api.VkApi(login, password)
    except vk_api.AuthorizationError as error_msg:
        print(error_msg) 
        return

    values = {
        'count': 5, # Получаем только один пост
        'domain' : 'bonch.news.english'
    }
    jsonVk = vk.method('wall.get', values)
    news=[]
    for (val) in jsonVk["items"]:
        new = {}
        new['id'] = val["id"]
        if not val["text"]:
            for copy_history in val["copy_history"]:
                new['text'] = copy_history["text"];
            new['repost'] = 1
        else:
            new['text'] = val["text"]
            new['repost'] = 0
        news.append(new)
    response.pageTitle = T("VK News English")
    response.pageSubtitle = T("Yep it's VK ;)")
    response.active=6
    return dict(news=news, message="")

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def deleteContact():
    objectId = request.args[0]
    info = contact.Query.get(objectId=objectId)
    info.delete()
    redirect(URL('default', 'contacts'))

