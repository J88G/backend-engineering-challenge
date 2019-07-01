"""Helper Functions"""
import json
from datetime import datetime
from json.decoder import JSONDecodeError  # pylint: disable=ungrouped-imports

import click
import oyaml
import pandas
from prettytable import PrettyTable
from prettytable.prettytable import PLAIN_COLUMNS

from .defaults import DATE_FORMAT, FREQUENCY, JSON, TABLE, YAML, REQUIRED_FIELDS
from .exceptions import InvalidDataFormatError, JsonDecoderError


def average(input_file, window_size):
    """
    :param input_file:
    :param window_size:
    :return:
    """

    _data = _get_data(input_file)
    data = pandas.DataFrame(sorted(_data, key=lambda i: datetime.strptime(i['timestamp'],
                                                                          DATE_FORMAT + '.%f'),
                                   reverse=False))

    # create field timestamp
    data['timestamp'] = pandas.to_datetime(data.timestamp)

    # set field timestamp as index
    data = data.set_index('timestamp')

    # get min and max values
    _start = data.index.min().floor('min')
    _end = data.index.max().ceil('min')

    data = data[['duration']].resample('min', label='right', closed='left').mean()
    data = data.reindex(pandas.date_range(_start, _end, freq=FREQUENCY).rename('date'))

    data['average_delivery_time'] = data[['duration']].rolling(window_size,
                                                               min_periods=1).mean().round(2)
    data = data[['average_delivery_time']]
    data = data.fillna(0)
    data = data.reset_index()

    data['date'] = data['date'].dt.strftime(DATE_FORMAT)

    return data.to_dict(orient='records')


def pretty_table(data):
    """
    Build and prettify table output
    :param data: Structured data
    :return:
    """
    table = PrettyTable()

    table.field_names = [header.upper() for header in data[0].keys()]

    for row in data:
        table.add_row(list(value for value in row.values()))

    table.set_style(PLAIN_COLUMNS)
    table.align = 'l'
    table.right_padding_width = 10

    return table


def _get_data(input_file):
    try:
        _data = [json.loads(_validate_data(line)) for line in open(input_file, 'r')]
    except JSONDecodeError:
        raise JsonDecoderError
    if _data:
        return _data
    raise InvalidDataFormatError


def _validate_data(item):
    for field in REQUIRED_FIELDS:
        if field not in item:
            raise InvalidDataFormatError(
                'Item {}, is missing the required_field {}'.format(item, field))
    return item


def _display_data(data, output):
    if output == JSON:
        for line in data:
            click.echo(line)

    if output == TABLE:
        click.echo(pretty_table(data))

    if output == YAML:
        click.echo(oyaml.safe_dump(data, default_flow_style=False))
