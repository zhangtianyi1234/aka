#coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context
from django.template import RequestContext
import os, datetime

def mainpage(request):#mainpage
	return render_to_response('mainpage.html',context_instance=RequestContext(request))
