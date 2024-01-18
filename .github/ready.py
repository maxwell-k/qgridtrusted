"""Ready to publish

If a suitable wheel exists and the corresponding version hasn't been published
to PyPI then exit with a return code of zero.

Wheel filename convention:
https://packaging.python.org/en/latest/specifications/binary-distribution-format/#file-name-convention
"""
from pathlib import Path
from subprocess import run

SUFFIX = "-py3-none-any.whl"
GLOB = f"dist/*{SUFFIX}"


def main() -> int:
    try:
        wheel = next(Path(".").glob(GLOB))
    except StopIteration:
        print(f"{GLOB=} not found")
        return 1
    name, _, version = wheel.name.removesuffix(SUFFIX).partition("-")
    args = ("pip", "index", "--pre", "versions", name)
    result = run(args, check=True, capture_output=True, text=True)
    print(f"{version=} {args=} {result.stdout=}")
    return int(f"{version}," in result.stdout)


if __name__ == "__main__":
    raise SystemExit(main())
