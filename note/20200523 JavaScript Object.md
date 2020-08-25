# 자바스크립트 Object

### object 는 key와 value의 집합체이다

1. Literal and property

```js
const obj1 = {};
const obj2 = new Object();

function print(person) {
  console.log(person.name);
  console.log(person.age);
}

const jade = {name: 'jade', age: 4};
print(jade);
```



2. Computed properties ( key는 항상 String으로 !)

```js
console.log(jade.name); // 코딩할 때
console.log(jade[name]); // 실시간으로 원하는 키의 값을 받고 싶을때 (runtime)
```

> 둘의 차이점은??
>
> . => 코딩하는 그 순간 키에 해당하는 값을 받아오고 싶을 때
>
> [''] => 정확하게 어떤 키가 필요한지 모를 때 runtime에서 결정 될 때 (동적으로 key의 value를 받아올때 유용함)

Ex)

```js
function printValue(obj, key) {
  console.log(obj.key); // undefined
  console.log(obj['key']) // jade
}
printValue(jade, 'name')
```



3. Property value shorthand

```js
const person1 = { name: 'bob', age: 2};
const person2 = { name: 'steve', age: 3};
const person3 = { name: 'dave', age: 4};
// 쉽게 추가하고 싶으면??
const person4 = makePerson('jade', 28);
function makePerson(name, age) {
  return {
    name,
    age,
  }
}
// 4. Constructor function
const person5 = new Person('jade', 28);
function Person(name, age) {
  this.name = name;
  this.age = age;
}
```



5. In operator: property existence check (key in obj)

```js
console.log('name' in jade); // true
console.log('age' in jade); // true
console.log('random' in jade); // false
console.log(jade.random); // undefined
```



6. For..in vs for..of

```js
for (key in jade) {
  console.log(key);
}

// for (value of iterable)
const array = [1, 2, 3, 4];
for(value of array) {
  console.log(value);
}
```



7. Cloning

```js
const user = {name: 'jade', age: '20'};
const user2 = user;
user2.name = 'coder';
console.log(user); // {name: "coder", age: "20"}

// old way
const user3 = {};
for (key in user) {
  user3[key] = user[key];
}
console.log(user3);

// useful way
const user4 = {};
Object.assign(user4, user);
// or
const user4 = Object.assign({}, user);

// another example
const fruit1 = { color: 'red' };
const fruit2 = { color: 'blue', size: 'big'};
const mixed = Object.assign({}, fruit1, fruit2);
console.log(mixed.color); // blue
console.log(mixed.size); // big

// => 뒤에 값을 앞에 계속 덮어 씌우기 때문에 같은 property가 있으면 뒤에 할당된 값을 받는다.
```















