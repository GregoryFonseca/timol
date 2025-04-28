import pathlib

package_dir = pathlib.Path(__file__).resolve().parent  # src/timol
flag_file = package_dir / ".initialized"
if not flag_file.exists():
    try:
        flag_file.write_bytes(b"1")
        print(
            "Timol is running for the first time: startup time might be slower due to bytecode compilation and initialization"
        )
    except OSError:
        # Not writeable or smth, so we just don't say anything
        # It is what it is
        pass

from .cli import bmark, cli
