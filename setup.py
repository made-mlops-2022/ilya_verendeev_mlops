#!/usr/bin/env python
from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


def required():
    """Create list of requires to setup function"""
    with open('requirements.txt') as file:
        requires = file.read().splitlines()
    return requires


setup(
    name='Mlops-ml-deploy-made-iv',
    version='0.8',
    description='Mlops-ml-deploy-made-iv',
    long_description=readme(),
    url='https://github.com/Z5-05/mlops_made_2022/tree/hw01',
    author='iverendeev',
    install_requires=required(),
    author_email='ilaverendeev@gmail.com',
    license='MIT',
    packages=['src', 'tests'],
)
