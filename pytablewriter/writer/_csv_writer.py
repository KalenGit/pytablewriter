# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import typepy

from .._const import FormatName
from ._text_writer import TextTableWriter


class CsvTableWriter(TextTableWriter):
    """
    A table writer class for character separated values format.
    The default separated character is a comma (``","``).

    :Examples:

        :ref:`example-csv-table-writer`
    """

    @property
    def format_name(self):
        return FormatName.CSV

    @property
    def support_split_write(self):
        return True

    def __init__(self):
        super(CsvTableWriter, self).__init__()

        self.indent_string = ""
        self.column_delimiter = ","
        self.is_padding = False
        self.is_write_header_separator_row = False
        self.is_write_null_line_after_table = False

        self._quote_flag_mapping[typepy.Typecode.NULL_STRING] = False
        self._is_remove_line_break = True

    def _write_header(self):
        if typepy.is_empty_sequence(self.header_list):
            return

        super(CsvTableWriter, self)._write_header()

    def _get_opening_row_item_list(self):
        return []

    def _get_value_row_separator_item_list(self):
        return []

    def _get_closing_row_item_list(self):
        return []
