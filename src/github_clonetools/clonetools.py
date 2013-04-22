import urllib, json, os
from default_files import gitignore, wingproj, license

def prep_directory(basedir):
    if not os.path.exists(basedir):
        os.mkdir(basedir)

def writefile(fpath,data):
    f = open(fpath, 'wb')
    f.write(data)
    f.close()
    
def write_default_files(dpath, name, desc, typ = "repo"):
    readme="""
%s
=======================
%s
    """ % (name, desc)
    if os.path.exists(dpath):
        writefile('/'.join([dpath, '%s.wpr' % name]), wingproj)
        
        fn_gitig = '/'.join([dpath, '.gitignore'])
        if not os.path.exists(fn_gitig):
            writefile(fn_gitig, gitignore)
            
        if typ != "repo":
            return
            
        fn_readme = '/'.join([dpath, 'README.md'])
        if not os.path.exists(fn_readme):
            writefile(fn_readme, readme)
            
        fn_license = '/'.join([dpath, 'LICENSE.txt'])
        if not os.path.exists(fn_license):
            writefile(fn_license, license)

def process(cmd,name,fpath, ask, desc, typ = "repo"):
    if ask:
        print "Clone %s ?" % name
        resp = raw_input("(yes or no): ")
        #faster: [enter] for "yes", [space] + [enter] for "no"
        if resp == "no" or resp == " ":
            return
    os.system(cmd)
    write_default_files(fpath,name, desc, typ = typ)

def get_gists(uname, ask = False, basedir = ''):
    print
    print "Cloning gists from %s..." % uname
    print
    gists = urllib.urlopen("https://api.github.com/users/%s/gists" % uname)
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
        cmd = "git clone git@gist.github.com:%s.git %s" % (idn, fpath)
        process(cmd, name, fpath, ask, desc, typ="gist")
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
        process(cmd, item['name'], fpath, ask, desc,typ="repo")

if __name__ == "__main__":
    get_gists("thearn", ask = True, basedir='gists')
    get_repos("thearn", ask = True, basedir='repos')