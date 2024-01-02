let prompt = require('prompt-sync')({ sigint: true }); //assigning prompt
let str=String(prompt('Enter Your Name: ')) //getting user input

let upperstr= str.toUpperCase()  //it converts lower case letters to uppper case letter
console.log(upperstr); 

