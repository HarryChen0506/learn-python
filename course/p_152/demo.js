// class A {
//   constructor(){
//     this.age = 'A'
//   }
//   do() {
//     console.log('do', this.age)
//   }
//   say() {
//     // console.log('say', this.name)
//     console.log('say', this.age)
//   }
//   age(){
//     console.log(this.age)
//   }
// }

// class B extends A {
//   constructor(){
//     super()
//     this.age = 'B'
//   }
//   do() {
//     console.log('hhh', super.age())
//   }
// }

// var a = new A()
// a.do()


// var b = new B()
// b.do()
// b.say()

// 单例模式
class A {
  constructor(name) {
    this.name = name
    if (A.instance === null) {
      A.instance = this
      return A.instance
    } else {
      return A.instance
    }
  }
}
A.instance = null

var a = new A('aaa')
var b = new A('bbb')
console.log('a', a)
console.log('b', b)
console.log('a===b', a === b)