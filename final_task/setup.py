from setuptools import setup, find_packages

setup(
   name='pycalc_1',
   version='1.0',
   description='Pure-python command-line calculator.',
   author='Aliaksandr Serada',
   author_email='alsereda1992.com',
   packages=find_packages(),
   py_modules=['pycalc'],
   entry_points={'console_scripts': ['pycalc = pycalc.pycalc:main', ], },
   platforms='any',
)
