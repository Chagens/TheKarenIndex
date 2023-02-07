#Prototyping Storing Procedures

#imports
from itertools import count
import json
import os.path
    
#function either creates the passive file or
#"boots up" the active memory from the passive file
#then returns the active memory object
def boot_TKI():
    #Create New .json file or open existing one
    if (os.path.exists(".\TKI.json")) :
        #print("Booting Active Memory from TKI.json file\n\n")
        a_mem = [] #create empty list
        
        #if the file isn't empty, read the memory
        if (os.path.getsize(".\TKI.json") != 0) :
            TKI_file = open(".\TKI.json", "r")
            #start by pulling memory into a string from the TKI file
            read_file = TKI_file.read()

            #then load the string into a proper Py object
            a_mem = json.loads(read_file)

            TKI_file.close()

        return a_mem #return the active_memory

    else :
        fd = open(".\TKI.json", "x") #create file
        #print("TKI.json file created\n\n")
        #recursively call function after object is made
        fd.close() #close file
        return boot_TKI()


#function stores the current active memory into the file
def store_active_mem(active_mem):
    #print("Storing Active Memory into Passive Memory\n\n")

    pass_mem = open("./TKI.json", "w")

    pass_mem.write(json.dumps(active_mem, indent = 3))

    pass_mem.close()


#this function will take in a new review and 
# store it into the active memory
def new_review(active_mem, url, text, stars, anger, incomp, length, scammy):
    #print("Adding New Review into Active Memory\n\n")

    #initialize the review object
    review = {
        "URL" : url,
        "Text" : text,
        "Stars" : stars,

        "ratings" : {
            "Anger" : anger,
            "Incomprehensible" : incomp,
            "Length" : length,
            "Scammy" : scammy
        }
    }

    #then insert it into active memory
    active_mem.append(review)

def return_LB_A(active_mem) :
    #print("Returning Anger LB\n\n")

    #traverse through a_mem,
    #look for highest val of CATEGORY
    #to find next:
    #   It. thru and use last highest as upper bounds
    #until top 5 are found
    #append each entry into a new object to return

    #create a copy so that elements can be deleted
    a_mem = active_mem.copy()
    it = 0
    found = 0 #"found" Top 5 scores
    top_score = 0
    top_score_index = 0
    num_elements = len(active_mem)
    leaderboard = []

    #find Top 1
    while (found < 5) :

        if (a_mem[it % num_elements]["ratings"]["Anger"] >= top_score) :
            top_score_index = it % num_elements
            top_score = a_mem[it % num_elements]["ratings"]["Anger"]

        it += 1

        if ((it % num_elements) == 0) :
            leaderboard.append(a_mem[top_score_index])
            del a_mem[top_score_index] #remove element so that it is not selected again
            num_elements = len(a_mem) #update this val
            found += 1
            it = 0
            top_score = 0

    return leaderboard


def return_LB_I(active_mem) :
    #create a copy so that elements can be deleted
    a_mem = active_mem.copy()
    it = 0
    found = 0 #"found" Top 5 scores
    top_score = 0
    top_score_index = 0
    num_elements = len(active_mem)
    leaderboard = []

    #find Top 1
    while (found < 5) :

        if (a_mem[it % num_elements]["ratings"]["Incomprehensible"] >= top_score) :
            top_score_index = it % num_elements
            top_score = a_mem[it % num_elements]["ratings"]["Incomprehensible"]

        it += 1

        if ((it % num_elements) == 0) :
            leaderboard.append(a_mem[top_score_index])
            del a_mem[top_score_index] #remove element so that it is not selected again
            num_elements = len(a_mem) #update this val
            found += 1
            it = 0
            top_score = 0

    return leaderboard

def return_LB_L(active_mem) :
    #create a copy so that elements can be deleted
    a_mem = active_mem.copy()
    it = 0
    found = 0 #"found" Top 5 scores
    top_score = 0
    top_score_index = 0
    num_elements = len(active_mem)
    leaderboard = []

    #find Top 1
    while (found < 5) :

        if (a_mem[it % num_elements]["ratings"]["Length"] >= top_score) :
            top_score_index = it % num_elements
            top_score = a_mem[it % num_elements]["ratings"]["Length"]

        it += 1

        if ((it % num_elements) == 0) :
            leaderboard.append(a_mem[top_score_index])
            del a_mem[top_score_index] #remove element so that it is not selected again
            num_elements = len(a_mem) #update this val
            found += 1
            it = 0
            top_score = 0

    return leaderboard

def return_LB_S(active_mem) :
    #create a copy so that elements can be deleted
    a_mem = active_mem.copy()
    it = 0
    found = 0 #"found" Top 5 scores
    top_score = 0
    top_score_index = 0
    num_elements = len(active_mem)
    leaderboard = []

    #find Top 1
    while (found < 5) :

        if (a_mem[it % num_elements]["ratings"]["Scammy"] >= top_score) :
            top_score_index = it % num_elements
            top_score = a_mem[it % num_elements]["ratings"]["Scammy"]

        it += 1

        if ((it % num_elements) == 0) :
            leaderboard.append(a_mem[top_score_index])
            del a_mem[top_score_index] #remove element so that it is not selected again
            num_elements = len(a_mem) #update this val
            found += 1
            it = 0
            top_score = 0

    return leaderboard