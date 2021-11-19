/*console.log("______________________synchronous(callback before the console_______________________")
const sum=()=>{
    res=19+3;
    console.log(res)
}
const mul=(value)=>{
    var mul=19*3;
    value()
    console.log(mul)
}
mul(sum)

console.log("____________________Asynchronous(callback next the console_______________________")
const s=()=>{
    res=19+3;
    console.log(res)
}
const m=(value)=>{
    var mul=19*3;
    console.log(mul)
    value()
}
m(s)*/

// function fun1(){
//     sum=10+15
//     console.log(sum)
// }
// function fun2(callback){
//     m=10*15
//     callback()
//     console.log(m)
// }
// fun2(fun1)

function fun1(){
    sum=10+15
    console.log(sum)
}
function fun2(callback){
    m=10*15
    console.log(m)
    callback()
}
fun2(fun1)
