"""Default labels"""
UNBABEL_CLI_VERSION = 'v1.0.0'
VERSION_OUTPUT = '%(version)s'
HELP_INPUT_FILE = 'Path to the file containing the data to analyse'
HELP_WINDOW_SIZE = 'Window Size'
HELP_FORMAT = 'Output format'

JSON = 'json'
TABLE = 'table'
YAML = 'yaml'
DEFAULT_FORMAT = JSON
EXPORT_FORMATS = [JSON, TABLE, YAML]

FREQUENCY = '1min'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

REQUIRED_FIELDS = ['event_name', 'duration', 'timestamp']
