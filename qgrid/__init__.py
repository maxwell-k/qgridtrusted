from ._version import __version__  # noqa F401

from .grid import (
    disable,
    enable,
    off,
    on,
    QgridWidget,
    QGridWidget,
    set_defaults,
    set_grid_option,
    show_grid,
)


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "static",
            "dest": "qgrid",
            "require": "qgrid/extension",
        }
    ]


__all__ = [
    "enable",
    "disable",
    "set_defaults",
    "on",
    "off",
    "set_grid_option",
    "show_grid",
    "QgridWidget",
    "QGridWidget",
]
