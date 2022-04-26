from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [           
          'requests>=2.25.1',
          'websocket-client<=0.57.0',
          'yapf>=0.30.0'
]

setup(
  name = 'Misty-SDK',
  packages = ['mistyPy'],
  version = '0.2.0',
  license='apache-2.0',
  description = 'Python SDK for Misty 2 Robots',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Misty Robotics',
  author_email = 'engineering.admin@mistyrobotics.com',
  url = 'https://www.mistyrobotics.com/',
  install_requires=requires,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
  ],
  project_urls={'Documentation': 'https://docs.mistyrobotics.com/',
  'Source': 'https://github.com/MistyCommunity/Python-SDK',
  },
  python_requires=">=3.8",
)