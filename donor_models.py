""" Donor and Donor Clooection Classes responsible for donor data"""
import os
import time
import webbrowser
import io
from html_render import *

class Donor:
    """ Class responsible for donor data encapsulation"""

    def __init__(self, name):
        self._name = name
        self._donations = []

    @property
    def name(self):
        """name"""
        return self._name

    @property
    def donations(self):
        """donations"""
        return self._donations

    @property
    def d_num(self):
        """number of donations"""
        return len(self._donations)

    @property
    def d_tot(self):
        """sum of donations"""
        return sum(self._donations)

    @property
    def d_avg(self):
        """average donation"""
        if self.d_num == 0:
            return 0
        else:
            return self.d_tot/self.d_num

    def add_donation(self, *args):
        """add donation amount to a donor object"""
        for i in args:
            self._donations.append(i)

    def send_thank_you(self, money_amount):
        """Sends a thank you when donation is made"""
        return f"""
Dear {self._name},
Thank you for your very kind donation of ${money_amount:.2f}
It will be put to very good use.
Sincerely,
-The Team"""

class DonorCollection:
    """ Class responsible for donor collection data encapsulation """

    def __init__(self):
        """Create a collection of donors"""
        donors=[]
        self.donor_obs_list = donors

    @property
    def list_donors(self):
        """Return a list of all donors"""
        return self.donor_obs_list

    @list_donors.setter
    def list_donors(self, donors):
        """list of donors"""
        self.donor_obs_list.extend(donors)

    def find_donor(self, new_donor):
        """find donor in list"""
        return next((donor for donor in self.donor_obs_list
                     if(donor._name.lower() == new_donor.lower())
                     ), None)

    def add_donors(self, *args):
        """Add a donor to the collection."""
        self.list_donors.extend(args)
        return self.list_donors

    def thanks_all(self):
        """export thankyous for all"""
        parent = os.getcwd()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        os.mkdir(timestr+'letter')
        for k in self.list_donors:
            filename = os.path.join(parent, timestr+'letter' + "/" + k._name + '.txt')
            with open(filename, 'w') as file:
                file.write(self.write_thanks_all(k._name, k.d_tot, k.d_num))
        print("Letters have been outputted for all donors")

    def write_thanks_all(self, name, total, numb):
        """write thankyous for all"""
        mass_text_1 = f"""
        Dear {name},
        Thank you for your very kind donation of ${total:.2f}
        It will be put to very good use.
                               Sincerely,
                                  -The Team"""

        mass_text_2 = f"""
        Dear {name},
        Thank you for your very kind donations totaling ${total:.2f}
        It will be put to very good use.
                               Sincerely,
                                  -The Team"""

        if numb == 1:
            return mass_text_1
        else:
            return mass_text_2

    @staticmethod
    def sort_key(self):
        """sort key is total donation amt"""
        return (sum(self._donations), self._name)

    def sort_donors(self):
        """sort the donors by reversing the sortkey"""
        return sorted(self.donor_obs_list, key=DonorCollection.sort_key, reverse=True)

    def create_report_header(self):
        """report header"""
        title_formater = '{:<30}{:<15}{:<15}{:5}\n'
        col_labels = ["Donor Name",
                      "Total Given",
                      "Num Gifts",
                      "Average Gift"]
        title = title_formater.format(*col_labels)
        seperate_line = '-' * len(title)
        title = f"""
{title}
{seperate_line}

"""
        return title

    def create_report_content(self):
        """ prints a report of donors"""
        raw = []
        raw.append(self.create_report_header())
        for this_ob in self.sort_donors():
            name = this_ob._name
            num = this_ob.d_num
            total = this_ob.d_tot
            aveg = this_ob.d_avg
            if total > 1000000:
                raw.append(f"{name:<30}${total:<14.3e}{num:<15}${aveg:<4.3e}")
            else:
                raw.append(f"{name:<30}${total:<14.2f}{num:<15}${aveg:<4.2f}")
            raw.append('\n')
        return "".join(raw)

    def create_html_report(self):
        """ opens tab with a report of donors"""
        page = Html()
        head = Head()
        style = Style()
        style.append(Customer('#customers {border-collapse: collapse;\
         width: 50%;margin:auto;}'))
        style.append(Customer('#customers th {text-align: center; \
        color: c0c0c0; border-width: 1px 1px 4px 1px; border-style: solid;\
         border-color:black; padding: 8px; padding: 12px, 0, 12px, 0;}'))
        style.append(Customer('#customers tr:nth-child(even) {background-color:\
         white}'))
        style.append(Customer('#customers tr:nth-child(odd){background-color:\
         lightgrey}'))
        style.append(Customer('#customers td:nth-child(even) {text-align:\
         right}'))
        style.append(Customer('#customers td:nth-child(odd){text-align:\
         center}'))
        style.append(Customer('#customers td {border: 1px solid black;\
        padding: 8px;}'))
        style.append(Customer('body {background-image: \
        linear-gradient(to bottom right, white ,black);\
         background-repeat: no-repeat; width: 100vw; height: 100vh;}'))
        head.append(style)
        page.append(head)
        body = Body()
        body.append(H(1, 'Donation Report', style="font-style: oblique;\
         color: 9c9c9c; text-align:center;"))
        table = Table(id='customers')
        column_list = Tr()
        column_list.append(Th('Donor Name'))
        column_list.append(Th('Total Given'))
        column_list.append(Th('Num Gifts'))
        column_list.append(Th('Average Gifts'))
        table.append(column_list)

        for this_ob in self.sort_donors():
            donor_tr = Tr()
            name = this_ob._name
            num = this_ob.d_num
            total = this_ob.d_tot
            aveg = this_ob.d_avg
            donor_tr.append(Td(name))
            if this_ob.d_tot > 1000000:
                donor_tr.append(Td(f"${total:<14.3e}"))
            else:
                donor_tr.append(Td(f"${total:<14.2f}"))
            donor_tr.append(Td(f"{num:<15}"))

            if this_ob.d_avg > 1000000:
                donor_tr.append(Td(f"${aveg:<4.3e}"))
            else:
                donor_tr.append(Td(f"${aveg:<4.2f}"))
            table.append(donor_tr)

        body.append(table)
        page.append(body)

        parent = os.getcwd()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        os.mkdir(timestr+'report')
        filename = os.path.join(parent, timestr+'report' + '/donors_report.html')
        f = io.StringIO()
        page.render(f)
        html_content = f.getvalue()
        with open(filename, 'w') as outfile:
            outfile.write(html_content)
        if os.path.exists('/Applications/Safari.app'):
            os.system(f'open /Applications/Safari.app {filename}')
        else:
            webbrowser.open(filename) #this did not work for me on safari
