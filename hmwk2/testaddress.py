from homework2 import addressbook

name_to_phone = {'alice': 5678982231, 'bob': '111-234-5678', 'christine': 5, 'daniel': '959-201-3198', 'edward': 6, 'buddy': 7}
name_to_address = {'alice': '11 hillview ave', 'bob': '25 arbor way', 'christine': '11 hillview ave', 'daniel': '180 ways court', 'edward': '11 hillview ave', 'buddy': '180 ways court'}
address_to_all = addressbook(name_to_phone, name_to_address)
print(address_to_all)