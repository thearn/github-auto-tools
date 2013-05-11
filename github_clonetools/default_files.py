def testfile(name):
    st = """
import unittest


class TestFunctions(unittest.TestCase):

    def test_main(self):
        pass

if __name__ == '__main__':
    unittest.main()
""" 
    return st

def setupfile(name,url,desc):
    st="""
from setuptools import setup, find_packages

setup(name='%s',
    version='0.1',
    install_requires=[],
    description="%s",
    author='Tristan Hearn',
    author_email='tristanhearn@gmail.com',
    url='%s',
    license='Apache 2.0',
    packages=['src'],
)
""" % (name, desc, url)
    return st

def license():
    st="""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
    return st

def gitignore():
    st= """
# logs #
########
*.openmdao_log.txt

# IDE #
#######
*.wpr
*.wpu

# Directories #
###############
build/
dist/
*.egg-info

# Compiled source #
###################
*.com
*.class
*.dll
*.exe
*.o
*.so
*.pyc

# Packages #
############
# it's better to unpack these files and commit the raw source
# git has its own built in compression methods
*.7z
*.dmg
*.gz
*.iso
*.jar
*.rar
*.tar
*.zip
*.egg

# Logs and databases #
######################
*.log
*.sql
*.sqlite

# OS generated files #
######################
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
Icon?
ehthumbs.db
Thumbs.db
"""
    return st

def wingproj():
    st= """
#!wing
#!version=4.0
##################################################################
# Wing IDE project file                                          #
##################################################################
[project attributes]
proj.directory-list = [{'dirloc': loc('.'),
                        'excludes': (),
                        'filter': '*',
                        'include_hidden': False,
                        'recursive': True,
                        'watch_for_changes': True}]
proj.file-type = 'shared'
"""
    return st

def readme(name,desc):
    st="""
%s
=======================
%s
    """ % (name, desc)
    return st
