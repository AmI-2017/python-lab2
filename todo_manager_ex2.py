'''
Created on Mar 17, 2017
Copyright (c) 2016-2017 Teodoro Montanaro

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
@author: tmontanaro
'''

from sys import argv

def new_task(tasks_list):
    '''
    Add a new element to the given list
    '''

    #ask the user to insert the task she wants to add
    string = input("Type the new task:\n>")

    # actually add the item to the list
    tasks_list.append(string)
    print("The new task was successfully added to the list")


def remove_task(tasks_list):
    '''
    Remove an element from the given list
    '''

    # ask the user to insert the task she wants to remove
    string = input("Type the entire content of the task you want to delete:\n>")

    # check if the task is actually present in the list
    if (string in tasks_list):
        tasks_list.remove(string)
        print("The element was successfully deleted")
    else:
        print("The element you specified is not in the list!")


def print_sorted_list(tasks_list):
    '''
    Print the elements of the list, sorted in alphabetic order
    '''

    # check if the list is empty
    if (len(tasks_list) == 0):
        print("The list is empty")
    else:
        # we don't want to modify the real list of elements: we want only to print it after sorting
        # there are 2 possibilities:
        # a) using the sort method
        #  temp_tasks_list = tasks_list[:]
        #  temp_tasks_list.sort()
        #  print(temp_tasks_list)
        # b) using the sorted method (the sorted method returns a new list)
        print(sorted(tasks_list))

if __name__ == '__main__':
    # main program

    # initialize the task list
    tasks_list = []
    # set a variable to False: it will be used to re-execute the program multiple times
    ended = False

    # if the user did not insert a filename we start from an empty list
    filename = ""
    if (len(argv)>1):
        filename = argv[1]
        try:
            # open the file
            txt = open(filename)

            # read the file: load each row in an element of the list without "/n"
            tasks_list = txt.read().splitlines()

            # close the file
            txt.close()

        except IOError:
            print("File not found! We will start with an empty list")

    # keep asking strings until the user types 4 (to exit)
    while not ended:

        # print the menu every time we finish to perform an operation
        print("Insert the number corresponding to the action you want to perform")
        print("1: insert a new task")
        print("2: remove a task (by typing all its content)")
        print("3: show all existing tasks sorted in alphabetic order")
        print("4: close the program")

        # get the action as input
        string = input("Your choice:\n>")

        # check if the inserted string is actually a number
        # we will ask the user a new input until it will insert a number
        while string.isdigit() != True:
            # if the string is not a number we will ask a new input
            string = input("Wrong input! Your choice:\n>")

        # convert the string to int (integer number)
        choice = int(string)

        # depending on the chosen input we perform the right action
        if (choice == 1):  # insert a new task
            new_task(tasks_list)
        elif (choice == 2):  # remove a task
            remove_task(tasks_list)
        elif (choice == 3):  # show the list of tasks
            print_sorted_list(tasks_list)
        elif (choice == 4):  # exit
            ended = True

    # if user inserted the character "4", we save results on file
    if (ended and filename!=""):
        try:
            # open file in write mode
            txt = open(filename, "w")

            # write each task as a new line in the file (write will automatically empty the file)
            for single_task in tasks_list:
                txt.write(single_task+"\n")

            # close the file
            txt.close()

        except IOError:
            print("Problems in saving todo list to file")
