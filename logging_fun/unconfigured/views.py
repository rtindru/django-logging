import logging

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)


@require_http_methods(('GET', ))
def home(request):
    logger.info("unconfigured:: INFO: Let's get started")
    logger.debug("unconfigured:: DEBUG: This is a debug log")
    logger.exception("unconfigured:: EXC: Sumthang Wong")
    logger.warning("unconfigured:: WARN: This is a warning, don't mess with it")
    logger.critical("unconfigured:: CRITICAL: SYSTEM IS DOWN!")
    return HttpResponse('unconfigured:: Logging is Fun?!')



