import os
import sys

cwd = os.getcwd()

if cwd not in sys.path:
    sys.path.append(cwd)

from startup.launcher import create_launcher

create_launcher(russian=True)