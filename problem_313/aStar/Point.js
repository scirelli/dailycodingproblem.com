module.exports = class Point{
    constructor(x=0, y=0, z=0) {
        this._x = x;
        this._y = y;
        this._z = z;
    }

    get x() {
        return this._x;
    }
    get y() {
        return this._y;
    }
    get z() {
        return this._z;
    }

    set x(x) {
        this._x = x;
    }
    set y(y) {
        this._y = y;
    }
    set z(z) {
        this._z = z;
    }

    equal(p) {
        return this.x === p.x && this.y === p.y && this.z === p.z;
    }

    toString() {
        return `(${this.x}, ${this.y}, ${this.z})`;
    }

    clone() {
        return new Point(this.x, this.y, this.z);
    }

    copy(p) {
        this.x = p.x || 0;
        this.y = p.y || 0;
        this.z = p.z || 0;
        return this;
    }
};
