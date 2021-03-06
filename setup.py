from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='charcoal',
    version='0.2.0',

    description='Opionionated high level StatsD client',
    long_description=long_description,

    url='https://github.com/cknv/charcoal',

    author='Esben Sonne',
    author_email='esbensonne+code@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=['charcoal'],
)
