function getName(){
    const USER_NAME = prompt("What is your Name")
    sayHello(USER_NAME)
    console.log("Inside getName Function")
}
function sayHello(name){
    alert('Hello ' + name + ' !');
    console.log("Inside sayHello Functionl")
}