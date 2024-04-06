// let  arr = [1,2,3,4,5,6,7,8, typeof Symbol()]
// let sym = Symbol()

// let  obj = {
//     item: 1,
//     0: "yo",
//     sym: "symbol" 
// }

// for(i of arr){
// console.log(i)
// }






// console.log(5000 in arr)



// //clone
// clone = arr
// arr.reverse().pop()
// clone.pop()
// console.log(arr == clone)


// let react = [""]

// for(let i  = 1; i <  10; i++ ){
//     for(let k = 1; k < 11; k++){
//         let answer =  i * k 
//         console.log(answer)
//     }
// }

// console.log("the loop is over")


function add(...params){
let val = 0;
for(let i = 0; i < params.length; i++){
val += params[i] 
}

console.log(val)
return val
}

add(1,2,3,5)