import pathlib

package_dir = pathlib.Path(__file__).resolve().parent  # src/timol
pycache_dir = package_dir / "__pycache__"

num_cache_files = sum(1 for _ in pycache_dir.iterdir() if _.is_file())
if num_cache_files == 1:
    print(
        "Timol is running for the first time: startup time will be slow due to bytecode compilation."
    )

from .cli import bmark, cli
