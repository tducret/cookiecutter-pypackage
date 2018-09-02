# -*- coding: utf-8 -*-

"""CLI tool for {{cookiecutter.project_slug}}"""
import sys
import click
import {{cookiecutter.project_slug}}

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
def main(param1, defaultparam2):
    """ Example main """


if __name__ == "__main__":
    main()
