let prompt = require('prompt-sync')({ sigint: true }); //assigning prompt
let str=String(prompt('Enter Your Name: ')) //getting user input

let str_length= str.length  //it returns total count of strings
console.log(str_length); 