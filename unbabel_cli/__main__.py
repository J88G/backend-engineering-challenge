"""Main module"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
from unbabel_cli.cli import cli
from .exceptions import CLIException


def main():
    """Main entry-point"""
    try:
        cli()  # pylint: disable=no-value-for-parameter
    except CLIException as exc:
        click.echo(exc)


if __name__ == '__main__':
    main()
