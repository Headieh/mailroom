#!/usr/bin/env python3
"""main module"""
import sys
import re
#import io
#import os
#import webbrowser
import donor_models as dm

_DC = dm.DonorCollection()

def valid_money():
    """ensures valid dollar amount is inputted"""
    while True:
        r_1 = input("Please enter a donation amount ")
        try:
            amount = float(r_1)
            if amount < 0.01 or amount > 10000:
                print("Invalid value")
            else:
                return amount
        except ValueError:
            print("Invalid value")

def valid_name():
    """ensures valid name is inputted"""
    while True:
        r_1 = input("Please enter a full name ")
        r_2 = re.sub(r'[^a-zA-Z]+', '', r_1)
        if r_1 == '':
            print('No name entered')
        elif r_2 == '':
            print('Not a valid name')
        elif len(r_1) > 30:
            print('Use a nick name - your name is too long')
        else:
            return r_1

def thanks():
    """adds donation and sends a thanks message"""
    response1 = valid_name()
    if response1.lower() == 'list':
        print([i.name for i in _DC.list_donors])
        return
    else:
        amount = valid_money()

    if not amount: #if get donation returns nothing, return nothing back to main
        return
    else:
        donor1 = donor_check(response1)
        donor1.add_donation(amount)
        print(donor1.send_thank_you(amount))

def donor_check(r_1):
    """checks if its an existing donor or new"""
    the_donor = _DC.find_donor(r_1)
    if the_donor is None:
        donor_new = dm.Donor(r_1)
        _DC.add_donors(donor_new)
        return donor_new
    else:
        return the_donor

def original_prompt():
    """menu options"""
    answers = input(f"""
Choose an action:
1 - Send a Thank You to a single donor.
2 - Create a Report.
3 - Send letters to all donors.
4 - Quit
""")
    return answers

def main():
    """main prompt"""
    options = {
        1: thanks,
        2: report,
        3: thanks_all,
        4: quits
    }

    while True:
        try:
            resp = original_prompt()
            if int(resp) in options:
                options.get(int(resp))()
            else:
                print(' Input is invalid, please input a valid option. ')
        except ValueError:
            print(' Input is invalid, please input a valid option. ')

def quits():
    """Quit program"""
    print("Bye!")
    sys.exit()

def initial():
    """initializes the dataset"""
    d_1 = dm.Donor('Karen')
    d_2 = dm.Donor('Susan')
    d_3 = dm.Donor('Larry')
    d_4 = dm.Donor('Curly')
    d_5 = dm.Donor('Mo')
    d_1.add_donation(20, 20, 100)
    d_2.add_donation(20)
    d_3.add_donation(40, 50)
    d_4.add_donation(20.99, 20, 100)
    d_5.add_donation(2)
    _DC.add_donors(d_1, d_2, d_3, d_4, d_5)

def report():
    """displays donor report"""
    print(_DC.create_report_content())
    _DC.create_html_report()

def thanks_all():
    """sends thanks to everyone"""
    _DC.thanks_all()


if __name__ == "__main__":
    initial()
    main()
