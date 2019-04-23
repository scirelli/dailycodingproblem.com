#!/usr/bin/env python3


class Node():
    def __init__(self, radix=0, nextNode=None):
        self.radix = radix
        self.nextNode = nextNode

    @staticmethod
    def create(strValue):
        rtn = None
        rtnPtr = None

        if not isinstance(strValue, str):
            raise ValueError

        for v in strValue[::-1]:
            v = int(v)
            if rtnPtr:
                rtnPtr.nextNode = Node(v)
                rtnPtr = rtnPtr.nextNode
            else:
                rtnPtr = Node(v)
                rtn = rtnPtr
        return rtn

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.nextNode

    def __add__(self, node):
        node1 = self
        node2 = node
        rtn = None
        rtnPtr = None
        carry = 0
        nodeCont = None

        while node1 is not None and node2 is not None:
            v = node1.radix + node2.radix + carry
            v2 = v - 10
            carry = 1 if v2 >= 0 else 0
            v = v2 if v2 >= 0 else v

            if rtn is None:
                rtn = Node(v)
                rtnPtr = rtn
            else:
                rtnPtr.nextNode = Node(v)
                rtnPtr = rtnPtr.nextNode

            node1 = node1.nextNode
            node2 = node2.nextNode

        if node1 is not None:
            nodeCont = node1
        elif node2 is not None:
            nodeCont = node2

        while nodeCont is not None:
            v = nodeCont.radix + carry
            v2 = v - 10
            carry = 1 if v2 >= 0 else 0
            v = v2 if v2 >= 0 else v

            if rtn is None:
                rtn = Node(v)
                rtnPtr = rtn
            else:
                rtnPtr.nextNode = Node(v)
                rtnPtr = rtnPtr.nextNode

            nodeCont = nodeCont.nextNode

        if carry:
            rtnPtr.nextNode = Node(carry)
            rtnPtr = rtnPtr.nextNode

        return rtn

    def __eq__(self, node):
        v1 = self
        v2 = node

        while v1 is not None and v2 is not None:
            if v1.radix != v2.radix:
                return False
            v1 = v1.nextNode
            v2 = v2.nextNode

        if v1 is not None or v2 is not None:
            return False

        return True

    def __ne__(self, node):
        return not self == node

    def __str__(self, delim=' -> '):
        rtn = []
        for n in self:
            rtn.append(str(n.radix))
        return delim.join(rtn)
