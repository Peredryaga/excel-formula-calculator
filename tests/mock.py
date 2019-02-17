# coding: utf8

from __future__ import unicode_literals, print_function
from efc.interface import BaseExcelInterface
from efc.rpn_builder.parser.operands import SingleCellOperand, CellSetOperand


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

    def cell_to_value(self, row, column, ws_name):
        return self.data[ws_name].get(row, {}).get(column)

    @property
    def named_ranges(self):
        op_set = CellSetOperand(ws_name='Sheet 1', source=self)
        op_set.add_row([SingleCellOperand(1, 2, ws_name='Sheet 1', source=self),
                        SingleCellOperand(1, 3, ws_name='Sheet 1', source=self)])
        return {
            'test': SingleCellOperand(1, 2, ws_name='Sheet 1', source=self),
            'test2': op_set
        }

    def named_range_to_cells(self, name, ws_name):
        return self.named_ranges[name]

    def is_ws_exists(self, ws_name):
        return ws_name in self.data

    def is_named_range_exists(self, name, ws):
        return name in self.named_ranges
