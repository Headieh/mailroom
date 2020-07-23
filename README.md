# Mailroom Program

A Mailroom program using object-oriented programming

#Goal:

You work in the mail room at a local charity. Part of your job is to write incredibly boring, repetitive emails thanking your donors for their generous gifts. You are tired of doing this over and over again, so you’ve decided to let Python help you out of a jam and do your work for you.

#The Program

Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following tasks:

It should hold a list of your donors and the history of the amounts they have donated.
The script should prompt the user to choose from a menu: “Send a Thank You”, “Create a Report”, "thank all donors" or “quit”.

##Classes:

#Donor Class:
responsible for donor data encapsulation

This class will hold all the information about a single donor, and have attributes, properties, and methods to provide access to the donor-specific information that is needed. Any code that only accesses information about a single donor should be part of this class.

#DonorCollection Class:
responsible for donor collection data encapsulation

This class will hold all of the donor objects, as well as methods to add a new donor, search for a given donor, etc. If you want a way to save and re-load your data, this class would hold that method, too.

Your class for the collection of donors will also hold the code that generates reports about multiple donors.


#Send a Thank You

If the user selects “Send a Thank You” option, prompt for a Full Name.
If the user types list show them a list of the donor names and re-prompt.
If the user types a name not in the list, add that name to the data and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Convert the amount into a number, check for bogus amounts.
Add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.

#Send a thank you to all donors
Write a full set of letters to all donors to individual files on disk.
Go through all the donors in your donor data structure, generate a thank you letter for each donor, and write each letter to disk as a text file.

#Create a Report

If the user selected “Create a Report,” print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations, and average donation amount as values in each row.
After printing this report, return to the original prompt.

#Quit
From the original prompt, the user should be able to quit the script cleanly.
