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

log = getLogger(__name__)

def includeme(config):
    config.scan(__name__)
    config.add_route('college_list', '/college/list')
    config.add_route('college_add', '/college/add')
    config.add_route('college_save', '/college/save')
    config.add_route('college_del', '/college/del')
    
@view_config(route_name='college_list', renderer='college/college_list.mako',permission='admin')
def listcollege(request):
     page = int(request.params.get('page', 1))
     conn = DBSession()
     items = conn.query(College).order_by(College.id)
     page_url = paginate.PageURL_WebOb(request)
     items = paginate.Page(
            items,
            page=int(page),
            items_per_page=10,
            url=page_url,
            )
     return dict(items=items)
 
@view_config(route_name='college_add', renderer='college/college_add.mako',permission='admin')
def addcollege(request):
     conn = DBSession()
     college = conn.query(College).filter(College.id==request.params.get('collegeid')).first()
     return dict(college=college)    
 
@view_config(route_name='college_save', renderer='college/college_add.mako',permission='admin')
def savecollege(request):
     conn = DBSession()
     if request.params.get('college.id'):
          college = conn.query(College).filter(College.id==request.params.get('college.id')).first()
          college.name=request.params.get('college.name')
          conn.flush()
          return HTTPFound(location=request.route_url('college_list'))
     else:
         college = College()
         college.name = request.params.get('college.name')
         conn.add(college)
         conn.flush()
         return HTTPFound(location=request.route_url('college_list'))
     return HTTPFound(location=request.route_url('college_list'))
 
@view_config(route_name='college_del', renderer='college/college_del.mako',permission='admin')
def delcollege(request):
    conn = DBSession()
    college = conn.query(College).filter(College.id==request.params.get('collegeid')).first()
    if request.params.get('college.id'):
        college= conn.query(College).filter(College.id==request.params.get('college.id')).first()
        conn.delete(college)
        conn.flush()
        return HTTPFound(location=request.route_url('college_list'))
    return dict(college=college)
