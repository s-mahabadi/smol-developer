from setuptools import setup, find_packages

# Package meta-data.
NAME = 'smol_dev'
DESCRIPTION = 'the first library to let you embed a developer agent in your own app!'
URL = 'https://github.com/smol-ai/developer'
EMAIL = 'morph@example.com'
AUTHOR = 'morph'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.0.1'

# README.md
long_description = ''
with open('readme.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
  name=NAME,
  version=VERSION,
  packages=find_packages(exclude=['dist', 'examples', 'v0', 'devcontainer', '__pycache__']),
  # install_requires=[
  #   # Add your package dependencies here
  # ],
  # entry_points={
  #   'console_scripts': [
  #     # Add your command line scripts here
  #   ],
  # },
  author=AUTHOR,
  author_email=EMAIL,
  description=DESCRIPTION,
  long_description=long_description,
  long_description_content_type='text/markdown',
  url=URL,
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires=REQUIRES_PYTHON,
)