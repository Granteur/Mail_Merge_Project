# Mail_Merge
Mail_Merge is written in Python. It uses a really simple letter template, and pulls from a list of names (familiar to fans of the classic Avatar the Last Airbender Show) to fill the templates with personalized letters.

## Purpose
Taking a break from recreating games, I am using this to both practice navigating through the file structure within Python code, but also to get some practice reading from and writing to files in Python.

## Description
Within the 'Input' folder, there is a 'Names' folder that contains an 'invited_names.txt' file with a list of names. Likewise, in the 'Letters' folder, there is a 'starting_letter.txt' file that has a letter template. The 'main.py' file reads information from these files storing their respective contents into two variables. A loop processes these variables and generates a new files in the /Output/ReadyToSend folder that combine the Input information to create personalized letters.