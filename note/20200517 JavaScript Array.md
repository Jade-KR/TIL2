# 자바스크립트 Array



1. Declaration

```js
const arr1 = new Array();
const arr2 = [1, 2];
```



2. shift, unshift (배열의 길이가 길면 길수록 느려진다)

```js
arr2.unshift(4, 2); // [4, 2, 1, 2]
arr2.shift(); // [2, 1, 2]
```



3. concat

```js
const ex1 = [1, 2]
const ex2 = [3, 4]
const ex3 = ex1.concat(ex2);
console.log(ex3); // [1, 2, 3, 4]

```



4. Searching ( indexOf, includes, lastIndexOf )

```js
const a = [1, 2, 3, 4, 4, 5]
console.log(a.indexOf(1)); // 0
console.log(a.indexOf(3)); // 2
console.log(a.indexOf(9)); // -1

console.log(a.includes(2)); // true
console.log(a.includes(6)); // false

console.log(a.indexOf(4)); // 3
console.log(a.lastIndexOf(4)) // 4
```

















