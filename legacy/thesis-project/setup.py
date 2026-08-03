#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for APA 7 Converter
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = (this_directory / "requirements.txt").read_text(encoding='utf-8').splitlines()
requirements = [r.strip() for r in requirements if r.strip() and not r.startswith('#')]

setup(
    name='apa7-converter',
    version='2.0.0',
    description='Convertidor de Markdown a DOCX con formato APA 7 profesional',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Claude',
    author_email='noreply@anthropic.com',
    url='https://github.com/yourusername/apa7-converter',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'flake8>=5.0.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'apa-converter=cli:cli',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Markup',
        'Topic :: Office/Business',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    keywords='apa apa7 markdown docx converter academic research thesis',
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/apa7-converter/issues',
        'Source': 'https://github.com/yourusername/apa7-converter',
        'Documentation': 'https://github.com/yourusername/apa7-converter/docs',
    },
)
