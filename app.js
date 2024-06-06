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


// function add(...params){
// let val = 0;
// for(let i = 0; i < params.length; i++){
// val += params[i] 
// }

// console.log(val)
// return val
// }

// add(1,2,3,5)


// class Counter {
//     constructor(iterable){
//     this.iterable =  iterable
//     this.map = new Map()
// }

// count(){
//     this.iterable.map((item)=> {
//         let is_key_exist = this.map.has(item)
//         if(is_key_exist){
//             return this.update(item)
//         }
//        this.create(item)
//     })

//     return this
//     }

// update(item){
//         let exist_item = this.map.get(item) 
//          exist_item[item] += 1
//          this.map.set(item, exist_item)
//          return
// }

// create(item){
//         let obj = {}
//         obj[item] = 1
//         this.map.set(item , obj)
// }

// copy(){
//     let clone = this.map
//     return clone
// }

// keys(){
//     return this.map.keys()
// }

// clear(){
//     return this.map.clear()
// }
// popitem(key){
//     return this.map.delete(key)
// }

//  get increment(){
// return this.map.values()
//  }
// }



// const counter = new Counter([1,{ite:"hello"},2,3,4,4,4,5,{ite:"hello"}, "hi",6])

// // javascript code
// function join(x, list = []){
//     list.push(x)
//     return list
//   }

//   console.log(join(20)) // returns [20]
//   console.log(join(50)) // return [50]
//   console.log(join(30)) // return [30]





//   function print_total(){
//     let avg  = 5


//     function print(){
//         let expenses = 2000
//         let amount  = 5000
//         return (amount - 2000 )+avg
//     }
//     return print
//   }


//   let get_total = print_total()
// console.log(get_total())


function decorator(decor){
    function decorWrappper(args){
        console.log("Greeting you now !")
        decor(args)
    }

    return decorWrappper
}


function decorate(args){
    console.log(args)
}

decorate = decorator(decorate)
decorate("Hello boss")