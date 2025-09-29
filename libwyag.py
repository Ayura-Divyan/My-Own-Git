# Importing Libraries

import argparse # To parse command line arguments
import configparser # To handle configuration files
from datetime import datetime # To handle date and time
import grp,pwd # To read the users/group database on Unix
from fnmatch import fnmatch # Filename matching 
import hashlib # To use SHA-1 hashing algorithm
from math import ceil # Just for one function
import os # For file directory operations
import re # Regular expressions
import sys # TO access command line arguments
import zlib # For compression

# Setting up Argument Parser
argparser = argparse.ArgumentParser(description="Wyag - Write Your Apps in Git")


# Handling Subcommands (like init, add, commit, etc.)
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True

# Function for subcommands
def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add":
            cmd_add(args)
        case "cat-file":
            cmd_cat_file(args)
        case "check-ignore":
            cmd_check_ignore(args)
        case "checkout":
            cmd_checkout(args)
        case "commit":
            cmd_commit(args)
        case "hash-object":
            cmd_hash_object(args)
        case "init":
            cmd_init(args)
        case "log":
            cmd_log(args)
        case "ls-files":
            cmd_ls_files(args)
        case "ls-tree":
            cmd_ls_tree(args)
        case "rev-parse":
            cmd_rev_parse(args)
        case "rm":
            cmd_rm(args)
        case "show-ref":
            cmd_show_ref(args)
        case "status":
            cmd_status(args)
        case "tag":
            cmd_tag(args)
        case _:
            print("Bad command.")

