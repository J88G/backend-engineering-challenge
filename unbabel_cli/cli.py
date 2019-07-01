"""
Main CLI
"""
import click
from .defaults import EXPORT_FORMATS, DEFAULT_FORMAT, HELP_INPUT_FILE,\
    HELP_WINDOW_SIZE, HELP_FORMAT, VERSION_OUTPUT, UNBABEL_CLI_VERSION
from .helpers import average, _display_data


@click.command()
@click.option('--input_file', '-i', type=click.Path(exists=True, allow_dash=True),
              help=HELP_INPUT_FILE, required=True)
@click.option('--window_size', '-w', required=True, type=int, help=HELP_WINDOW_SIZE)
@click.option('--output', '-o', type=click.Choice(EXPORT_FORMATS), default=DEFAULT_FORMAT,
              required=False, help=HELP_FORMAT)
@click.version_option(version=UNBABEL_CLI_VERSION, message=VERSION_OUTPUT)
def cli(input_file, window_size, output):
    """
    :param input_file: Path to json file
    :param window_size: integer
    :param output: [json, table, yaml]
    :return:
    """
    data = average(input_file, window_size)
    _display_data(data, output)
