// First JS code


// Use let keyword to identify variable
// cannot be a reserved keyword

let person = 'Matthew';
console.log(person);

// {} object
let human = {
    firstName: 'Count',
    age: 20
};

// Dot notation
human.name = 'John'

console.log(human.name)

//bracket notation
human['firstName'] = 'Matthew';

// Each notation has its own uses.

// Arrays: Data Structure to represent a list of items 

let selectedColors = ['red', 'blue']; // array literal
selectedColors[2] = 'green';
// Use index to access an element
//ie
console.log(selectedColors[0]) // will print red

console.log(selectedColors.length)

// Functions: Fundamental building block in JS, completes a task
// body of function inside {} , parameter inside, input for the function()
function greet(name){
    console.log('Hello' + name);
}

greet('Matthew'); // Matthew is an argument for the parameter
greet('Grinch');

function greet(name, lastName){
    console.log('Hello' + ' ' + name + ' ' + lastName);
}
greet('Matthew', 'Mockett')

// Calculating a value
function square(number){
   return number * number;
}

let num = square(2);
console.log(num)