from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse, Http404
import random


def home(request, **kwargs):
    phrase = random.choice(settings.PHRASES)
    try:
        t = kwargs['template']
    except:
        raise Http404
    c = RequestContext(request, locals())
    r = HttpResponse(t.render(c), 'text/html')
    r['Pragma'] = 'no-cache'
    return r
