#!/usr/bin/env python
from setuptools import setup, find_packages

version = '0.6'

LONG_DESCRIPTION = """
User accounts
--------------------------
"""

setup(
    name='django-logos',
    version=version,
    description="django-logos",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='logos,django',
    author='Lenin Yee',
    author_email='lenin.ayr@gmail.com',
    url='http://github.com/lenin/django-logos',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
