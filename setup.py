"""
Flask-Env
==============
"""
from setuptools import setup, find_packages


def get_long_description():
    with open('README.rst') as f:
        rv = f.read()
    return rv


setup(
    name='Flask-Env',
    version='1.0.0',
    url='https://github.com/brettlangdon/flask-env',
    license='MIT',
    author='Brett Langdon',
    author_email='me@brett.is',
    description='Easily set Flask settings from environment variables',
    long_description=get_long_description(),
    packages=find_packages(),
    zip_safe=True,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)