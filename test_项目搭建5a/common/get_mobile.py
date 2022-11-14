
import faker

def get_mobile():

    fk=faker.Faker(locale=['zh_CN'])  #locale记得转中文

    return fk.phone_number()


a=get_mobile()
print(a)