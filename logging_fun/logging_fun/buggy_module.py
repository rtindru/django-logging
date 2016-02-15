import logging
from logging import Filter

logger = logging.getLogger(__name__)


def lots_of_debug_logs():
    logger.debug('You know nothing about DEBUG logging, Jon Snow!')
    logger.exception('Exception :: Raised inside logging_fun.buggy_module :: lots_of_debug_logs\n')


class PasswordObfuscationFilter(Filter):
    """Filters out passwords in log messages."""

    def filter(self, record):
        try:
            qd = record.msg.POST.copy()
            qd['password'] = "%s (removed)" % ('x'*8)
            record.msg.POST = qd
        except AttributeError:
            pass
        return True
