"""Test for mailroom"""
import os
import time
import pytest
from donor_models import Donor, DonorCollection

p1, p2 = Donor('Mo'), Donor('Larry')
p2.add_donation(20)
p1.add_donation(4, 2)
dt = DonorCollection()
dt.add_donors(p1, p2)

def test_create_donor():
    """Test create of donor"""
    assert p1._name == 'Mo'
    assert p2._name == 'Larry'

def test_add_donation():
    """Test donation added"""
    assert p1._donations[1] == 2

def test_math():
    """Test math: total, num, avg"""
    assert p1.d_tot == 6
    assert p1.d_num == 2
    assert p1.d_avg == 3

def test_add_donors():
    """Test adding donor to list"""
    assert len(dt.list_donors) == 2
    assert dt.list_donors[0].name == 'Mo'
    assert dt.list_donors[0].donations[1] == 2
    assert dt.list_donors[1].name == 'Larry'
    assert dt.list_donors[1].donations[0] == 20
    assert dt.find_donor('Karen') is None
    assert dt.find_donor('Mo') is not None
    assert dt.find_donor('mo') is not None

def test_thanks_mass():
    """send thanks to everyone message"""
    my_str1 = dt.write_thanks_all(name=p1._name,
                                  total=p1.d_tot,
                                  numb=p1.d_num).strip()
    assert 'Mo' in my_str1
    assert '6' in my_str1
    assert 'totaling' in my_str1
    my_str2 = dt.write_thanks_all(name=p2._name,
                                  total=p2.d_tot,
                                  numb=p2.d_num).strip()
    assert 'Larry' in my_str2
    assert '20' in my_str2
    assert 'totaling' not in my_str2

def test_thanks_export():
    """send thanks to everyone export"""
    dt.thanks_all()
    parent = os.getcwd()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(parent, timestr + "letter/" + 'Mo.txt')
    assert os.path.exists(filename)

def test_thanks_1addition():
    """send thanks to single donor for single donation"""
    expected = (f"""
Dear Larry,
Thank you for your very kind donation of $90.00
It will be put to very good use.
Sincerely,
-The Team""")
    dc = DonorCollection()
    r1 = 'Larry'
    donor_new = Donor(r1)
    dc.add_donors(donor_new)
    donor1 = donor_new
    donor1.add_donation(40, 50)
    assert donor1.send_thank_you(donor1.d_tot) == expected

def test_donor_collection():
    """test donor collection"""
    dc = DonorCollection()
    assert isinstance(dc, DonorCollection)

def test_sort():# using above 'donors_db' data base
    """test donors are sorted in descending order by totals"""
    sortlist = dt.sort_donors()
    assert sortlist[0]._name == 'Larry'
