
github-clonetools
=======================
Python command line tool to clone all repos and gists from a single github account,
and populate empty new repos with a set of templated common default files.
    
# Installation:

Just run `python setup.py build install` as normal

# Usage:

The setup.py file installs three command line scripts into your python scripts directory.

- `clonerepos [username] [directory]` clones all github repos from github user 
`username` into directory `directory`. 
If no directory is given, the repos are cloned into the current working directory.
If a subdirectory already exists that matches the name of a repo, that repo is skipped. 

- `clonegists [username] [directory]` clones all github gists from github user 
`username` into directory `directory`. 
The directories are named according to the first file in a gist. If no directory is given, 
the repos are cloned into the current working directory.
If a subdirectory already exists that matches the name of a gist, that gist is skipped. 

- `cloneall [username] [repo directory] [gists directory]` clones all github 
repos and gists from github user `username` into directories `repo directory` 
and `gists directory`, respectively.
If no directories are given, all repos and gists are cloned into the current working directory.
If a subdirectory already exists that matches the name of a repo or gist, that repo or gist is skipped. 

# Empty repo behavior: 
When an empty repo is cloned using either the `clonerepos` or `cloneall` script,
the directory is automatically populated with a set of default files. These include:

- `.gitignore`
- `README.md`
- `LICENSE.txt`
- `setup.py`, pointing to a created `src/` directory
- `src/__init__.py`
- an empty Wing IDE project file

Each of these files can be templated with repo information using 
`github_clonetools/default_files.py`.
Individual default files can be added/removed to the script behavior by editing
the method `write_default_files` in `github_clonetools/clonetools.py`.