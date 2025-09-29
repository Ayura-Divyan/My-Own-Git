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

#Setting up Argument Parser
argparser = argparse.ArgumentParser(description="Wyag - Write Your Apps in Git")


#Handling Subcommands (like init, add, commit, etc.)
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True
