if(!String.prototype.reverse) {
    String.prototype.reverse = function() {
        return this.split('').reverse().join('');
    };
}

if(!String.prototype.isPalindrome) {
    String.prototype.isPalindrome = function() {
        if(!this.length) return false;
        if(this.valueOf().toLowerCase() === this.reverse().toLowerCase()) {
            return true;
        }
        return false;
    };
}

class Node{
    constructor(palindrome='') {
        this.children = [];
        this.palindrome = palindrome;
    }
}

module.exports = (()=> {
    return function listFewestPalindromes(str) {
        const root = new Node();

        _t(str, root);

        return findShortestPath(root);

        function _t(str, node) {
            for(let i=1, l=str.length, ss, n; i<=l; i++) {
                ss = str.substring(0, i);
                if(ss.isPalindrome()) {
                    n = new Node(ss);
                    node.children.push(n);
                    _t(str.substring(i), n);
                }
            }
        }

        function findShortestPath(node) {
            const paths = [];
            let shortestPath = Number.MAX_SAFE_INTEGER,
                result = [];

            _t(node);
            result.shift();
            return result.map(n=>n.palindrome);

            function _t(node) {
                paths.push(node);

                if(!node.children.length) {
                    if(paths.length < shortestPath) {
                        shortestPath = paths.length;
                        result = paths.slice(0);
                    }
                }

                for(let i=0; i<node.children.length; i++) {
                    _t(node.children[i]);
                }
                paths.pop();
            }
        }
    };
})();
/*
Example 1:
    aabbaa
                                         ('')
                          ┎------┍---------┴---┒
                          |      |          (aabbaa)
                          |     (aa)--┒
                          |      |   (bb)
                          |     (b)   |
                          |      |   (aa)
                          |     (b)--┒
                          |      |  (aa)
                          |     (a)
                          |      |
                          |     (a)
                         (a)------------------------------------┒
                          |                                     (abba)
                         (a)-----------┒--------------┒          |
                          |            |              |          (a)
                         (b)           (bb)--┒        (bbaa)
                          |             |    |
                         (b)---┒        (a) (aa)
                          |    |        |
                         (a)   (aa)     (a)
                          |
                         (a)
 */
