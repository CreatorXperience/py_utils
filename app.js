let  arr = [1,2,3,4,5,6,7,8, typeof Symbol()]
let sym = Symbol()

let  obj = {
    item: 1,
    0: "yo",
    sym: "symbol" 
}

for(i of arr){
console.log(i)
}






console.log(5000 in arr)



//clone
clone = arr
arr.reverse().pop()
clone.pop()
console.log(arr == clone)