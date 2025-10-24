#!/usr/bin/python3

# INET4031
# Tai Nguyen
# 10/24/2025
# 10/24/2025

# Module that allows the file to interact, read, and write the folders and files of the operating system
import os
# Short for regular, imports regular expressions that help look for strings that match the exact input
import re
# Allows for the file to interact with the Python interperter and the operating system
import sys

def main():
    for line in sys.stdin:

        # The re.match command indetifies the given string and ensures that the first character in the string is a '#'.
        match = re.match("^#",line)

        #This line checks the inputted string and splits it every single time a ':' is present. It also removes all the newlines from the string.
	# It also assigns the new string into the variable 'fields'
        fields = line.strip().split(':')

        #If checks if the input variable(s) meets the given condition(s). The first condition checked is if the first character was '#'.
	#The second condition is if the inputted string was split 5 times (username, password, etc.). The program will continue if
	# there is no '#" or if there are 5 lines of data after removing the ':'. Either condition being true will make the program halt.
        if match or len(fields) != 5:
            continue

        #After the string is split, it takes the first line and assigns it to the username. Second is the password. Inputs 3 and 4 are user
	#info that gets assigned to gecos.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # The last input may have multiple groups within it. The split command identifies all the commas, splits each individual group
	# and puts it into the groups variable.
        groups = fields[4].split(',')

        #To show to the end user that their input was valid and the newuser is being created.
        print("==> Creating account for %s..." % (username))
        # This command calls the adduser command, disables the password, and enters the user data into gecos. The new user is created.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #These commands will enable the script to actually make changes into the operating system and make real user accounts. This is commented
	# out for now to test that the inital input actually worked before it made actual changes.
        print (cmd)
        os.system(cmd)

        #This print statement tells the end user that their password is being added to the account.
        print("==> Setting the password for %s..." % (username))
        #This command enables the given password from earlier and sets it into the newly created account.Password is given twice to ensure
	#the correct password was added. 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # These commands will enable the script to actually make changes into the operating system and make real accounts. This is commented
	#out for now to test that the inital input actually worked before it made actual changes.
        print (cmd)
        os.system(cmd)

        for group in groups:
            # An invalid group would be something with no characters or simply a '-'. This checks if the passed group is not empty.
		#If it is not empty, it will assign the user to the group that was given.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print (cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
