from clonetools import get_gists, get_repos
from argparse import ArgumentParser

def clone():
    parser = ArgumentParser()
    parser.add_argument("github_name")
    parser.add_argument("basedir_repos", nargs='?', default="")
    parser.add_argument("basedir_gists", nargs='?', default="")
    args = parser.parse_args()
    name = args.github_name
    basedir_repos = args.basedir_repos
    basedir_gists = args.basedir_gists
    
    get_repos(name, ask=False, basedir=basedir_repos)
    get_gists(name, ask=False, basedir=basedir_gists)
    
if __name__ == "__main__":
    clone()