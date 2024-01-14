# qgridtrusted

_A fork of [qgrid] using [trusted publishing]._

To reduce the changes required to adopt this fork, the project is installed as
`qgridtrusted` and the Python package is imported as `qgrid`. For details of how
to use the `qgrid` package see [README.rst](/README.rst).

Pull requests including automated tests are welcome.

## Priorities

This fork should:

1. Be easy to install
2. Be compatible with recent releases of its dependencies
3. Minimise changes to the Python code (see below)

## Changes to the Python code

Command to view the changes to the Python code:

    git diff 877b420d3bd83297bbcc97202b914001a85afff2.. '*.py'

Command to view a summary of the number of lines changed using [cloc]:

    cloc --vcs=git --include-lang=Python --diff 877b420d3bd83297bbcc97202b914001a85afff2 HEAD

[cloc]: https://github.com/AlDanial/cloc
[qgrid]: https://github.com/quantopian/qgrid
[trusted publishing]: https://docs.pypi.org/trusted-publishers/
