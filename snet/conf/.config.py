import pathlib
import sys, os


BASE_DIR = pathlib.Path(__file__).parent.parent.absolute()
DEBUG = True

LOG_DIR = BASE_DIR.parent.absolute() / ".log"

if not LOG_DIR.exists():
    os.makedirs(LOG_DIR)

MIDDLEWARES = []
STARTUP = []
SHUTDOWN = []
TASKS = []
DATABASE = {
    "connections":{
        "default": f"sqlite://{BASE_DIR}/db.sqlite"
        # "default":{
        #     "engine": "tortoise.backends.asyncpg",
        #     "credentials":{
        #         "host": "127.0.0.1",
        #         "port": 5432,
        #         "user": "snet",
        #         "password": "parol",
        #         "database": "snet_data",
        #         "minsize": 50,
        #         "maxsize": 90 if DEBUG else 190,
        #     }
        # }
    },
    "apps":{
        "user": {
            "models": ["snet.store.user_models"],
            "default_connection": "default",
        }
    },
    "timezone": "UTC",
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "[%(asctime)s] # %(levelname)s %(message)s"},
        "extended": {
            "format": (
                "<[%(asctime)s LINE: %(lineno)-5d] # %(levelname)-8s"
                "%(pathname)s %(funcName)s():> %(message)s"
            )
        },
        "json": {
            "format": (
                '{"_level": "%(levelname)s", "_time": "%(asctime)s", "_thread": '
                '%(thread)d, "_file": "%(pathname)s", "_func": "%(funcName)s()",'
                ' "_line": %(lineno)d, "_message": "%(message)s", "_name": "%(name)s"}'
            )
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "extended",
            "stream": "ext://sys.stdout",
        },
        "syslog": {
            "class": "logging.handlers.SysLogHandler",
            "formatter": "extended",
            "address": "/dev/log",
            "facility": "local0",
        }
        if sys.platform == "linux"
        else {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "extended",
            "filename": LOG_DIR / "all.log",
            "maxBytes": 10485760,
            "backupCount": 10,
            "encoding": "utf8",
        },
        "except": {
            "class": "logging.handlers.SysLogHandler",
            "formatter": "extended",
            "address": "/dev/log",
            "facility": "local1",
        }
        if sys.platform == "linux"
        else {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "extended",
            "filename": LOG_DIR / "exceptions.log",
            "maxBytes": 10485760,
            "backupCount": 10,
            "encoding": "utf8",
        },
    },
    "loggers": {
        "snet.dev": {"level": "DEBUG", "handlers": ["console", "syslog"]},
        "snet.syslog": {
            "level": "DEBUG" if DEBUG else "WARNING",
            "handlers": ["syslog"],
        },
        "snet.except": {"level": "WARNING", "handlers": ["except"]},
    },
}

LOGGER = "snet.dev" if DEBUG else "snet.syslog"
EXCEPTLOGGER = "snet.except"
ROOTURLS = "snet.web.root.urls"