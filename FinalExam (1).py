#Big Data Final Exam Script


string = "ATTTGGATT" #name of string

#building a function to find all possible unique substrings of length "x" in a given string

def possiblecombs(x, string):
    '''This function finds all possible unique substrings of length x in a given string
        Arguments:
        x (int) = the length of the substring that you want to find
        string = name of the string you want to put into the function
        
        Return: The number of possible unique substrings of length x within your string'''
    
    #possible number of combinations for substrings of length "x"
    combinations = 4**x 
    
    #total slots (spaces in between the substrings) of length "x" in string
    slots =  len(string) + (1 -x)
    
    #so depending on the length of the string, you are either limited by the number of slots OR the number of unique combinations
    #to deal with this, I'm going to write an if/else function
    if combinations <= slots:
            return combinations
    else:
            return slots
        

        
#now we need the actual OBSERVED substrings
#this function calculates the actual observed number of substrings within a string

def actualcombs(y, string):
    '''This function finds the observed unique substrings of length x in a given string
        Arguments:
        y (int) = the length of the substring that you want to find
        string = name of the string you want to put into the function
        
        Return: The number of observed unique substrings of length x within your string'''
    #tells you the total number of slots of length y in the given string
    slots = len(string) + (1-y)
    #now we need to make a list to store the substrings
    sub = []
    
    
    #okay now we need to loop through all of the different slots in the given string of length y
    for i in range(slots):
        #if the sub string in the ith slot is not already in the list, then it appends it
        if string[i:i+y] not in sub:
            sub.append(string[i:i+y])
        
        
    return len(sub)



#third function to calculate linguistic complexity (obs/possible)

def lin_compl(string):
    '''This function utilizes the previous two functions to calculate linguistic complexity
        Arguments:
        string = name of the string you want to put into the function
        
        Return: the linguistic complexity of a given string, calculated as observed/possible. '''
    #create two variables, one as possible and one as observed
    possible = 0 
    observed = 0
    
    #loop through all possible sub string lengths and add the number of observed and possible substrings of length z to variables possible and observed, respectively
    
    for i in range(len(string)): #for i within the length of the string
        #
        z = i+1 #need + 1 so that it doesn't start at 0 and instead starts at 1
        possible += possiblecombs(z, string) # += allows us to update the variable each time to include new information
        observed += actualcombs(z, string) 
             
    return observed/possible #to calc linguistic complexity, we divide observed/possible