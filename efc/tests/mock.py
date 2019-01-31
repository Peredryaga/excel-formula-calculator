# coding: utf8

from __future__ import unicode_literals, print_function
from efc.interface import BaseExcelInterface
from efc.rpn.errors import EFCLinkError, EFCNameError
from efc.rpn.operands import SingleCellOperand


class ExcelMock(BaseExcelInterface):
    data = {
        'Sheet 1': {
            1: {1: 13, 2: 16, 3: 18},
            3: {1: 4, 2: 2, 3: 8},
        },
        'Yet another sheet': {
            100: {1: 4, 2: 2, 3: 8},
            104: {1: 4, 2: 2, 3: 8, 27: 45},
        },
        'Sheet4': {
            1: {1: 13, 2: 16, 3: 18},
            2: {1: 13, 2: 16, 3: 18},
            3: {1: 4, 2: 2, 3: 8},
        },
    }

    named_ranges = {
        'test': [(1, 1), (2, 2)],
        'test2': [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
    }

    def cell_to_value(self, row, column, ws_name):
        if ws_name not in self.data:
            raise EFCLinkError(ws_name)

        return self.data[ws_name].get(row, {}).get(column)

    def named_range_to_cells(self, range_name, ws_name):
        if ws_name not in self.data:
            raise EFCLinkError(ws_name)

        named_ranges = {
            'test': SingleCellOperand(1, 2, ws_name='Sheet 1', source=self),
            'test2': [SingleCellOperand(1, 2, ws_name='Sheet 1', source=self),
                      SingleCellOperand(1, 3, ws_name='Sheet 1', source=self)]
        }
        if range_name not in named_ranges:
            raise EFCNameError(ws_name)

        return named_ranges[range_name]
