from setuptools import find_packages
from setuptools import setup

setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    install_requires=[
# XXX Matplotlib requires numpy, install via pip install -r requirements.txt
        'matplotlib',
    ],
    name='plone_matplotlib',
    packages=find_packages(),
)
