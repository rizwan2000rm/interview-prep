//? https://www.youtube.com/watch?v=v4cd1O4zkGw

//? 'n' => number of inputs.

//? Rule 1
//! O(a+b)

//? Rule 2
//! Drop the constants
//! O(2n) => O(n)

const rule2 = () => {
  //! O(n)
  for (let i = 0; i < array.length; i++) {
    doStep1();
  }
  //! O(n)
  for (let i = 0; i < array.length; i++) {
    doStep2();
  }
};

//? Rule 3
//! Different inputs different variables
//! O(a*b)
const rule3 = (array1, array2) => {
  //! O(a)
  for (let i = 0; i < array1.length; i++) {
    //! O(b)
    for (let j = 0; j < array2.length; j++) {
      doStep2();
    }
  }
};

//? Rule 4
//! Drop non dominate terms
//! O(n + n^2) => O(n^2)
