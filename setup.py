from setuptools import setup, find_packages
import sys, os


setup(name='github_clonetools',
    version='0.1',
    description="Command line tools to clone all github repos of a given account",
    author='Tristan Hearn',
    author_email='tristanhearn@gmail.com',
    url='http://www.google.com',
    license='Apache 2.0',
    packages=['github_clonetools'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts':
            ['cloneall=github_clonetools.github_all:clone',
             'clonerepos=github_clonetools.github_repo:clone',
             'clonegists=github_clonetools.github_gists:clone']
    }
)
