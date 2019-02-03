# --------------
##File path for the file 
file_path 

#Code starts here
##Creating a function to read files, and store the first sentence
def read_file(path):
    file = open(path, 'r')
    sentence = file.readline()
    file.close()
    return sentence

##Running the above custom function to open file in file_path
sample_message = read_file(file_path)

#Code ends here


# --------------
#Code starts here
##Calling the earlier-defined read-file function to open the two files, and outputting the respective messages
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
print(message_1, message_2)

##Creating a function to merge two messages
def fuse_msg(message_a, message_b):
    quotient = int(message_b)//int(message_a)
    return str(quotient)

##Running the earlier-defined function on the two opened files
secret_msg_1 = fuse_msg(message_1, message_2)

#Code ends here


# --------------
#Code starts here
##Calling the earlier-defined read-file function to open the third file, and outputting the message
message_3 = read_file(file_path_3)
print(message_3)

##Creating a substitute function to replace extant text with pre-set text
def substitute_msg(message_c):
    if message_c == "Red":
        sub = "Army General"
    elif message_c == "Green":
        sub = "Data Scientist"
    else:
        sub = "Marine Biologist"
    return(sub)

####Running the earlier-defined function on the opened file
secret_msg_2 = substitute_msg(message_3)
#Code ends here


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
##Calling the earlier-defined read-file function to open the two files, and outputting the respective messages
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4, message_5)

##Creating a function to read text present in one message but not in the second
def compare_msg(message_d, message_e):
    a_list = message_d.split(" ")
    b_list = message_e.split(" ")
    c_list = [x for x in a_list if x not in b_list]
    final_msg = " ".join(c_list)
    return final_msg

##Running the earlier-defined function on the two opened files
secret_msg_3 = compare_msg(message_4, message_5)
#Code ends here


# --------------
#Code starts here
####Calling the earlier-defined read-file function to open the third file, and outputting the message
message_6 = read_file(file_path_6)
print(message_6)

##Creating an extraction function to ouput only words with even number of characters
def extract_msg(message_f):
    a_list = message_f.split(" ")
    even_word = lambda x: len(x)%2 == 0
    b_list = filter(even_word, a_list)
    final_msg = " ".join(b_list)
    return final_msg

####Running the earlier-defined function on the opened file
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)
#Code ends here


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

final_path= user_data_dir + '/secret_message.txt'

#Code starts here
##Combining contents of collated message into a sentence
secret_msg = " ".join(message_parts)

##Creating a custom function to write to a file
def write_file(secret_msg, path):
    opened_file = open(path, 'a+')
    opened_file.write(secret_msg)
    opened_file.close()

##Running the earlier-defined function on the opened file
write_file(secret_msg, file_path)

##Outputting the secret message
print(secret_msg)
#Code ends here


