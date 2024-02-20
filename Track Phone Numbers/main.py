import phonenumbers
from phonenumbers import geocoder
dodo = phonenumbers.parse("+90 534 212 03 35")
ege = phonenumbers.parse("+90 553 672 99 43")
serap = phonenumbers.parse("+90 535 549 28 75")
nardane = phonenumbers.parse("+994 77 635 68 06")
tayfun = phonenumbers.parse("+1 770 479 58 55")
kemah_sitayla = phonenumbers.parse("+90 216 343 28 75")


print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(dodo, "tr"))
print(geocoder.description_for_number(ege, "tr"))
print(geocoder.description_for_number(serap, "tr"))
print(geocoder.description_for_number(nardane, "tr"))
print(geocoder.description_for_number(tayfun, "tr"))
print(geocoder.description_for_number(kemah_sitayla, "tr"))
