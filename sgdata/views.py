from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from json import dumps

import spacegrids as sg

def index(request):
  return HttpResponse('test')

def get_field(request, project,exp, field):

  context = RequestContext(request)

  D = sg.info_dict()
  P = sg.Project(D[project])
  P[exp].load(field)

  fld = P[exp][field]


  return HttpResponse(dumps(fld.json(types_allow=[sg.Gr,sg.Ax,sg.Coord])))