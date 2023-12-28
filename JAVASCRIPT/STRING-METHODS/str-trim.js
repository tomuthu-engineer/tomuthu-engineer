let prompt = require('prompt-sync')({ sigint: true }); //assigning prompt
let str=String(prompt('Enter Your Name: ')) //getting user input

let str_trim= str.trim()  //removes the white spaces both sides of the string
console.log(str_trim); 