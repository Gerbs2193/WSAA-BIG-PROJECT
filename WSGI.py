import sys
import os

path = '/home/ger2193gerbs/WSAA-BIG-PROJECT'
if path not in sys.path:
    sys.path.append(path)

from server import app as application