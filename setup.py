from setuptools import setup
# run:
#   setup.py install
# or (if you'll be modifying the package):
#   setup.py develop
# To use a consistent encoding
# To upload to PyPI:
# twine upload dist/*
#
# Tag the release in github!
#

classifiers = [
    'Environment :: Console',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    'Topic :: Scientific/Engineering',
    ]

# aiohttp == 3.8.1
# aiobotocore==2.1.0
# botocore==1.23.24
# # 'botocore==1.23.24',  getting import error: 'is_valid_ipv6_endpoint_url' from 'botocore.endpoint' without this on lambda
install_requires = [
    'aiohttp',
    'aiobotocore',
    'aiohttp_cors',
    'aiofiles',
    'cryptography',
    'numcodecs',
    'numpy',
    'psutil',
    'pyjwt',
    'pytz',
    'pyyaml',
    'requests-unixsocket',
    'simplejson'
    ]


setup(name='hsds',
      version='0.7.0',
      description='HDF REST API',
      url='http://github.com/HDFGroup/hsds',
      author='John Readey',
      author_email='jreadey@hdfgrouup.org',
      license='Apache',
      packages=['hsds', 'hsds.util'],
      install_requires=install_requires,
      setup_requires=['setuptools'],
      extras_require={'azure': ['azure', 'azure-storage-blob']},
      zip_safe=False,
      classifiers=classifiers,
      data_files = [
        ('./config', ['admin/config/config.yml',]),
      ],
      entry_points={'console_scripts': [
          'hsds = hsds.app:main',
          'hsds-datanode = hsds.datanode:main',
          'hsds-servicenode = hsds.servicenode:main',
          'hsds-headnode = hsds.headnode:main',
          'hsds-rangeget = hsds.rangeget_proxy:main', 
          ]}
)
