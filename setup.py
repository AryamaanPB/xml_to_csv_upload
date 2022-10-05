from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'xml_to_csv', 'main', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='xml_to_csv',
    version=version['__version__'],
    description=('Download and Parse XML files, convert relevant tags to CSV and upload to an S3 bucket'),
    long_description=long_description,
    author='Aryamaan Pratap Singh',
    author_email='aryamaansingh13@gmail.com',
    url='https://github.com/AryamaanPB/xml_to_csv_upload',
    # license='MPL-2.0',
    packages=['xml_to_csv'],
#   no dependencies in this example
  install_requires=[
      'pandas >= 1.3.0',
  ],
#   no scripts in this example
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[
        'Development Status :: Production/Stable',
        'Intended Audience :: Recruiter',
        'Programming Language :: Python :: 3.10'],
    )