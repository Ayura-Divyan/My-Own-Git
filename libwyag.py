#Importing Libraries

import argparse
import configparser
from datetime import datetime
import grp,pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re 
import sys
import zlib

argparser = argparse.ArgumentParser(description="Wyag - Write Your Apps in Git")
