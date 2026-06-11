# Automated File Organizer:

A project to automating the process of organizing files into specific folders. These folders are created to store files of same type.

## Intoduction:

This project is created to automate the process of organizing the file in our system using a "Python script". The python script given can perform functions such as:
* Continuous monitoring of the specified path provided by the user to organize and allocate a set of unsorted files into sorted folder.
* Organiztion of the files is done by reading the "extention" of each file and allocating them to a folder named as the same file extention which is being sorted(Example: If a file having ".png" is being sorted then it is stored in the folder named "png").
* The program creates new folders to store specific file extention if it was not already avalable this means the program is designed to handle any type of file formate.
* The monitoring is scheduled to take place in an interval of 5 seconds to avoid infinite iteration.

This project helps users simplify a monotonous task such as file organiztion and improves efficiency of an individual.

## Modules used:
* https://docs.python.org/3/library/os.html
* https://docs.python.org/3/library/shutil.html
* https://docs.python.org/3/library/time.html

## Output (Video):


https://github.com/user-attachments/assets/9f262dd5-d2ac-4286-93ce-5e11ca7834f9

## Output (Images):
Before running the script:
<img width="840" height="741" alt="Screenshot 2026-06-12 013022" src="https://github.com/user-attachments/assets/2c73ba38-83ef-4f5f-83a2-aa10d11a2542" />

After running the script:
<img width="843" height="742" alt="Screenshot 2026-06-12 012842" src="https://github.com/user-attachments/assets/03f96c21-ce42-4f63-b498-2dc297b0ccae" />

## Issues:
* Over utilisation of CPU resources
* Unavailability of set times for program execution (Example: script executed as a shartup program to avoid endless execution and resource usage.)
* Unable to handle files that is being used by another programs.
* Cannot handle multiple extensions in a single file.
