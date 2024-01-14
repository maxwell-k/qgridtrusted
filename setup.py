import logging
from pathlib import Path
from subprocess import run

from setuptools import Command
from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info

STATIC = Path("qgrid") / "static"
TARGETS = [STATIC / "extension.js", STATIC / "index.js"]
STATIC.mkdir(exist_ok=True)

logging.basicConfig(level=logging.DEBUG)
logging.info("setup.py entered")


def prepare(command):
    class DecoratedCommand(command):
        def run(self):
            if not all(target.is_file() for target in TARGETS):
                self.distribution.run_command("jsdeps")
            command.run(self)

    return DecoratedCommand


class jsdeps(Command):
    def finalize_options(self):
        pass

    def initialize_options(self):
        pass

    def run(self):
        try:
            run(["npm", "--version"], capture_output=True, check=True)
        except Exception:
            logging.error("`npm` unavailable.")
        else:
            logging.info("Running `npm install`. This may take a while.")
            run(["npm", "install"], cwd="js", check=True)

        if missing := [i for i in TARGETS if not i.is_file()]:
            raise ValueError("Missing files: %s" % missing)


data_files: list[tuple[str, list[str]]] = [
    ("share/jupyter/nbextensions/qgrid", list(map(str, STATIC.iterdir()))),
]
cmdclass = dict(build_py=prepare(build_py), egg_info=prepare(egg_info), jsdeps=jsdeps)
setup(data_files=data_files, cmdclass=cmdclass)
