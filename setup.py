from setuptools import setup

# reading long description from file
with open('app/Readme.md', 'r') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests', 'pandas', 'os']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

# calling the setup function
setup(name='mygmap',
      version='1.0.0',
      description='Test push of the King Scripts',
      long_description=long_description,
      url='https://github.com/kingoperating/v2',
      author='Nikhil Kumar Singh',
      author_email='mtanner@kingoperating.com',
      license='MIT',
      packages=['geo'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='maps location address'
      )
