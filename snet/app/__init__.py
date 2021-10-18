import snet
import argparse
from datetime import date
from typing import TypeVar
from snet.conf import settings

Args = TypeVar("Args")


class SNetService:
    @staticmethod
    #когда staticmethod, тогда self в скобки функции не передаем
    def create_parser() -> Args:
        parser = argparse.ArgumentParser(
            prog = "Social network.",
            description = "Very cool social network.\n(c) Kolya Gajdym {}".format(
                date.today().year
            ),
            #(c) - копирайт, хз зачем
            add_help = False,
        )
        parser.add_argument(
            "-h",
            "--help",
            action = "help",
            help = "Print this message.",
        )
        parser.add_argument(
            "-v",
            "--version",
            action = "version",
            help = "Current version.",
            version = f"Snet: {snet.__version__}",
        )
        parser.add_argument(
            "--host",
            dest = "host",
            default = "127.0.0.1",
            help = "Network adress.",
        )
        parser.add_argument(
            "--port",
            dest = "port",
            default = 8008,
            help = "Network port.",
        )
        parser.add_argument(
            "-d"
            "--debug",
            dest = "debug",
            default = "store_true",
            help = "Run application in DEBUG mode.",
        )
        parser.add_argument(
            "-t"
            "--task",
            dest = "task",
            default = "store_true",
            help = "Run bg tasks.",
        )
        parser.add_argument(
            "-w"
            "--wait",
            dest = "wait",
            default = "store_true",
            help = "Run bg tasks.",
        )
        # return parser.parse_args()
        return parser._parse_known_args()[0], parser.parse_known_args()[1]


    def __init__(self) -> None:
        self.arguments, self.vars = self.create_parser()
        print(self.arguments)
        print(self.vars)
        # print(self.create_parser())

    def load(self):
        print(settings.DEBUG)
        return self

    def run(self):
        ...


def run():
    print("WORK!!!")
    SNetService().load().run() #точка входа
