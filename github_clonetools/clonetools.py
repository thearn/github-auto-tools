import urllib, json, os
from default_files import gitignore, wingproj, license, readme, setupfile

def get_default_files(name,desc):
    """
    General default files
    """
    defaultfiles = [['.gitignore', gitignore()],
                    ['README.md', readme(name, desc)],
                    ['LICENSE.txt', license()]]
    return defaultfiles

def get_default_py_files(name,desc,url):
    """
    Python - specific default files
    """
    defaultfiles = [['setup.py', setupfile(name, url, desc)],
                    ['%s.wpr' % name, wingproj()]]
    return defaultfiles

#make a source directory for setup.py to point to
make_src_dir = True

def prep_directory(basedir):
    if not os.path.exists(basedir):
        os.mkdir(basedir)

def writefile(fpath,data):
    f = open(fpath, 'wb')
    f.write(data)
    f.close()
    
def write_default_files(dpath, name, desc, url):

    if os.path.exists(dpath):
        onlyfiles = [ f for f in os.listdir(dpath) 
                      if os.path.isfile(os.path.join(dpath,f)) ]
        if len(onlyfiles) > 0:
            return #only add defaults if repo is empty
        print "Empty repo - adding default files..."
        files = get_default_files(name, desc)
        if "python" in desc.lower():
            files = files + get_default_py_files(name,desc,url)
            if make_src_dir:
                srcdir = dpath+'/src'
                os.mkdir(srcdir)
                writefile(srcdir+'/__init__.py', '')
        for fname, data in files:
            fn = '/'.join([dpath, fname])
            writefile(fn, data)

def process(cmd,name,fpath, ask, desc, url, typ = "repo"):
    if ask:
        print "Clone %s ?" % name
        resp = raw_input("(yes or no): ")
        #faster: [enter] for "yes", [space] + [enter] for "no"
        if resp == "no" or resp == " ":
            return
    os.system(cmd)
    if typ == "repo":
        write_default_files(fpath,name, desc, url)

def get_gists(uname, ask = False, basedir = ''):
    print
    print "Cloning gists from %s..." % uname
    print
    gists = urllib.urlopen("https://api.github.com/users/%s/gists" % uname)
    wingfn = 'gists.wpr'
    if basedir:
        prep_directory(basedir)
    for item in json.loads(gists.readlines()[0]):
        name= '-'.join(item['files'].keys()[-1].split('.'))
        if basedir:
            fpath = '/'.join([basedir, name])
        else:
            fpath = name
        if os.path.exists(fpath): #already cloned
            continue
        desc = item['description']
        idn = item['id']
        url = item['html_url']
        cmd = "git clone git@gist.github.com:%s.git %s" % (idn, fpath)
        process(cmd, name, fpath, ask, desc, url,typ="gist")
        print
    
def get_repos(uname, ask = False, basedir = ''):
    print
    print "Cloning repos from %s..." % uname
    print
    gists = urllib.urlopen("https://api.github.com/users/%s/repos" % uname)
    if basedir:
        prep_directory(basedir)
    for item in json.loads(gists.readlines()[0]):
        name= item['full_name']
        if basedir:
            fpath = '/'.join([basedir, item['name']])
        else:
            fpath = item['name']
        if os.path.exists(fpath):
            continue
        cmd = "git clone git@github.com:%s.git %s" % (name, fpath)
        desc = item['description']
        url = item['html_url']
        process(cmd, item['name'], fpath, ask, desc,url, typ="repo")
        print
        