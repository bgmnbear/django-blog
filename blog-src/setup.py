# coding: utf-8

from setuptools import setup, find_packages

packages = find_packages('typeidea')
setup(
    name='typeidea',
    version='0.1',
    description='Blog System base on Django',
    author='whister',
    author_email='jasonwhister@gmail.com',
    url='https://bgmnbear.github.io/',
    packages=packages,
    package_dir={'': 'typeidea'},
    include_package_data=True,
    install_requires=[
        'django==1.11.29',
    ],
    scripts=[
        'typeidea/manage.py',
    ],
)
