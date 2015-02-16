import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

REQUIREMENTS = [
    'colander',
    'cornice',
    'pyfxa',
    'pyramid_multiauth',
    'redis',  # Session backend
    'requests',
    'six',
    'waitress',
]

POSTGRESQL_REQUIRES = [
    'psycopg2>2.5',
]

DEPENDENCY_LINKS = [
    'https://github.com/mozilla/PyFxA/tarball/master#egg=PyFxA-0.0.3dev',
]

ENTRY_POINTS = {
    'paste.app_factory': [
        'main = readinglist:main',
    ]}


setup(name='readinglist',
      version='0.3.dev0',
      description='readinglist',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Mozilla Services',
      author_email='services-dev@mozilla.com',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=REQUIREMENTS,
      extras_require={
        'postgresql': REQUIREMENTS + POSTGRESQL_REQUIRES,
      },
      dependency_links=DEPENDENCY_LINKS,
      entry_points=ENTRY_POINTS)
