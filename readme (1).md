## Final Exam Readme

Lauren Michael, 2023

### Overview
These scripts were created for the final exam of Big Data Analysis at the University of Rhode Island.

There are two scripts necessary for this project, FinalExam and test_finalexam.

The FinalExam script will calculate:
-Function 1: the number of possible substrings of length x of a given string
-Function 2: the number of observed substrings of length y of a given string
-Function 3: the linguistic complexity of that string, calculated as the observed/possible substrings of a given string


The test_finalexam script tests if these functions are working properly. 


### Inputs
string = string of your choice
x,y,z = chosen substring length

Function 1 and 2 require both a string and substring length, Function 3 only requires the string.


### Utilizing the functions

To use these functions, simply run the FinalExam script in the command line. Once this is complete, you can run the function by running:

functionname(substring length, string name)

for instance:

string = "ATTTGGATT"
possiblecombs(3, string)

To utilize the test functions, you will need to input your string and your expected output. Once you've added those to the function, you can simply run the script in the command line. To see if the test was successful, you can run:

testname()

for instance:
test_possiblecombs()