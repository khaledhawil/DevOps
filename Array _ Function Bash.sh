#!/usr/bin/bash
echo "Hello Mina"
#--------------------------------------------------------------------------------------------------#
#create Array 
declare -A AssoociativeArray #Array index os named form 
declare -a NumericArray      #Array index os named form 
array=(1 2 3 4 "Minasss" 5)
array2=(1 2 3 4 5)
#--------------------------------------------------------------------------------------------------#
#display All Array 
echo "display All Array : ${array[@]}"
#display Specific index
index=2
echo "display Specific index : ${array[$index]}"
#display All index 
echo "display All index : ${!array[@]}"
#display length of Array 
echo "length of Array : ${#array[@]}"
 
#display length of Specific Element Array 
echo "length of Specific Element : ${#array[4]}"

#--------------------------------------------------------------------------------------------------#
#Add a new element
#Method 1  ==> +=
array2+=( Cobalt Nickel )

#Method 2  ==> [index]
array2[10]="test"
echo "Array 2 = ${array2[@]}"
echo "display All index : ${!array2[@]}" #display All index 
echo "length of Array : ${#array2[@]}" #display length of Array 
#Delete an element  ==> unset my_array[index]
unset array2[10]
echo "Array 2 = ${array2[@]}"
#--------------------------------------------------------------------------------------------------#
#Bash for loop array example to iterate through array values
# for i in "${arrayName[@]}"
# do
#    # do whatever on "$i" here
# done
sum=0
for i in "${array2[@]}"
do
   sum=$(($sum*$i))
done
echo "Sum =  $sum"
#Finally use the three-expression (C style) bash for loops syntax:
for (( j=0; j<${#array2[@]}; j++ ));
do
  echo "Current index $j with value : ${array2[$j]}"
done


#Take Array from user 
read -p "Enter Array : " -a x
echo "You Enter ${x[@]}"


read -p "Enter size of array " size 
for((i=0;i < $size; i++)) 
do 
read -p "enter element number $i: " array[$i] 
done 
echo "${array[@]}" 

#replace Value
y=( ${x[@]/1/5})
echo "y =  ${y[@]}"

: ' 
Syntax	Result
arr=()	Create an empty array
arr=(1 2 3)	Initialize array
${arr[2]}	Retrieve third element
${arr[@]}	Retrieve all elements
${!arr[@]}	Retrieve array indices
${#arr[@]}	Calculate array size
arr[0]=3	Overwrite 1st element
arr+=(4)	Append value(s)
str=$(ls)	Save ls output as a string
arr=( $(ls) )	Save ls output as an array of files
${arr[@]:s:n}	Retrieve n elements starting at index s
'


function test(){
    echo "Hello Function"
}
test
#Variables Scope
var1='A'
var2='B'

my_function () {
  local var1='C'
  var2='D'
  echo "Inside function: var1: $var1, var2: $var2"
}

echo "Before executing function: var1: $var1, var2: $var2"

my_function

echo "After executing function: var1: $var1, var2: $var2"
#Return Values
my_function () {
  echo "some result"
  return 55
}

my_function
echo $?
#Passing Arguments to Bash Functions
greeting () {
  echo "Hello $1"
}

greeting "Joe"
