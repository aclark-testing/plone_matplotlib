from setuptools import find_packages
from setuptools import setup

setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    name='plone_matplotlib',
    packages=find_packages(),
)
