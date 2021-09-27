from phonenumbers import geocoder
import phonenumbers
from test import number
ch_number= phonenumbers.parse('+41 69944848', 'CH')
print(geocoder.description_for_number(ch_number, 'en'))