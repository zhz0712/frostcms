# coding=utf-8
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.security import remember, forget
from logging import getLogger
from .models import *
from .token import Token
import time
import cgi, uuid
import webhelpers.paginate as paginate
from datetime import *  
import time

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('lesson_list', '/lesson/list')
    config.add_route('lesson_add', '/lesson/add')
    config.add_route('lesson_save', '/lesson/save')
    config.add_route('lesson_del', '/lesson/del')
    
@view_config(route_name='lesson_list', renderer='lesson/lesson_list.mako',permission='admin')
def listlesson(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     semesters = conn.query(Semester).order_by(Semester.id)
     if request.method == "POST":
         semesterid = request.params.get('semesterid')
         items = conn.query(Lesson).filter(Lesson.semesterid==semesterid)
     else :
         items = conn.query(Lesson).order_by(Lesson.id)
     lis = conn.query(Semester).order_by(Semester.id)
     page_url = paginate.PageURL_WebOb(request)
     items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
     return dict(items=items,lis=lis)
 
@view_config(route_name='lesson_add', renderer='lesson/lesson_add.mako',permission='admin')
def addlesson(request):
     conn = DBSession()
     lesson = conn.query(Lesson).filter(Lesson.id==request.params.get('lessonid')).first()
     lis = conn.query(Lesson).order_by(Lesson.id)
     return dict(lesson=lesson,lis=lis)    
 
@view_config(route_name='lesson_save', renderer='lesson/lesson_add.mako',permission='admin')
def savelesson(request):
     conn = DBSession()
     if request.params.get('lesson.id'):
          lesson = conn.query(Lesson).filter(Lesson.id==request.params.get('Lesson.id')).first()
          lesson.name = request.params.get('lesson.name')
          lesson.collegeid = request.params.get('lesson.collegeid')
          conn.flush()
     else:
         lesson = Lesson()
         lesson.name = request.params.get('lesson.name')
         lesson.collegeid = request.params.get('lesson.collegeid')
         conn.add(lesson)
     return HTTPFound(location=request.route_url('lesson_list'))
 
@view_config(route_name='lesson_del', renderer='lesson/lesson_del.mako',permission='admin')
def dellesson(request):
    conn = DBSession()
    lesson = conn.query(Lesson).filter(Lesson.id==request.params.get('lessonid')).first()
    if request.params.get('lesson.id'):
        lesson = conn.query(Lesson).filter(Lesson.id==request.params.get('lesson.id')).first()
        conn.delete(lesson)
        return HTTPFound(location=request.route_url('lesson_list'))
    lis = conn.query(Semester).order_by(Semester.id)
    return dict(lesson=lesson,lis=lis)