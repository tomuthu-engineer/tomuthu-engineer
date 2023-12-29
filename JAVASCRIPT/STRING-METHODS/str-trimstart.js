let prompt = require('prompt-sync')({ sigint: true }); //assigning prompt
let str=String(prompt('Enter Your Name: ')) //getting user input

let str_trim= str.trimStart()  //it removes the leading white spaces   
console.log(str_trim); 

