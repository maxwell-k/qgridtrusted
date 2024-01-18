"""Ready to publish

If a suitable wheel exists and the corresponding version hasn't been published
to PyPI then exit with a return code of zero.

Wheel filename convention:
https://packaging.python.org/en/latest/specifications/binary-distribution-format/#file-name-convention
"""
from pathlib import Path

import urllib3

SUFFIX = "-py3-none-any.whl"
GLOB = f"dist/*{SUFFIX}"


def main() -> int:
    try:
        wheel = next(Path(".").glob(GLOB))
    except StopIteration:
        print(f"{GLOB=} not found")
        return 1
    name, _, version = wheel.name.removesuffix(SUFFIX).partition("-")
    response = urllib3.request("GET", f"https://pypi.org/pypi/{name}/json")
    result = int(version in (releases := list(response.json()["releases"])))
    print(f"{version=} {releases=} {result=}")
    return result


if __name__ == "__main__":
    raise SystemExit(main())

# /// script
# dependencies = ["urllib3"]
# ///
