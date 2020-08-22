module.exports = class Grid{
    static WALL = 0;
    static EMPTY = 1;
    static START = 2;
    static GOAL = 3;

    constructor(width, height, depth, fillType=Grid.EMPTY) {
        this.width = Number(width) || 1;
        this.height = Number(height) || 1;
        this.depth = Number(depth) || 1;
        this.grid = (new Array(this.width*this.height*this.depth)).fill(fillType);
        this.start = {x: 0, y: 0, z: 0};
        this.goal = {x: 0, y: 0, z: 0};
    }

    isValidCell(cell) {
        if(cell.x >= 0 && cell.x < this.width && cell.y >= 0 && cell.y < this.height && cell.z >= 0 && cell.z < this.depth) return true;
        return false;
    }

    get(loc) {
        return this.grid[this.pointToPos(loc)];
    }

    isType(loc, type) {
        return this.get(loc) === type;
    }

    isWall(loc) {
        if(!this.isValidCell(loc)) return true;
        return this.isType(loc, Grid.WALL);
    }

    isGoal(loc) {
        return this.isType(loc, Grid.GOAL);
    }

    isStart(loc) {
        return this.isType(loc, Grid.START);
    }

    isEmpty(loc) {
        return this.isType(loc, Grid.EMPTY);
    }

    pointToPos(p) {
        return p.x + p.y*this.width + p.z*this.height;
    }

    setLocationType(loc, type) {
        this.grid[this.pointToPos(loc)] = type;

        return this;
    }

    addType(list, type) {
        for(let loc of list) {
            this.setLocationType(loc, type);
        }

        return this;
    }

    addWalls(listOfWalls) {
        return this.addType(listOfWalls, Grid.WALL);
    }

    addGoal(loc) {
        this.goal.x = parseInt(loc.x);
        this.goal.y = parseInt(loc.y);
        this.goal.z = parseInt(loc.z);
        this.setLocationType(this.goal, Grid.GOAL);

        return this;
    }

    addStart(loc) {
        this.start.x = parseInt(loc.x);
        this.start.y = parseInt(loc.y);
        this.start.z = parseInt(loc.z);
        this.setLocationType(loc, Grid.START);

        return this;
    }
};
