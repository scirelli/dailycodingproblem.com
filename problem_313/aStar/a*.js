/*
 * A* Path finding Algorithm
 *
 *    Sample algorithm:
 *    This is a fairly simple and easy-to-understand pathfinding algorithm for tile-based maps. To start off, you have a map, a start coordinate and a destination coordinate. The map will look like this, X being walls, S being the start, O being the finish and _ being open spaces, the numbers along the top and right edges are the column and row numbers:
 *
 *      1 2 3 4 5 6 7 8
 *    X X X X X X X X X X
 *    X _ _ _ X X _ X _ X 1
 *    X _ X _ _ X _ _ _ X 2
 *    X S X X _ _ _ X _ X 3
 *    X _ X _ _ X _ _ _ X 4
 *    X _ _ _ X X _ X _ X 5
 *    X _ X _ _ X _ X _ X 6
 *    X _ X X _ _ _ X _ X 7
 *    X _ _ O _ X _ _ _ X 8
 *    X X X X X X X X X X
 *    First, create a list of coordinates, which we will use as a queue. The queue will be initialized with one coordinate, the end coordinate. Each coordinate will also have a counter variable attached (the purpose of this will soon become evident). Thus, the queue starts off as ((3,8,0)).
 *
 *    Then, go through every element in the queue, including elements added to the end over the course of the algorithm, and to each element, do the following:
 *
 *    Create a list of the four adjacent cells, with a counter variable of the current element's counter variable + 1 (in our example, the four cells are ((2,8,1),(3,7,1),(4,8,1),(3,9,1)))
 *    Check all cells in each list for the following two conditions:
 *    If the cell is a wall, remove it from the list
 *    If there is an element in the main list with the same coordinate and a less than or equal counter, remove it from the cells list
 *    Add all remaining cells in the list to the end of the main list
 *    Go to the next item in the list
 *    Thus, after turn 1, the list of elements is this: ((3,8,0),(2,8,1),(4,8,1))
 *
 *    After 2 turns: ((3,8,0),(2,8,1),(4,8,1),(1,8,2),(4,7,2))
 *    After 3 turns: (...(1,7,3),(4,6,3),(5,7,3))
 *    After 4 turns: (...(1,6,4),(3,6,4),(6,7,4))
 *    After 5 turns: (...(1,5,5),(3,5,5),(6,6,5),(6,8,5))
 *    After 6 turns: (...(1,4,6),(2,5,6),(3,4,6),(6,5,6),(7,8,6))
 *    After 7 turns: (...(1,3,7)) – problem solved, end this stage of the algorithm – note that if you have multiple units chasing the same target (as in many games – the finish to start approach of the algorithm is intended to make this easier), you can continue until the entire map is taken up, all units are reached or a set counter limit is reached
 *    Now, map the counters onto the map, getting this:
 *
 *      1 2 3 4 5 6 7 8
 *    X X X X X X X X X X
 *    X _ _ _ X X _ X _ X 1
 *    X _ X _ _ X _ _ _ X 2
 *    X S X X _ _ _ X _ X 3
 *    X 6 X 6 _ X _ _ _ X 4
 *    X 5 6 5 X X 6 X _ X 5
 *    X 4 X 4 3 X 5 X _ X 6
 *    X 3 X X 2 3 4 X _ X 7
 *    X 2 1 0 1 X 5 6 _ X 8
 *    X X X X X X X X X X
 *    Now, start at S (7) and go to the nearby cell with the lowest number (unchecked cells cannot be moved to). The path traced is (1,3,7) -> (1,4,6) -> (1,5,5) -> (1,6,4) -> (1,7,3) -> (1,8,2) -> (2,8,1) -> (3,8,0). In the event that two numbers are equally low (for example, if S was at (2,5)), pick a random direction – the lengths are the same. The algorithm is now complete.
 *
 *
 * References:
 *    https://en.wikipedia.org/wiki/Pathfinding
 */
const Point = require('./Point'),
    Grid = require('./Grid');

const NOT_CHECKED = -1;

class A_Star{
    constructor(grid) {
        this.grid = null;
        this.setGrid(grid);
    }

    setGrid(g) {
        if(g instanceof Grid) {
            this.grid = g;
        }else{
            throw new Error('setGrid() parameter one must be of type Grid.');
        }
        return this;
    }

    findShortestPath(grid) {
        grid = grid || this.grid;
        let weightedCells = buildWeightCellList.call(this, grid),
            weightGrid = new Grid(grid.width, grid.height, grid.depth,  NOT_CHECKED);

        weightGrid.start = (new Point()).copy(grid.start);
        weightGrid.goal = (new Point()).copy(grid.goal);
        weightedCells.forEach((cell)=> {
            weightGrid.setLocationType(cell, cell.weight);
        });

        return walkShortestPath.call(this, weightGrid);
    }
}

function buildWeightCellList(grid) {
    let queue = [(new A_Star.WeightedPoint()).copy(grid.goal)], i = 0, curCell;

    while(i < queue.length) {
        curCell = queue[i];
        if(this.grid.isStart(curCell)) {
            break;
        }
        queue.push(...getAdjecentCellsList.call(this, curCell).filter((cell)=> {
            if(this.grid.isWall(cell)) {
                return false;
            }
            for(let qdCell of queue) {
                if(qdCell.equal(cell) && qdCell.weight <= cell.weight) {
                    return false;
                }
            }

            return true;
        }));
        i++;
    }
    return queue;
}

function getAdjecentCellsList(cell) {
    let weight = cell.weight + 1,
        above = new A_Star.WeightedPoint(cell.x, cell.y - 1, cell.z, weight),
        below = new A_Star.WeightedPoint(cell.x, cell.y + 1, cell.z, weight),
        left = new A_Star.WeightedPoint(cell.x - 1, cell.y, cell.z, weight),
        right= new A_Star.WeightedPoint(cell.x + 1, cell.y, cell.z, weight),
        back = new A_Star.WeightedPoint(cell.x, cell.y, cell.z + 1, weight),
        front = new A_Star.WeightedPoint(cell.x, cell.y, cell.z - 1, weight),
        cellList = [];

    if(this.grid.isValidCell(above)) {
        cellList.push(above);
    }
    if(this.grid.isValidCell(below)) {
        cellList.push(below);
    }
    if(this.grid.isValidCell(left)) {
        cellList.push(left);
    }
    if(this.grid.isValidCell(right)) {
        cellList.push(right);
    }
    if(this.grid.isValidCell(back)) {
        cellList.push(back);
    }
    if(this.grid.isValidCell(front)) {
        cellList.push(front);
    }

    return cellList;
}

function walkShortestPath(weightGrid) {
    let curCell = weightGrid.start, path=[new Point().copy(weightGrid.start)], adjCells, lowestWeight;

    while(!curCell.equal(weightGrid.goal)) {
        adjCells = getAdjecentCellsList.call(this, curCell).filter(c=>weightGrid.get(c)!==NOT_CHECKED);
        lowestWeight = adjCells.pop();
        adjCells.forEach((c)=>{
            if(weightGrid.get(c) < weightGrid.get(lowestWeight)) {
                lowestWeight = c;
            }
        });
        curCell = lowestWeight;
        path.push(new Point().copy(curCell));
        console.log(new Point().copy(curCell), weightGrid.get(curCell));
    }

    return path;
}

A_Star.Grid = Grid;
A_Star.WeightedPoint = class WeightedPoint{
    constructor(x, y, z, weight = 0) {
        this.point = new Point(x, y, z);
        this.weight = weight;
    }

    get x() {
        return this.point.x;
    }
    get y() {
        return this.point.y;
    }
    get z() {
        return this.point.z;
    }

    get weight() {
        return this._weight;
    }

    set x(x) {
        this.point.x = x;
    }
    set y(y) {
        this.point.y = y;
    }
    set z(z) {
        this.point.z = z;
    }

    set weight(w) {
        this._weight = w;
    }

    equal(p) {
        return this.point.equal(p);
    }

    toString() {
        return this.point.toString();
    }

    clone() {
        return new WeightedPoint(this.x, this.y, this.z, this.weight);
    }

    copy(p) {
        this.x = p.x || 0;
        this.y = p.y || 0;
        this.z = p.z || 0;
        this.weight = p.weight || 0;

        return this;
    }
};

module.exports = A_Star;
