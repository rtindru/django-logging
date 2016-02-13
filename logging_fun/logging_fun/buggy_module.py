import logging
from logging import Filter

logger = logging.getLogger(__name__)


def lots_of_debug_logs():
    logger.debug('You know nothing about DEBUG logging, Jon Snow!\n')
    logger.debug('You know nothing about DEBUG logging, Jon Snow!\n')


class PasswordObfuscationFilter(Filter):
    """Filters out passwords in log messages."""

    def filter(self, record):
        import pdb; pdb.set_trace()
        if getattr(record.msg, 'POST') and record.msg.POST.get('password', None):
            qd = record.msg.POST.copy()
            qd['password'] = "%s (removed)" % ('x'*8)
            record.msg.POST = qd
        return True
