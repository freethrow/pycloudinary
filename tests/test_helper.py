import os
import random

SUFFIX = os.environ.get('TRAVIS_JOB_ID') or random.randint(10000, 99999)
TEST_IMAGE = "tests/logo.png"
TEST_TAG = "pycloudinary_test"
UNIQUE_TAG = "{0}_{1}".format(TEST_TAG, SUFFIX)

def get_method(args):
    return args[0]

def get_uri(args):
    return args[1]

def get_params(args):
    return args[2] or {}
