# Spring-2023-Final-Project

Video link: https://youtu.be/ByNkiFNYCVQ

Final Code: Found in repository under file name FinalTest.py


Some difficulties I faced when working on this project was storing the many input values which needed to be given by the user as well as needing to have a way in which the redirect the user back to the input if they entered an invalid input, without using a new function each time. Sometimes, however, it was necssary to embed a new function and have to use a variable from the previous function. I had some issues with this. An error would display which said the variable was not defined yet, when trying to use it in the new function. Because I needed to embed functions to allow the program to progress, returning a variable would not work as this would stop the function and, thus, the program. However, I solved this by using the idea that functions are also objects from https://stackoverflow.com/questions/10139866/calling-variable-defined-inside-one-function-from-another-function. I was able to solve the issue of redirecting the user back to the input by using Try and Except. When allowing the user to create the itinerary, I was also having issues with retrieving the correct tourist attraction from the dictionary. I solved this by creating a for loop to print out all of the locations and then converting this into a list under a new variable using the splitlines function.
