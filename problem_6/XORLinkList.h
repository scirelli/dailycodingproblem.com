#ifndef XORLinkList_H_
#define XORLinkList_H_

#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    char *name;
    unsigned long both;
} Node;

typedef struct List{
    Node* head;
    Node* tail;
    unsigned int length;
} List;

unsigned int xorll_add(List * const list, Node * const node);
unsigned int xorll_insertHead(List * const list, Node * const node);
unsigned int xorll_insert(List * const list, Node * const node, unsigned int index);
unsigned int xorll_remove(List * const list, unsigned int index);
Node* xorll_get(List * const list, unsigned int index);
void xorll_printNode(const Node * const node);
void xorll_printList(const List * const list);

#endif
