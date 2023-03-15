
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: W1805896
# Name : Joven Manikiza
 
# Date: 29/11/2021





    
import time              # I CREDIT THE import time AND time.sleep() TO: User: Evan Fosmark @ StackOverflow.com  LINK : https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python/510351#510351                                                                      



histogram_points = {
    "Progress" : 0,
    "Trailer" :  0,                                                                             #Users input data from the loop gets stored here
    "Retriever" : 0,                                                                            #Currently inputted some values 
    "Exclude" : 0,
    } 

teach_or_stu = str('')
clear = "\n" * 22                                                                               #visual effect to clear users UI for readability and enjoyment

'''if clear is higher than * 45 it condenses it into an alert box
    when running in the idle so I had to make it smaller and print them
    more often'''



    #VISUAL LOADING                                                                                                           
def loading():
    print(clear)   # I CREDIT THE  clear = "\n" * 22 AND print(clear) TO: StackOverflow.com, The direct link to the source has been lost
    print(clear)
    print(clear)
    time.sleep(1.5)
    print("loading", end = "")
    time.sleep(1)
    print(".", end = "")
    time.sleep(0.7)
    print(".", end = "")
    time.sleep(0.7)
    print(".", end = "")                                                                                      
    time.sleep(1)
    print(clear)
    print(clear)
    print(clear)
    print("Complete", end = "")
    time.sleep(2)
    print(clear)
    print(clear)
    print(clear)



    #LOGIN FUNCTION
def login():
    
    print(clear)
    print(clear)
    print(clear)

    time.sleep(1)

    print("\n    ......\n     Login\n    ......\n\n")

    time.sleep(1.3)
    global teach_or_stu
    teach_or_stu = str(input("   1. Teacher\n\n   2. Student\n\n"))                                  #user can type 1,2, T/teacher, S/student aslong as it is either number or a word containing either R or S,
    time.sleep(1.3)                                                                             # as they are only contained in each word. Will work if user spells it wrong.


    if teach_or_stu == '1' or 'r' in teach_or_stu or 'R' in teach_or_stu:
        username = input("\n\nUsername: ")
        time.sleep(1)
        password = input("\nPassword: ")

        password = len(password) * '*'

    
        print(clear)
        print(clear)
        print("Username: " + username + "\nPassword: " + password)
        print(clear)
        time.sleep(1)

        print("\n\nWelcome " + username, end = ''),
        time.sleep(1.3),
        print(" to the 'Progression Predictor'!\n\n")
        time.sleep(3)
        print("\nAs you are using a Teacher account your input values of students will be saved and later can be called upon in the form of a histogram.\n\n")
        time.sleep(3)
        print("\nHow to use: ")
        time.sleep(1.5)
        print("             * Keep the input range between 0 and 120\n")
        time.sleep(2)
        print("             * Numerical values only unless specified otherwise\n")
        time.sleep(2)
        print("             * Multiples of 20 only \n")
        time.sleep(2)
        print("             * The inputted data must equal exactly 120 \n\n")
        time.sleep(1.2)
        ready = input("\n\n\n\n      When you are ready press the 'Enter' key\n\n")



    if teach_or_stu == '2' or 's' in teach_or_stu or 'S' in teach_or_stu:
        
        username = input("\n\nStudent ID: ")
        time.sleep(1)

        password = input("\nPassword: ")

        password = len(password) * '*'

        print(clear)
        print(clear)
        print("Student ID: " + username + "\nPassword: " + password)
        print(clear)

        time.sleep(1)

        print("\n\nWelcome " + username, end = ''),
        time.sleep(1.3),
        print(" to the 'Progression Predictor'!\n\n")                                                   
        time.sleep(3)                                                                                   
        print("\nAs you are using a Student account your input values will not be saved and is used to help you predict your end of year grade.\n\n")
        time.sleep(3)
        print("\nHow to use: ")
        time.sleep(1.5)
        print(" " * 13 + "* Keep the input range between 0 and 120\n")
        time.sleep(2)
        print(" " * 13 + "* Numerical values only unless specified otherwise\n")
        time.sleep(2)
        print(" " * 13 + "* Multiples of 20 only \n")
        time.sleep(2)
        print(" " * 13 + "* The inputted data must equal exactly 120 \n\n")
        time.sleep(1.2)
        ready = input("\n\n\n\n" + " " * 8 + "When you are ready press the 'Enter' key\n\n")

        loading()



        
    #LOGOUT FUNCTION
def logout():

    loop = True
    time.sleep(2)
    print(clear)
    print(clear)
    print("Logging out user...")
    time.sleep(2.5)
    print("Logged out.")
    time.sleep(2.5)
    print(clear)
    print(clear)
    print(clear)
    login()


    

loop = True

login()

while loop == True:

    pass_input = 0
    defer_input = 0                                                                             # This will wipe the values stored when user incurs problem
    fail_input = 0

   


                      
    #PASS                  
    try: 
        pass_input = int(input("\nWhat is the pass mark? \n\n"))
        
    except TypeError:
        print("\nInteger required. Try using multiples of 20.\n")
        continue
    
    except ValueError:
        print("\nInteger required. Use numerical values only.\n")
        continue

    if (pass_input % 20) != 0:
        print("\nOut of range. Please only use multiples of 20.\n")
        continue

    elif pass_input < 0 or pass_input > 120:
        print("\n\nPlease keep your input range between 0 and 120.\n\n")
        continue



    #DEFER
    try:
        defer_input = int(input("\nWhat is the defer mark? \n\n"))
        
    except TypeError:
        print("\nInteger Required. Try using multiples of 20.\n")
        continue
    
    except ValueError:
        print("\nInteger required. Use numerical values only.\n")
        continue

    if (defer_input % 20) != 0:
        print("\nOut of range. Please only use multiples of 20.\n")
        continue
    
    elif defer_input < 0 or defer_input > 120:
        print("\n\nPlease keep your input range between 0 and 120.\n\n")
        continue

    elif pass_input + defer_input > 120:
        print("\nPlease make sure you keep the total value to be exactly 120.\n")
        continue





    #FAIL
    try:  
        fail_input = int(input("\nWhat is the fail mark? \n\n"))                        # THESE ALL COULD HAVE BEEN MADE INTO FUNCTIONS AND CALLED UPON
        
    except TypeError:
        print("\nInteger Required. Try using multiples of 20.\n")
        continue

    except ValueError:
        print("\nInteger required. Use numerical values only.\n")
        continue

    if (fail_input % 20) != 0:
        print("\nOut of range. Please only use multiples of 20.\n")
        continue

    elif fail_input < 0 or fail_input > 120:
        print("\n\nPlease keep your input range between 0 and 120.\n\n")
        continue

    elif pass_input + defer_input + fail_input != 120:
        print("\nPlease make sure you keep the total value to be exactly 120.\n")
        continue


    

 
    pdf_values = [pass_input, defer_input, fail_input]

    if pdf_values[0] == 120:
        print("\n  Progress")                                                            
        
    elif pdf_values[0] == 100:
        print("\n   Trailer")                                                               

    elif pdf_values[0] < 100 and pdf_values[2] < 80:
        print("\n   Retriever")                                                            

    elif pdf_values[2] >= 80:
        print("\n   Exclude")


    #STUDENT CONTINUE
    if teach_or_stu == '2' or 's' in teach_or_stu or 'S' in teach_or_stu:                           #Here it splits the code to kick the student out or bring her to the top
        q_or_c = str(input("\n\nPress Y to try again\n\nPress Q to quit"))                          #The teachers code runs through the exact same programme but has access to further the code

        if 'q' in q_or_c or 'Q' in q_or_c:
            
            logout()
            login()
            continue

        else:
            time.sleep(2)
            continue
    




    #ADDING TO HISTOGRAM DICTIONARY
        
    if pdf_values[0] == 120:
        histogram_points["Progress"]+= 1                                                              #is the value of progress, where pass equalled 120 
        
    elif pdf_values[0] == 100:
        histogram_points["Trailer"]+= 1                                                               # is the value of progress(module trailer), where pass would equal 100 and one of the other two values would be 20

    elif pdf_values[0] < 100 and pdf_values[2] < 80:
        histogram_points["Retriever"] += 1                                                            # is the value of Do not progress - module retriever, being below 100 on pass and below 80 on fail would produc the module retriever

    elif pdf_values[2] >= 80:
        histogram_points["Exclude"] += 1                                                              # is the value of Exclude, where fail would have to be equal to or greater than 80





    #TEACHER CONTINUE
    if teach_or_stu == '1' or 'r' in teach_or_stu or 'R' in teach_or_stu:
        complete = str(input("\nWould you like to continue adding more values? \n\nPress Y to continue\nPress Q to quit and view histogram.\n\n"))

        if complete == "Y" or complete == "y":
        
            time.sleep(2)
            continue

        elif 'Q' in complete or 'q' in complete:
            loading()   
    

    #HISTOGRAM / HORIZONTAL
        
        time.sleep(1)
        print("Here is the histogram of the data you have inputted.")
        time.sleep(4)
        print("\n\n")
        print(" " * 17 + "Horizontal Histogram\n")
        print(" " + "-" * 50)
        time.sleep(0.7)
        print("\n Progress   " + str(histogram_points["Progress"]) + " : | " + "* " * histogram_points["Progress"] + "\n")
        time.sleep(0.7)
        print(" Trailer    " + str(histogram_points["Trailer"]) +" : | " + "* " * histogram_points["Trailer"] + "\n")
        time.sleep(0.7)
        print(" Retriever  " + str(histogram_points["Retriever"]) + " : | " + "* " * histogram_points["Retriever"] + "\n")
        time.sleep(0.7)
        print(" Exclude    " + str(histogram_points["Exclude"]) + " : | " + "* " * histogram_points["Exclude"] + "\n")
        time.sleep(0.7)
        print(" " + "-" * 50)
        print("\n" * 2)
        print("Total values inputted: " + str((histogram_points["Progress"] + histogram_points["Trailer"] + histogram_points["Retriever"] + histogram_points["Exclude"])))

                                                                                                     
    #HISTOGRAM / VERTICAL
        
        time.sleep(4)
        print("\n" * 3 + " " * 17 + "Vertical Histogram")
        print(" " + "-" * 50)
        time.sleep(0.7)
        print(" |   Progress " + str(histogram_points["Progress"]) + "  Trailer " + str(histogram_points["Trailer"]) + "  Retriever " + str(histogram_points["Retriever"]) + "  Exclude " + str(histogram_points["Exclude"]) + "|")
        print(" " + "-" * 50)

        

        all_values = histogram_points.values()           #I CREDIT THIS AND THE NEXT LINE TO: Kite.com @ https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
        max_histogram_points = max(all_values)
        

        
        for i in range(max_histogram_points):         #IF i IS IN THE HIGHEST VALUE IT WILL RUN
            
            print(" |" + " " * 7, end= "")

            if i in range(histogram_points["Progress"]):
                print("*" + " " * 11, end="")

            else:
                print(" " * 12, end="")


            if i in range(histogram_points["Trailer"]):
                print("*" + " " * 10,  end="")

            else:
                print(" " * 11, end ="")

            if i in range(histogram_points["Retriever"]):
                print("*" + " " * 12, end ="")

            else:
                print(" " * 13, end="")

            if i in range(histogram_points["Exclude"]):
                print("*" + " " * 4 + "|")

            else:
                print(" " * 5 +"|")
                
              
        print("\n\nTotal values inputted: " + str((histogram_points["Progress"] + histogram_points["Trailer"] + histogram_points["Retriever"] + histogram_points["Exclude"])))



        time.sleep(2)
        print("\n\n Keep adding more values or would you like to logout?\n\n")
        time.sleep(0.7)
        print(" 1. Continue\n")
        print(" 2. Quit\n")
        again = input()

        if '1' in again or 'c' in again or 'y' in again or 'C' in again :
            time.sleep(0.7)
            continue

        elif '2' in again or 'q' in again or 'Q' in again:
            logout()
            loading()
            login()
            continue

        #END
