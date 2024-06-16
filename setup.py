from setuptools import setup
import os
import sys

if __name__ == '__main__':
    setup(name='SemanticQuantities',
          version='0.1.0',
          description="""
          A package that provides classes and utilities dealing with physical quantities, their units, uncertainty and bounds.
          """,
          url='https://andreacortis@bitbucket.org/neoncatdb/qi_project.git',
          author='Andrea Cortis',
          author_email='andrea.cortis@gmail.com',
          license='MIT',
          packages=['quantities'],
          include_package_data=True,
          zip_safe=False,
          install_requires=[
                            "Pint",
                            "uncertainties",
                            "typeguard",
                            "pyinterval"
                            ]
          )


