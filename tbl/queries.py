from collections import namedtuple as NT
import copy

from tbl import tbl

class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

GT = NT("GT", ["lhs", "rhs"])
KEEP = NT("KEEP", ["lhs", "rhs"])
gt = Infix(lambda lhs, rhs: GT(lhs, rhs))

@Infix
def keep_rows_where (lhs, rhs):
    T = lhs
    # The LHS needs to be a tbl, the RHS 
    if not (type(T) is tbl):
        print("The left-hand side of |keep_rows_where| must be a tbl.")
    newT = copy.deepcopy(T)

    # Get the row index based on the field, which will be a Column() structure.
    col_index = T._get_column_index(rhs.lhs)

    # new_rows = list(filter(lambda r: r[col_index] > rhs.rhs, T.fields.rows ))
    new_rows = list()
    for r in T.fields.rows:
        # FIXME: I want to import values appropriately, and I want 
        # to have checking integrated somewhere up the chain so that 'gt' 
        # comparisons don't happen on the wrong types of data.
        if float(r[col_index]) > float(rhs.rhs):
            new_rows.append(r)

    newT._set_rows(new_rows)
    return newT