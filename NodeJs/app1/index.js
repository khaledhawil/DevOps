// var data = "Khaled Hawil loves his work";

// data="khaled";
// console.log(data)



// var x = 4 ;

// x += 5;
// x -= 3;
// x *= 2;
// // x /= 4;
// x %= 5;




// console.log(x)





// {
//     var x = 5;
// }
 

// console.log(x)



//   var x = 4 ;
//   var y = 5 ;
//   var first_name = "Khaled"  ; 

//   var age = 23 ;


//   if ( first_name == "Khalmed" && age >=20 || x == 5 && y == 3   )
//     {
//     console.log("Ok")
//   } 
//   else if (first_name == "Khaled") 
// {
//         console.log("You'r Khaled")
// }
//   else 
//   {
//     console.log("Not Ok")
//   }




// var date = 5;

// {
//   console.log(date);

//   var date = 7;   
// }
 






// // x = 5; 
// {
//   const x =  65;

//   console.log(x);

// }


// function how()
// { 
//    const x =  65;

//   console.log(x)
// }

// how();









// {
//   let k = 9 ;
//   console.log(k)

// }

// let k = 66 ;

//   console.log(k)

// let m = 9;

// for ( let i = 0; i <= 9 ; i++ )
//   {  
//      console.log(i , " * " , m , " = " , m * i );

//   }




// for ( let i = 0; i <= 6 ; i++  ){
//   // console.log(i , " + " , i , " = " , i +  i)
//   console.log("I = ",i)
//   console.log("---------------------")
//   for (let k = 0; k <= 3  ; k++)
//     {
//       console.log(i, " * " , k , " = " , i * k )
//    }
//    console.log("=========================")
   
// }




// for ( let i = 0; i <= 10 ; i++  )
//   {

//     if ( i == 7 ){
//       console.log("The End ^");
//       break;
      
//     }

//     if ( i   ==  3 ){
//       console.log("not end ^");
//       continue;
      
//     }

//     console.log(i)

// }






            // "هكتب "يا رب اخلص جيش ب عدد الايامي الي متبقيه" 


// for ( i = 0 ; i <= 90 ; i++){
//   console.log(i," = " ,  "يــــا رب أ خلــــص جــــيش") 
  
//   if ( i == 90 ){
//     console.log("'تلاته منه و نرتاح منه' ")
//     console.log("'---------------' ")
//     console.log(" '25/11/2024 = The freedom  , 90 days left to be free ' ")
//     console.log("'---------------' ")
//     console.log("'7awil' ")
//   }
// }


// for ( let i = 0; i <= 10 ; i++  )
//   {

//     if ( i == 7 ){
//       console.log("The End ^");
//       break;
      
//     }

//     if ( i   ==  3 ){
//       console.log("not end ^");
//       continue;
      
//     }

//     console.log(i)

// }

// factorial  of number 


// !5 = 5 * 4*3*2*1
// !10 = 10 * 9 * 8 * .....

// const n = 5 ; 
// let factorial = 1;


// for (let i = 2 ; i <=n; i++)
//   {
//     factorial =  factorial *  i ;

//   }

//   console.log(factorial);
//   console.log(5 * 4 * 3 * 2 * 1);


const n = 30;



for(let i = 2 ; i <= n ; i ++)
  {
    let isPrime = true ;
    
    for(let j = 2 ; j < i ; j++){
      
      if (i % j == 0){
        isPrime = false;
        break;
      }
    }
    if (isPrime){
      console.log(i);
    }

}








