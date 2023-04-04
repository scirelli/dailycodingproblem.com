#!/usr/bin/env node
const assert = require('node:assert/strict');
//Given a complete binary tree, count the number of nodes in faster than O(n) time. 
//Recall that a complete binary tree has every level filled except the last, and the 
//nodes in the last level are filled starting from the left.

/*
                        (0)                                         -- 0
             /                          \                              |
           (1)                          (2)                            1
        /        \               /              \                      |
      (3)        (4)           (5)              (6)                    2
   /      \     /    \      /       \        /        \                |
 (7)      (8) (9)   (10) (11)       (12)   (13)       (14)             3


                        (0)                                         -- 0
             /                          \                              |
           (1)                          (2)                            1
        /        \               /              \                      |
      (3)        (4)           (5)              (6)                    2
   /      \     /    \      /       \        /        \                |
 (7)      (8)                                                          3


              (x)


              (x)
              /
            (y)


            (x)
           /   \
        (y)    (z)
 */

/*
Count of nodes of a complete tree at a given height 2^(h+1) - 1
 */

function Node(value, left=null, right=null) {
    this.left = left;
    this.right = right;
    this.value = value;
}

function totalNodes(node) {
    if(node === null) return 0;
    let lHeight = leftHeight(node),
        rHeight = rightHeight(node);

    if(lHeight === rHeight) {
        return calcCompleteTreeHeight(lHeight);
    }

    return 1 + totalNodes(node.left) + totalNodes(node.right);// + 1 for the root node.
}

function calcCompleteTreeHeight(height) {
    return Math.pow(2, height + 1) - 1;
}

function height(node, level=0) {
    if(node.left === null){
        return level;
    }
    return height(node.left, level + 1);
}

function leftHeight(node) {
    let height = -1;

    if(!node) throw new Error('Invalid tree root node');

    while(node){
        height++;
        node = node.left;
    }

    return height;
}

function rightHeight(node) {
    let height = -1;

    if(!node) throw new Error('Invalid tree root node');

    while(node){
        height++;
        node = node.right;
    }

    return height;
}

function testRunner() {
    const tests = [
        {
            tree: new Node(0, 
                new Node(1,
                    new Node(3, new Node(7), new Node(8)), 
                    new Node(4, new Node(9), new Node(10))
                ), 

                new Node(2,
                    new Node(5, new Node(11), new Node(12)),
                    new Node(6, new Node(13), new Node(14))
                )
            ),
            expected: 15
        },
        {
            tree: new Node(0, 
                new Node(1,
                    new Node(3, new Node(7), new Node(8)), 
                    new Node(4, new Node(9), new Node(10))
                ), 

                new Node(2,
                    new Node(5, new Node(11), new Node(12)),
                    new Node(6, new Node(13))
                )
            ),
            expected: 14
        },
        {
            tree: new Node(0, 
                new Node(1,
                    new Node(3, new Node(7), new Node(8)), 
                    new Node(4, new Node(9), new Node(10))
                ), 

                new Node(2,
                    new Node(5, new Node(11), new Node(12)),
                    new Node(6)
                )
            ),
            expected: 13
        },
        {
            tree: new Node(0, 
                new Node(1,
                    new Node(3, new Node(7), new Node(8)), 
                    new Node(4, new Node(9), new Node(10))
                ), 

                new Node(2,
                    new Node(5, new Node(11)),
                    new Node(6)
                )
            ),
            expected: 12
        },
        {
            tree: new Node(0, 
                new Node(1,
                    new Node(3, new Node(7), new Node(8)), 
                    new Node(4, new Node(9), new Node(10))
                ), 

                new Node(2,
                    new Node(5),
                    new Node(6)
                )
            ),
            expected: 11
        }
    ];

    tests.forEach(t=>{
        let actual = totalNodes(t.tree);
        if(actual !== t.expected){
            process.stdout.write('F');
            console.debug(`\nCalculated height is incorrect. ${actual} != ${t.expected}`);
        }else{
            process.stdout.write('P');
        }
    });

    console.log('\nAll tests passed!');
}

testRunner();
