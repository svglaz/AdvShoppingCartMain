from faker import Faker
fake = Faker(locale='en_CA')

# --------------------- Advantage Shopping Cart App DATA PARAMETERS ------------------------

app = 'Advantage Shopping Cart'
adv_shop_cart_url = 'https://advantageonlineshopping.com/#/'
adv_shop_cart_home_page_title = ' Advantage Shopping'
adv_create_account_page_url = 'https://advantageonlineshopping.com/#/register'
adv_myAccount_page_url = 'https://advantageonlineshopping.com/#/myAccount'
adv_MyOrders_page_url = 'https://advantageonlineshopping.com/#/MyOrders'

new_username = fake.user_name()[0:14]
new_password = fake.password()
email = fake.email()

first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone = fake.bothify(text='1-(###)-###-####')

country = fake.current_country()
city = fake.city()
address = fake.street_address()
state = fake.province_abbr()
postal_code = fake.postalcode()

subject = fake.sentence(nb_words=50)


