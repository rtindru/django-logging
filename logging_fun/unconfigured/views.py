import logging

from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)


@require_http_methods(('GET', ))
def home(request):
    logger.debug("\n\nInside unconfigured::")
    logger.debug("unconfigured:: DEBUG: This is a debug log")
    logger.info("unconfigured:: INFO: Let's get started")
    try:
        a = []
        a[100]
    except IndexError as e:
        logger.exception(e)
    return HttpResponse('unconfigured:: Logging is Fun?!')



