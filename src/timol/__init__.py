import pathlib

from .cli import bmark, cli

package_dir = pathlib.Path(__file__).resolve().parent  # src/timol
pycache_dir = package_dir / "__pycache__"

if not pycache_dir.exists():
    print(
        "Timol is running for the first time: startup time will be slow due to bytecode compilation."
    )
