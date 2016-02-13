import logging
import time
from random import randint

from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from buggy_module import lots_of_debug_logs
from .models import Table

logger = logging.getLogger(__name__)


@require_http_methods(('GET', ))
def home(request):
    logger.debug("DEBUG: Log at logging_fun.home")
    logger.info("INFO: Log at logging_fun.home")
    logger.exception("EXCEPTION: Log at logging_fun.home")
    logger.warning("WARNING: Log at logging_fun.home")
    logger.critical("CRITICAL: Log at logging_fun.home")
    return HttpResponse('Logging is Fun?')


@require_http_methods(('GET', ))
def buggy(request):
    logger.debug("DEBUG: Calling lots_of_debug_logs")
    lots_of_debug_logs()
    logger.debug("DEBUG: Done calling lots_of_debug_logs")
    return HttpResponse('Logging is Fun?!')


@require_http_methods(('GET', 'POST'))
@csrf_exempt
def raise_500(request):
    if request.method == 'POST':
        logger.info(request)
        return HttpResponse('Please check logs for password!')
    Table.objects.all()[-1]
    return HttpResponse('Fun with Logging!')


@require_http_methods(('GET', ))
def hit_db(request):
    try:
        objs = Table.objects.all()[0]  # Lazy *_*
    except IndexError:
        pass
    return HttpResponse('Fun with Logging!')


@require_http_methods(('GET', ))
def delay(request):
    for i in range(3):
        logger.info('Log Number: {}'.format(i))
        time.sleep(randint(1, 3))
    logger.info('Returning finally!')
    return HttpResponse('Finally Responded!')


@require_http_methods(('GET', ))
def springboard(request):
    pass
