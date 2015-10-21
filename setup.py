try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

print "================================================"
print find_packages()
print "================================================"


setup(
    name             = 'sensors',
    version          = '0.0.1',
    description      = 'A collection of sensor utilities for the Raspberry Pi',
    author           = 'Barton Satchwill',
    author_email     = 'barton.satchwill@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['Adafruit_BMP>=1.5.0'],
    dependency_links = ['https://github.com/adafruit/Adafruit_Python_BMP/tarball/master#egg=Adafruit-BMP-1.5.0'],
    tests_require    = ['nose'],
    packages         = find_packages(exclude=['docs', 'tests']),
    scripts          = ['bin/barometer']
)
