module.exports = class Node{
    constructor(val, left, right) {
        this.val = val;
        this._left = left;
        this._right = right;
    }

    set left(l) {
        if(l instanceof Node) {
            this.left = l;
        }else{
            throw new Error('Must be type Node');
        }
    }

    get left() {
        return this._left;
    }

    set right(r) {
        if(r instanceof Node) {
            this._right = r;
        }else{
            throw new Error('Must be type Node');
        }

    }

    get right() {
        return this._left;
    }
};
