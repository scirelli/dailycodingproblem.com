#!/usr/bin/env node
/*
 * You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order.
 * Each of these wheels rotate clockwise and counterclockwise.

 * In addition, the lock has a certain number of "dead ends", meaning that if you turn the wheels to one of
 * these combinations, the lock becomes stuck in that state and cannot be opened.

 * Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction. Given a lock
 * initially set to 000, a target combination, and a list of dead ends, write a function that returns the minimum
 * number of moves required to reach the target state, or None if this is impossible.
 */

/*
 * This is a 3D grid, 10x10x10. You are given a starting position with in the grid [0, 0 ,0], a goal position [x, y, z], and all the obstacles' positions.
 */
const WIDTH = 10,
    HEIGHT = 10,
    DEPTH = 10,
    WALL = 0,
    MARK = 0,
    OPEN = 1,
    GOAL = 2;

class Point{
    constructor(x=0, y=0, z=0) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}

function createField() {
    return (new Array(WIDTH*HEIGHT*DEPTH)).fill(OPEN);
}

function pointToPos(p, w=WIDTH, h=HEIGHT) {
    return p.x + p.y*w + p.z*h;
}

function insertObstacles(grid, obstacles) {
    obstacles.forEach((p)=>{
        grid[pointToPos(p)] = WALL;
    });

    return grid;
}

function insertGoal(grid, goal) {
    grid[pointToPos(goal)] = GOAL;
    return grid;
}

function moveRight(p) {
    return new Point(p.x+1, p.y, p.z);
}

function moveDown(p) {
    return new Point(p.x, p.y+1, p.z);
}

function moveLeft(p) {
    return new Point(p.x-1, p.y, p.z);
}

function moveUp(p) {
    return new Point(p.x, p.y-1, p.z);
}

function moveInto(p) {
    return new Point(p.x, p.y, p.z+1);
}

function moveOutOf(p) {
    return new Point(p.x, p.y, p.z-1);
}

function isValuePoint(p) {
    if( p.x < WIDTH && p.x >= 0 &&
        p.y < HEIGHT && p.y >= 0 &&
        p.z < DEPTH && p.z >= 0) return true;

    return false;
}

function isType(grid, p, type) {
    if(grid[pointToPos(p)] === type) return true;
    return false;
}

function isGoal(grid, p) {
    return isType(grid, p, GOAL);
}

function isWall(grid, p) {
    return isType(grid, p, WALL);
}

function findGoal(grid, pos, count, finalCount) {
    if(!isValuePoint(pos)) return;
    if(isWall(grid, pos)) return;
    if(finalCount.count) return;

    if(isGoal(grid, pos)) {
        finalCount.count = count;
        return;
    }

    grid = grid.slice();
    grid[pointToPos(pos)] = MARK;

    findGoal(grid, moveRight(pos), count+1, finalCount);
    findGoal(grid, moveDown(pos), count+1, finalCount);
    findGoal(grid, moveLeft(pos), count+1, finalCount);
    findGoal(grid, moveUp(pos), count+1, finalCount);
    findGoal(grid, moveInto(pos), count+1, finalCount);
    findGoal(grid, moveOutOf(pos), count+1, finalCount);

    return finalCount;
}

function main() {
    const testCases = [
        {
            /* 18
               1 1 1 1 1 1 1 1 1 1
               1 0 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 2
            */
            start:     new Point(),
            gameField: insertGoal(
                insertObstacles(
                    createField(),
                    [
                        new Point(1, 1, 0),
                        new Point(1, 1, 1)
                    ]
                ),
                new Point(9, 9, 0)
            )
        },
        {
            /* 19
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 1
               1 0 1 1 1 1 1 1 1 1  |  1 0 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 1
               1 1 1 1 1 1 1 1 1 1  |  1 1 1 1 1 1 1 1 1 2
            */
            start:     new Point(),
            gameField: insertGoal(
                insertObstacles(
                    createField(),
                    [
                        new Point(1, 1, 1),
                        new Point(1, 1, 0)
                    ]
                ),
                new Point(9, 9, 9)
            )
        }
    ];

    testCases.forEach((test)=> {
        console.log(findGoal(test.gameField, test.start, 0, {count: 0}));
    });
}

main();

