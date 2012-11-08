#! /usr/bin/env python

from setuptools import setup, find_packages
import dojoforms

setup(
    name="dojoforms",
    version=dojoforms.__version__,
    description="Dojo forms and widgets for Django",
    author="Mike Kibbel",
    author_email="mkibbel@gmail.com",
    license="BSD License",
    platforms=["OS Independent"],
    install_requires=[
        "Django>=1.4",
        "django-dojo=0.0.1",
    ],
    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    zip_safe=False,
)
