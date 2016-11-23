"""PyJam : a tool to retreive tracks from Jamendo and build a chart based on dowload figures.
"""

# Always prefer setuptools over distutils
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyJam',

    version='0.1.0',

    description='a tool to retreive tracks from Jamendo and build a chart based on dowload figures.',
    long_description=long_description,

    url='https://github.com/ymauray/pyjam',

    author='The French Guy from Switzerland',
    author_email='yannick@frenchguy.ch',

    license='GPLv3+',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Podcast publishers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],

    keywords='jamendo audio podcast',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    dependency_links = [
        'git+https://github.com/ymauray/ymatools.git'
    ],

    entry_points={
        'console_scripts': [
            'pyjam=pyjam:main',
        ],
    },
)
