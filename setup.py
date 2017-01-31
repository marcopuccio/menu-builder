import os
import sys

from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='menubuilder', 
      version=0.1, 
      description="""
      Create and Manange simple and dynamic menues for your site.      
      """,
      packages=find_packages(),
      include_package_data=True,
      license = 'MIT',
      install_requires=[
          'django==1.9.8',
      ],
      zip_safe=False,
      author='marcopuccio',
      url='https://github.com/marcopuccio/menu-builder',
      classifiers = [
          'Enviroment :: Web Enviroment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: MIT Licence',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
      ],
)
