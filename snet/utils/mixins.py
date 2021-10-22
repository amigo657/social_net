import logging
import traceback
from snet.conf import settings


class LogMixin():
    __log = logging.getLogger(settings.LOGGER)
    __exept_log = logging.getLogger(settings.EXCEPTLOGGER)

    @property
    def _log(self):
        return self.__log

    @property
    def _exlog(self):
        return self.__exept_log

    @property
    def _trace(self):
        return traceback.format_exc()