from pyalge import Case, of
from nodes import *


def get_indent(level):
    return ''.join([' '] * level * 4)

class Repr(Case):

    @of('ArrayNode(data, owners)')
    def array_node(self, data, owners):
        level = self.state['level']
        return '{0}ArrayNode: \n{1}'.format(get_indent(level),
            str(Repr(data, state={'level':level+1})))

    @of('ArrayDataNode(array_data)')
    def array_data_node(self, array_data):
        level = self.state['level']
        return '{0}array_data: {1}\n'.format(get_indent(level), str(array_data))

    @of('VariableDataNode(name)')
    def variable_data_node(self, name):
        level = self.state['level']
        return '{0}variable_data: {1}\n'.format(get_indent(level), name)

    @of('ScalarNode(value)')
    def scalar_node(self, value):
        level = self.state['level']
        return '{0}ScalarNode: {1}\n'.format(get_indent(level), str(value))

    @of('UnaryOperation(operand, op_str)')
    def unary_operation(self, operand, op_str):
        level = self.state['level']
        return '{0}UnaryOperation: {1}\n{2}\n'.format(get_indent(level),
            op_str,
            Repr(operand, state={'level':level+1}))

    @of('BinaryOperation(lhs, rhs, op_str)')
    def binary_operation(self, lhs, rhs, op_str):
        level = self.state['level']
        return '{0}BinaryOperation: {1}\n{2}\n{3}\n'.format(get_indent(level),
            op_str,
            Repr(lhs, state={'level':level+1}),
            Repr(rhs, state={'level':level+1}))

    @of('ArrayAssignOperation(operand, key, value)')
    def array_assign_operation(self, operand, key, value):
        level = self.state['level']
        return '{0}ArrayAssignOperation: \n{1}\n{2}\n'.format(get_indent(level),
            Repr(key, state={'level':level+1}),
            Repr(value, state={'level':level+1}))

    @of('WhereOperation(cond, left, right)')
    def where_operation(self, cond, left, right):
        level = self.state['level']
        return '{0}WhereOperation: \n{1}\n{2}\n{3}\n'.format(get_indent(level),
            Repr(cond, state={'level':level+1}),
            Repr(left, state={'level':level+1}),
            Repr(right, state={'level':level+1}))

    @of('UFuncNode(ufunc, args)')
    def ufunc_node(self, ufunc, args):
        level = self.state['level']
        ufunc_str = '{0}UFuncNode: \n'.format(get_indent(level))
        for arg in args:
            ufunc_str = '{0}{1}\n'.format(ufunc_str, Repr(arg, state={'level':level+1}))
        return ufunc_str