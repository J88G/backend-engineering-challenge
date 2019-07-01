"""CLI Exceptions"""
from click import ClickException


class CLIException(ClickException):
    """ Common base class for all CLIexceptions. """
    pass  # pylint: disable=unnecessary-pass


class InvalidDataFormatError(CLIException):
    """ Invalid Data Format """
    exit_code = 1

    def __init__(self, message="Invalid Data Format"):
        super().__init__(message)


class JsonDecoderError(CLIException):
    """ Json Decoder Error """
    exit_code = 1

    def __init__(self, message="Ups, Json is invalid"):
        super().__init__(message)
