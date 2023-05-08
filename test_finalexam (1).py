from FinalExam import * #import our FinalExam script

#This is a test script for FinalExam.py

#testing our first function 

string = "ATTTGGATT" #put in whatever string you want, in this case the one from the exam
x = 1 #put in whatever value you want for x, this is the size of the substring
def test_possiblecombs():
     '''This is a test function to test the "possiblecombs" function 
        Arguments:
        x = the length of the substring that you want to find
        string = "ATTTGGATT" 
        expected output: the expected output for a given x in that function
        
        Return: Returns nothing if correct, returns error if incorrect'''
    actual_output = possiblecombs(x, string) #this is running the original function we wrote
    expected_output = 4 #use expected outputs from the table
    assert actual_output == expected_output #assert means if it's true, nothing happens, if it's false it'll give you an error
        #the last part is comparing actual to expected 


#testing again
string = "ATTTGGATT" #put in whatever string you want, in this case the one from the exam
x = 9 #put in whatever value you want for x, this is the size of the substring
def test_possiblecombs():
     '''This is a test function to test the "possiblecombs" function 
        Arguments:
        x = the length of the substring that you want to find
        string = "ATTTGGATT" 
        expected output: the expected output for a given x in that function
        
        Return: Returns nothing if correct, returns error if incorrect'''
    actual_output = possiblecombs(x, string) #this is running the original function we wrote
    expected_output = 1 #use expected outputs from the table
    assert actual_output == expected_output #assert means if it's true, nothing happens, if it's false it'll give you an error
        #the last part is comparing actual to expected 
        



#testing the second function

string = "ATTTGGATT" #put in whatever string you want, in this case the one from the exam
y = 1 #put in whatever value you want for y, this is the size of the substring
def test_actualcombs():
     '''This is a test function to test the "actualcombs" function 
        Arguments:
        y = the length of the substring that you want to find
        string = "ATTTGGATT" 
        expected output: the expected output for a given y in that function
        
        Return: Returns nothing if correct, returns error if incorrect'''
    actual_output = actualcombs(y, string) #this is running the original function we wrote
    expected_output = 3 #use expected outputs from the table
    assert actual_output == expected_output #assert means if it's true, nothing happens, if it's false it'll give you an error
    
    
#testing again
string = "ATTTGGATT" #put in whatever string you want, in this case the one from the exam
y = 9 #put in whatever value you want for y, this is the size of the substring
def test_actualcombs():
     '''This is a test function to test the "actualcombs" function 
        Arguments:
        y = the length of the substring that you want to find
        string = "ATTTGGATT" 
        expected output: the expected output for a given y in that function
        
        Return: Returns nothing if correct, returns error if incorrect'''   
    actual_output = actualcombs(y, string) #this is running the original function we wrote
    expected_output = 1 #use expected outputs from the table
    assert actual_output == expected_output #assert means if it's true, nothing happens, if it's false it'll give you an error
    

    
#testing the third function

string = "ATTTGGATT" #put in whatever string you want, in this case the one from the exam

def test_lincompl():
      '''This is a test function to test the "lin_compl" function 
        Arguments:
        string = "ATTTGGATT" 
        expected output: the expected linguistic complexity of the given string
        
        Return: Returns nothing if correct, returns error if incorrect'''
    actual_output = lin_compl(string) #this is running the original function we wrote
    expected_output = 0.875 #use expected outputs from the table
    assert actual_output == expected_output #assert means if it's true, nothing happens, if it's false it'll give you an error