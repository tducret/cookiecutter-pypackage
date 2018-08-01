#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
try:  # For pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # For pip <= 9
    from pip.req import parse_requirements


__version__ = {{ cookiecutter.version }}  # Should match with __init.py__
_GITHUB_URL = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo }}',
_KEYWORDS = ['api', {{ cookiecutter.project_slug }}, 'parsing',
              'python-wrapper', 'scraping', 'scraper', 'parser']
{% if cookiecutter.command_line_interface == 'y' -%}
_SCRIPTS = ['{{ cookiecutter.project_slug }}_cli.py']
# To delete here + 'scripts' dans setup()
# if no command is used in the package
{% endif %}

install_reqs = parse_requirements('requirements.txt', session='hack')
requirements = [str(ir.req) for ir in install_reqs]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(),
    package_data={},
{% if cookiecutter.command_line_interface == 'y' -%}
    scripts=_SCRIPTS,
{% endif %}
    version=__version__,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    platforms='Posix; MacOS X',
    description="{{ cookiecutter.project_short_description }}",
    long_description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url=_GITHUB_URL,
    download_url='{github_url}/tarball/{version}'.format(
                                                github_url=_GITHUB_URL,
                                                version=__version__),
    keywords=_KEYWORDS,
    setup_requires=requirements,
    install_requires=requirements,
    classifiers=[
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)
