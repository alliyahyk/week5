# tuple is made for names
names_tuple = 'Rod', 'Jane', 'Freddy'
# bungle cannot be added to the tuple because it is immutable
# causes error which runs the except code on line 18
try:
    print('######### TRY #########')
    print("The TRY block attempts to run")
    print(f"Original Tuple: {names_tuple}")
    names_sorted_as_list = sorted(names_tuple)
    print("Added Bungle:", names_sorted_as_list)
    print("Attempt to manipulate the tuple...")
    names_tuple[0] = 'Zippy'
    print("is this code reached?")
except FileNotFoundError as error:
    print("######### EXCEPT: FileNotFoundError ######")
    print("the EXCEPT/CATCH block only runs if this error happens")
    print(f"the following file cannot be found {error.filename}. Please try another file")
except TypeError as error:
    print("####### EXCEPT: TypeError #######")
    print("Oh dear, that is not allowed on that type")
    print(error)
except Exception as error:
    print("####### EXCEPT: Exception ######")
    print("Generic catch-all except / catch block")
    print(error)
# finally always runs whether
finally:
    print('The FINALLY block ALWAYS runs')
    print('The finally block is used to tidy up')
    if names_tuple:
        names_tuple = None




print("After exception handling is finished...the program can continue")