#!/usr/bin/env python3
import sys
from Node import Node


def test_not_equals_operator():
    v1 = Node(9, Node(9))
    v2 = Node(5, Node(2))

    assert v1 != v2, 'Lists that are not equal should return True'

    v1 = Node(9, Node(9))
    v2 = Node(9, Node(9))

    assert not v1 != v2, 'Lists that are equal should return False'  # pylint: disable=unneeded-not


def test_equals_operator():
    v1 = Node(5, Node(2))
    v2 = Node(5, Node(2))

    assert v1 == v2, 'Lists that are equal should return true'

    v1 = Node(5, Node(2))
    v2 = Node(5, Node(6))

    assert not v1 == v2, 'Lists that are not equal should return False'  # pylint: disable=unneeded-not


def test_str_operator():
    v1 = Node(5, Node(2, Node(3)))

    assert str(v1) == '5 -> 2 -> 3', 'Should return a string representation of the list.'


def test_add_operator():
    v1 = Node(9, Node(9))
    v2 = Node(5, Node(2))
    result = Node(4, Node(2, Node(1)))

    assert v1 + v2 == result, 'Add should add two or more lists'


def test_create_method():
    result = Node.create('1024')
    expected = Node(4, Node(2, Node(0, Node(1))))

    assert result == expected, 'Create method should create a list from a string.'


def test_commutation_of_add():
    n1 = Node.create('12345')
    n2 = Node.create('11111')

    result = n1 + n2
    result2 = n2 + n1

    assert result == result2, 'Addition should be commutative.'

    n1 = Node.create('99')
    n2 = Node.create('99999')

    result = n1 + n2
    result2 = n2 + n1

    assert result == result2, 'Addition should be commutative.'


def test_add_some_numbers():
    n1 = Node.create('99999999999999999999999999999999999999999999999999999999999999999999')
    n2 = Node.create('1')

    result = n1 + n2

    assert result.__str__('') == '000000000000000000000000000000000000000000000000000000000000000000001', 'Add should add large numbers.'

    n1 = Node.create('99999999999999999999999999999999999999999999999999999999999999999999')
    n2 = Node.create('99999999999999999999999999999999999999999999999999999999999999999999')

    result = n1 + n2
    assert result.__str__('') == '899999999999999999999999999999999999999999999999999999999999999999991', 'Add should add large numbers.'


if __name__ == '__main__':
    for n in list(sys.modules[__name__].__dict__):
        if n.startswith('test_'):
            try:
                sys.modules[__name__].__dict__[n]()
                print('.')
            except Exception as e:  # pylint: disable=broad-except
                print('f')
                print(e)
