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


def find_urgent(tasks):
    '''
    Find a urgent task
    '''

    # init a new, empty dictionary
    urgents = {}

    # look for the urgent tasks
    for task in tasks.keys():
        if tasks[task]['urgent']:
            urgents[task] = tasks[task]

    # print the result
    print(urgents)


if __name__ == '__main__':
    # main program

    # prepare the dictionary
    task1 = {'todo': 'call John for AmI project organization', 'urgent': True}
    task2 = {'todo': 'buy a new mouse', 'urgent': True}
    task3 = {'todo': 'find a present for Angelina\'s birthday', 'urgent': False}
    task4 = {'todo': 'organize mega party (last week of April)', 'urgent': False}
    task5 = {'todo': 'book summer holidays', 'urgent': False}
    task6 = {'todo': 'whatsapp Mary for a coffee', 'urgent': False}
    tasks = {'task1':task1, 'task2':task2, 'task3':task3, 'task4':task4, 'task5':task5, 'task6':task6}

    #find urgent tasks in dictionary
    find_urgent(tasks)