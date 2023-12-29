let prompt = require('prompt-sync')({ sigint: true }); //assigning prompt

let str=String(prompt('Enter Your Name: ')) //getting user input

let str_trimend = str.trimEnd()  //it removes the trailing white spaces
console.log(str_trimend); 