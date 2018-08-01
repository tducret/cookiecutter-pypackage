# -*- coding: utf-8 -*-

"""CLI tool for {{cookiecutter.project_slug}}."""
import sys
import click
from {{cookiecutter.project_slug}} import __version__

# Usage : {{cookiecutter.project_slug}}_cli.py --help

@click.command()
@click.option(
    '--param1', '-p',
    envvar="PARAM1",
    type=str,
    help='example string param (or set the env var PARAM1)',
)
@click.option(
    '--defaultparam2', '-d',
    type=str,
    help='example param with default value',
    default='fr'
)
@click.version_option(
    version=__version__,
    message='%(prog)s, based on [{{cookiecutter.project_slug}}] package version %(version)s'
)
def main(param1, defaultparam2):
    """ Example main """


if __name__ == "__main__":
    main()
