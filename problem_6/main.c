#include <stdio.h>
#include <stdlib.h>
#include "XORLinkList.h"

int main(int argc, char *argv[]) {
    List list;
    Node a, b, c, d;
   
    a.name = "a";
    b.name = "b";
    c.name = "c";
    d.name = "d";

    xorll_add(&list, &a);
    xorll_add(&list, &b);
    xorll_add(&list, &c);
    xorll_add(&list, &d);
    printf("Forward Once\n");
    xorll_printList(&list);
    printf("Forward Twice\n");
    xorll_printList(&list);
    printf("Get 0\n");
    xorll_printNode(xorll_get(&list, 0));
    printf("Get 1\n");
    xorll_printNode(xorll_get(&list, 1));
    printf("Get 2\n");
    xorll_printNode(xorll_get(&list, 2));
    printf("Get 3\n");
    xorll_printNode(xorll_get(&list, 3));
    printf("Get 4\n");
    xorll_printNode(xorll_get(&list, 4));

    printf("Reverse it\n");
    list.head = &d;
    list.tail = &a;
    xorll_printList(&list);

    return EXIT_SUCCESS;
}

/*

3210

&a = 1001  0x9
&b = 0110  0x6
&c = 1010  0xA
^           
--------------
        0101  0x5

a.both = (0x0 ^ &b ) = 0x6
b.both = (&a  ^ &c ) = 0x3
c.both = (&b  ^ 0x0) = 0x6

node = 0x7ffeefbfefb8
list->head->both = 0x7ffeefbfefb8
*/
