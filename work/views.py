from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

def start(request):
    return render_to_response('work/index.html',context_instance=RequestContext(request))
