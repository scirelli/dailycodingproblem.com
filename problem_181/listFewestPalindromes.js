if(!String.prototype.reverse) {
    String.prototype.reverse = function() {
        return this.split('').reverse().join('');
    };
}

if(!String.prototype.isPalindrome) {
    String.prototype.isPalindrome = function() {
        if(!this.length) return false;
        if(this.valueOf() === this.reverse()) {
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
    const allResults = [];
    let lowestPalindromeCount = Number.MAX_SAFE_INTEGER;

    return function listFewestPalindromes(str) {
        let results = [];

        if(!str || !str.length) {
            return results;
        }

        for(let i=str.length, p=''; i>=0; i--) {
            p = str.substring(0, i);
            if(p.isPalindrome()) {
                results.push(p);
                results = results.concat(listFewestPalindromes(str.substring(i)));
            }
        }

        allResults.push(results);
        results = [];

        return results;
    };
})();
//aaaaaabcba
//a,a,a,a,a,a,b,c,b,a
