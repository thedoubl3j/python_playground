try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jake Jackson',
    'url': 'URL to get the thing',
    'download_url': 'where to download it',
    'author_email': 'my_email@lol.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['homercoma'],
    'scripts': [],
    'name': 'homercoma'
}

setup(**config)