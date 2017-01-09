"""Installation script for proselint."""

from setuptools import setup, find_packages
from proselint.version import __version__

base_url = 'http://github.com/mcarthurgill/proselint'

setup(
    name='proselint',
    version=__version__,
    description='A linter for prose',
    url=base_url,
    download_url=base_url,
    author='Amperser Labs',
    author_email='hello@amperser.com',
    license='BSD',
    packages=find_packages(),
    package_data={'': ['demo.md', '.proselintrc']},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'proselint = proselint.command_line:proselint',
        ],
    },
    install_requires=[
        'click',
        'future',
        'six'
    ])
