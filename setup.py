from setuptools import setup, find_packages
import sys, os


setup(name='github_clonetools',
    version='',
    description="Command line tools to clone all github repos of a given account",
    long_description='',
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Tristan Hearn',
    author_email='tristanhearn@gmail.com',
    url='http://www.google.com',
    license='Apache 2.0',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts':
            ['cloneall=github_clonetools.github_all:clone',
             'clonerepos=github_clonetools.github_repo:clone',
             'clonegists=github_clonetools.github_gists:clone']
    }
)
