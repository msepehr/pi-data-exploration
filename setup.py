# coding: utf-8

"""
	Copyright 2018 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	  <http://www.apache.org/licenses/LICENSE-2.0>
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""

from setuptools import setup, find_packages

NAME = "pidataexploration"
VERSION = "0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["six >= 1.10", "requests", "requests-kerberos", "pandas>=0.20.3", "setuptools >= 21.0.0"]

setup(
    name=NAME,
    version=VERSION,
    description="Data Exploration for PI System (2018)",
    url="https://github.com/msepehr/pi-data-exploration",
    keywords=["PI Web API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    author='Mahyar Sepehr',
    author_email='mahyar.sepehr@gmail.com',
    classifiers=[
        'Development Status :: 1 - Development/Alpha'
    ],
    long_description="""\
    Data Exploration for PI System (2018)
    """
)
