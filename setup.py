#!/usr/bin/env python
from setuptools import setup, find_packages
from eclingo.control import __version__

setup(
    version = __version__,
    name = 'eclingo',
    description = 'System to solve epistemic logic programs.',
    author = 'Jorge Fandinno & Javier Garea',
    license = 'MIT',
    packages = find_packages(include=['eclingo', 'eclingo.*']),
    test_suite = 'tests',
    zip_safe = False,
    entry_points = {
        'console_scripts': [
            'eclingo=eclingo:main',
        ]
    },
    python_requires='>=3.8',
)
