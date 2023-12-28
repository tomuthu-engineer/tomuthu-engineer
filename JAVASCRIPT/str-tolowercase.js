let prompt = require('prompt-sync')({ sigint: true }); //assigning prompt

let str=String(prompt('Enter Your Name: ')) //getting user input

let lowerstr= str.toLowerCase()  //it converts Upper case letters to lower case letter
console.log(lowerstr); 