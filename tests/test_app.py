# !/usr/bin/python
# -*- coding: utf-8 -*-
"""testing the main"""
import unittest

from click.testing import CliRunner
from unbabel_cli.cli import cli
from unbabel_cli.defaults import UNBABEL_CLI_VERSION
from .results import RESULT_JSON, RESULT_TABLE, RESULT_YAML


class MainTest(unittest.TestCase):
    """the main test"""

    def test_help(self):
        """testing the help of the main"""
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])

        self.assertIn("-i, --input_file PATH", result.output)
        self.assertIn("-w, --window_size INTEGER", result.output)
        self.assertIn("-o, --output [json|table|yaml]", result.output)
        self.assertIn("--version", result.output)
        self.assertIn("--help", result.output)
        self.assertEqual(0, result.exit_code)

    def test_version(self):
        """testing the help of the main"""
        runner = CliRunner()
        result = runner.invoke(cli, ['--version'])

        self.assertIn(UNBABEL_CLI_VERSION, result.output)

    def test_input_file_not_ok(self):
        """testing the help of the main"""
        runner = CliRunner()
        result = runner.invoke(cli, ['--input_file'])
        self.assertIn('Error: --input_file option requires an argument', result.output)

    def test_windows_size_ok(self):
        """testing the help of the main"""
        runner = CliRunner()
        result = runner.invoke(cli, ['--window_size'])
        self.assertIn('Error: --window_size option requires an argument', result.output)

    def test_input_file_invalid_path(self):
        """testing the help of the main"""
        runner = CliRunner()
        result = runner.invoke(cli, ['--input_file', 'test_cases/does_not_exist.json'])
        self.assertIn('Invalid value for "--input_file" / "-i":'
                      ' Path "test_cases/does_not_exist.json" does not exist.\n', result.output)

    def test_ok(self):
        runner = CliRunner()
        result = runner.invoke(cli,
                               ['--input_file', 'test_cases/data_ok.json', '--window_size', '10'])

        self.assertEqual(RESULT_JSON, result.output)

    def test_ok_table(self):
        runner = CliRunner()
        result = runner.invoke(cli,
                               ['--input_file', 'test_cases/data_ok.json', '--window_size', '10',
                                '--output', 'table'])

        self.assertEqual(RESULT_TABLE, result.output)

    def test_ok_yaml(self):
        runner = CliRunner()
        result = runner.invoke(cli,
                               ['--input_file', 'test_cases/data_ok.json', '--window_size', '10',
                                '--output', 'yaml'])
        self.assertEqual(RESULT_YAML, result.output)

    def test_invalid_data_format(self):
        runner = CliRunner()
        result = runner.invoke(cli,
                               ['--input_file', 'test_cases/data_not_ok.json', '--window_size',
                                '10'])
        self.assertEqual('Error: Invalid Data Format\n', result.output)

    def test_invalid_json(self):
        runner = CliRunner()
        result = runner.invoke(cli,
                               ['--input_file', 'test_cases/data_not_ok_2.json', '--window_size',
                                '10'])
        self.assertEqual('Error: Item Hello this is just text, is missing'
                         ' the required_field event_name\n', result.output)


if __name__ == '__main__':
    unittest.main()
