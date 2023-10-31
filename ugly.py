
"""This is some ugly code."""

import os
import sys
import time
from functools import partial
import logging
import argparse
from collections import defaultdict
import subprocess
import multiprocessing


def get_args(): print("get_args")
def get_logger(): print("get_logger")
class B( object ) :
    def __init__(self) : print("B init")
    def __call__(self) : print("B call")
    def do_something(self) : print("B do_something") ; print("you can do that?")


