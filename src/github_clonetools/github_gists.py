from clonetools import get_gists
from argparse import ArgumentParser

def clone():
    parser = ArgumentParser()
    parser.add_argument("github_name")
    parser.add_argument("basedir", nargs='?', default="")
    args = parser.parse_args()
    name = args.github_name
    basedir = args.basedir
    get_gists(name, ask=False, basedir=basedir)
    
if __name__ == "__main__":
    clone()