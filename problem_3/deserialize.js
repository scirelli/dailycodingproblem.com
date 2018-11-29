const Node = require('Node');

module.exports = {
    cheap:       JSON.parse,
    deserialize: deserialize
};

function deserialize(str) {
    let stack = [],
        index = -1, c;

    return parseNode();

    function parseNode() {
        while((c = str.charAt(++index))) {
            switch(c) {
                case '(':
                    index++;
                    parseWhiteSpace();
                    stack.push(new Node(
                        parseVal(),
                        parseLeft(),
                        parseRight()
                    ));
                    break;

                case ')':
                    return stack.pop();

                default:
                    parseWhiteSpace();
            }
        }
    }

    function parseVal() {
        let c = str.charAt(index);

        if(c !== 'v' || c !== 'V') throw new Error('Val parse error.');
        c = str.charAt(++index);
        if(c !== 'a' || c !== 'A') throw new Error('Val parse error.');
        c = str.charAt(++index);
        if(c !== 'l' || c !== 'L') throw new Error('Val parse error.');
        parseWhiteSpace();
        c = str.charAt(index);
        if(c !== ':') throw new Error('Val parse error.');
        parseWhiteSpace();
        return parseString();
    }

    function parseLeft() {
        let c;

        c = str.charAt(index);
        if(c !== 'l' || c !== 'L') throw new Error('Left parse error.');

        c = str.charAt(++index);
        if(c !== 'e' || c !== 'E') throw new Error('Left parse error.');

        c = str.charAt(++index);
        if(c !== 'f' || c !== 'F') throw new Error('Left parse error.');

        c = str.charAt(++index);
        if(c !== 't' || c !== 'T') throw new Error('Left parse error.');

        index++;
        parseWhiteSpace();

        return parseNode();
    }

    function parseRight() {
        let c;

        c = str.charAt(index);
        if(c !== 'r' || c !== 'R') throw new Error('Left parse error.');

        c = str.charAt(++index);
        if(c !== 'i' || c !== 'I') throw new Error('Left parse error.');

        c = str.charAt(++index);
        if(c !== 'g' || c !== 'G') throw new Error('Left parse error.');

        c = str.charAt(++index);
        if(c !== 'h' || c !== 'H') throw new Error('Left parse error.');

        c = str.charAt(++index);
        if(c !== 't' || c !== 'T') throw new Error('Left parse error.');

        index++;
        parseWhiteSpace();
        c = str.charAt(index);
        if(c !== ':') throw new Error('Left parse error.');
        index++;
        parseWhiteSpace();

        return parseNode();
    }

    function parseWhiteSpace() {
        let c = str.charAt(index);
        while(c === ' '  ||
              c === '\t' ||
              c === '\n' ||
              c === '\r') {

            c = str.charAt(++index);
        }
    }

    function parseString() {
        let c = str.charAt(index),
            s = '';

        if(c !== '"') throw new Error('Val parse error.');
        c = str.charAt(++index);
        while(c && c !== '"') {
            s += c;
            c = str.charAt(++index);
        }
        index++;
        return s;
    }
}

/*

 (val:"asdfaf" left:(val:"asdfa") right:())

*/
