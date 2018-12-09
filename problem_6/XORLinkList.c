#include "XORLinkList.h"

unsigned int xorll_add(List * const list, Node * const node)
{
    Node *prev;

    if(node == NULL){
        return list->length;
    }

    if(list->head == NULL) {
        node->both = 0L;
        list->head = node;
        list->tail = node;
        list->length += 1;
        return list->length;
    }

    if(list->tail == NULL) {
        list->tail = list->head;
    }
    
    list->tail->both = list->tail->both ^ (unsigned long)node;
    prev = list->tail;
    list->tail = node;
    list->tail->both = (unsigned long)prev;
    
    list->length += 1;
    return list->length;
}

unsigned int xorll_insertHead(List * const list, Node * const node)
{
    Node *cur = list->head;

    cur->both = cur->both ^ (unsigned long)node;
    node->both = (unsigned long)cur;
    
    list->head = node;

    return ++list->length;
}

/*
    A <--> B <--> C <--> D
    ^      ^             ^
   head    |            tail
           | 
            -- B' insert

Insert at position 1 results in

    A <--> B' <--> B <--> C <--> D
    ^                            ^
   head                         tail
 */
unsigned int xorll_insert(List * const list, Node * const node, unsigned int index)
{
    Node *prev = 0L,
        *cur = list->head,
        *next = list->head;
    unsigned int position = 0;
    
    if(index >= list->length) {
        return xorll_add(list, node);
    }
    
    if(index == 0) {
        return xorll_insertHead(list, node);
    }

    while(cur != 0L) {
        if(position == index){
            if(prev != 0L){
                prev->both = (unsigned long)cur ^ prev->both ^ (unsigned long)node;
            }
           
            cur->both = (unsigned long)prev ^ cur->both ^ (unsigned long)node;
            node->both = (unsigned long)prev ^ (unsigned long)cur;
            
            if(index == 0) {
                list->head = node;
            }

            return ++list->length;
        }

        if(cur->both != 0L){
            next = (Node*)((unsigned long)prev ^ cur->both);
            prev = cur;
            cur = next;
            position++;
        }else{
            break;
        }
    }
    return 0;
}

/*
    A <--> B <--> C <--> D
    ^      ^             ^
   head    |            tail
           | 
            -- B remove

Remove at position 1 results in

    A <--> C <--> D
    ^             ^
   head          tail
 */
unsigned int xorll_remove(List * const list, unsigned int index)
{
    Node *prev = 0L,
        *cur = list->head,
        *next = list->head;
    unsigned int position = 0;
    
    if(index >= list->length) {
        return list->length;
    }
   
    if(index == 0){
        next = (Node*)((unsigned long)prev ^ cur->both);
        if(next != 0){
            next->both = (unsigned long)list->head ^ next->both;
        }
        list->head = next;
        return --list->length;
    }
    
    if(index == list->length-1){
        next = list->tail;
        list->tail = (Node*)list->tail->both;
        if(list->tail != 0){
            list->tail->both = list->tail->both ^ (unsigned long)next;
        }

        return --list->length;
    }

    while(cur != 0L) {
        if(position == index){
            if(prev != 0L){
                prev->both = (unsigned long)cur ^ prev->both ^ (unsigned long)next;
            }
           
            if(next != 0L){
                next->both = (unsigned long)cur ^ (unsigned long)next->both ^ (unsigned long)prev;
            }

            return --list->length;
        }

        if(cur->both != 0L){
            next = (Node*)((unsigned long)prev ^ cur->both);
            prev = cur;
            cur = next;
            next = (Node*)((unsigned long)prev ^ cur->both);
            position++;
        }else{
            break;
        }
    }
    return 0;
}

Node* xorll_get(List * const list, unsigned int index)
{
    Node *prev = 0L,
        *cur = list->head,
        *next = list->head;
    unsigned int count = 0;
    
    if(index >= list->length) return NULL;

    while(cur != 0L) {
        if(count == index) return cur;
        count++;
        if(cur->both != 0L){
            next = (Node*)((unsigned long)prev ^ cur->both);
            prev = cur;
            cur = next;
        }else{
            break;
        }
    }
    return NULL;
}

void xorll_printNode(const Node * const node)
{
    if(node == NULL){
        printf("Invalid node.\n");
        return;
    }
    printf("%s = %p, both = 0x%lx\n", node->name, node, node->both);
}

void xorll_printList(const List * const list)
{
    Node *prev = 0L,
        *cur = list->head,
        *next = list->head;
    
    while(cur != 0L) {
        xorll_printNode(cur);
        if(cur->both != 0L){
            next = (Node*)((unsigned long)prev ^ cur->both);
            prev = cur;
            cur = next;
        }else{
            break;
        }
    }
}
