#A program that gives you a random hobby from a pool
import random

hobby_list=[]
list1 = open('Hobby_list.txt')
list1.close()

with open('Hobby_list.txt') as file:
    for line in file:
        hobby_list.append(line.strip()) #stripping the new character line from each line


#making a list that we can add hobbies to

def get_random_hobby():
    '''returns a random hobby from the list'''
    return random.choice(hobby_list)

def get_random_hobby_different(hobby_list,x):
    while True:
        random.hobby = random.choice(hobby_list)
        if random.hobby != x: # checks that the new hobby is different from the first hobby x
            print(random.hobby, '\n Are you satisfied? press y for yes, n for no and anything else to go back')
            y = input()
            if y == 'y':
                return random.hobby # returns the value of the random hobby
            elif y == 'n':
                continue
            else:
                return
        else:
            continue

def append_hobby_list(hobby_list):
    '''allows the user to append to the list'''
    z = 1
    for i in hobby_list: # this lets the user see the hobby list
        print(z,i)
        z= z + 1 
    hobby = input('What hobby would you like to add? Press q to go back ')
    if hobby == 'q':
        return
    else:
        hobby_list.append(hobby)

def remove_hobby_list(hobby_list):
    '''allows the user to remove from the list'''
    z = 1
    for i in hobby_list: # this lets the user see the hobby list
        print(z,i)
        z= z + 1
    while True:
        try: #checks that the user typed in the correct input
            hobby = int(input('What hobby would you like to remove? Press 0 to go back '))
            if hobby == 0:
                break
        except ValueError:
            print('Please type a number')
    if hobby == 0:
        return
    else:
        try:
            del hobby_list[hobby-1] # deletes from the hobby list
            z = 1
            for i in hobby_list: # shows the new updated list
                print(z,i)
                z= z + 1
            with open('Hobby_list.txt','w') as file:
                for hobby in hobby_list:
                    file.write(f'{hobby}\n')
        except IndexError:
            print('There are no hobbies to remove')


def main():
    '''main menu for the application'''
    while True:
        if not hobby_list: # if the list is empty
            '''The program requires at least 1 hobby in the list'''
            first_hobby = input('Please introduce a hobby to start ')
            if first_hobby.strip():
                hobby_list.append(first_hobby)
                break
        else: #in case the list isnt empty
            break

    x = get_random_hobby()
    while True:
        '''main loop for the menu'''
        try:
            command = int(input(
            '''What would you like to do? \n 
            1.Get random hobby \t 
            2.Get random hobby different from previous (press q at any time to exit) \t 
            3.Add a hobby \t 
            4.Remove a hobby \t 
            5. quit \n'''))
        except ValueError:
            print('Please use a number')
            continue #prevents future errors
        if command == 1:
            print(x)
        elif command == 2:
            get_random_hobby_different(hobby_list, x)
        elif command == 3:
            append_hobby_list(hobby_list)
        elif command == 4:
            remove_hobby_list(hobby_list)
        elif command == 5:
            with open('Hobby_list.txt','w') as file:
                for hobby in hobby_list:
                    file.write(f'{hobby}\n')
            break

if __name__ == '__main__':
    main()