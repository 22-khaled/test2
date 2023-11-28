import email
import streamlit as st
import pandas as pd
from time import ctime as t# Your data dictionaries
from PIL import Image
sea_food={'Real Maine lobster':4.5, 'Swordfish steak': 3.00, 'Salmon':3.75, 'Blue crab': 3.25, 'Gravadlax': 3.5, 'Fried catfish': 3.00, 'Shrimp Po\'Boy':4.0, 'Snakehead fish':3.5}
soups={'Cream Soup':1.65, 'Puree Soup':1.50,'Bisque':1.50, 'Chowder Soup': 2.00, 'Veloute Soup':1.75}# Define other dictionaries similarly
rice={'Mansaf':3.00, 'Mandi':2.0, 'Ozi':2.00, 'Kabseh':2.00, 'White rice':1.75}
departments={'sause':['ketchup', 'mionaze', 'garlic sause']
             ,'salts':['fruit salt', 'normal salt', 'tona salt'],
             'breakfast':['fried egg', 'coffee', 'donut', 'croissant', 'pancake', 'toast', 'bread', 'orange juice'],
             'meals':['shawerma', 'italy', 'french', 'brousted', 'burger'],
             'sandwitches':['shawerma', 'burger', 'mexico', 'fajeta'],
             'beverages':['pepsi', 'sprit', 'fanta', 'pepsi dite'],
             'family_meals':['3 persons meal', '6 persons meal', '10 persons meal'],
             'snacks':['wedgs potatos', 'potatos', 'onion circles', 'modzarella fingers', 'yoghurt'],
             'sea_food':['Real Maine lobster', 'Swordfish steak', 'Salmon', 'Blue crab', 'Gravadlax', 'Fried catfish', 'Shrimp Po\'Boy', 'Snakehead fish'],
             'soups':['Cream Soup', 'Puree Soup', 'Bisque', 'Chowder Soup', 'Veloute Soup'],
             'rice':['Mansaf', 'Mandi', 'Ozi', 'Kabseh', 'White rice']}
salads={'fruit salads':1.25, 'normal salads':0.75, 'tona salads':1.15}
sause={'ketchup':0.10, 'mionaze':0.25, 'garlic sause':0.35}
snacks={'wedgs potatos': 1.00, 'potatos': 0.85, 'onion circles':0.25, 'modzarella fingeers':0.80, 'yoghurt':0.5}
family_meals={'3 persons meal': 5.5, '6 persons meal':9.5, '10 persons meal': 15}
basket={'item':[], 'amount':[], 'unit price':[], 'total price':[]}
beverages={'pepsi':0.30,'sprite':0.3,'fanta':0.3, 'pepsi dite':0.35}
breakfast={'fried egg':0.75 ,'coffee':0.60, 'donut':0.50, 'croissant':0.65, 'pancake':1.25, 'toast':0.35, 'bread':0.25, 'orange juice':1.00}
sandwitches={'shawerma':0.6, 'burger':0.75, 'mexico':1.0, 'fajeta':1.25}
meals={'shawerma':1.50, 'italy':2.0, 'french':2.0, 'brousted':2.75}
new_products={}
information={'email':[], 'passward':[], 'Phone Number':[], 'C/E':[], 'address':[]}
finv={'id':[], 'item':[], 'amount':[], 'unit price':[],'total price':[]}
invoice={'inv_id':[0], 'time':[], 'total':[]}
resturant={'notes':[]}








import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader


# Create a Streamlit app
def display_items(category, items):
    st.header(f"{category} Menu")

    col1, col2 = st.columns(2)

    for item in items:
        with col1, col2:
            image = Image.open(item['image_path'])
            st.image(image, caption=item['caption'])
            if st.button(f"{item['name']} - {item['price']} JD"):
                # Handle button click action here
                if st.button(f"{item['name']} - {item['price']} JD"):
                    # Handle button click action here
                    pass

# Categories
seafood_items = [
    {"name": "Real Maine Lobster", "image_path": r"C:\Users\Dell\hello\Real_Maine_lobster.jpg", "caption": "Real Maine Lobster", "price": 4.50},
    {"name": "Swordfish steak", "image_path": r"C:\Users\Dell\hello\Swordfish steak.jpg", "caption": "Swordfish steak", "price": 3.00},
    {"name": "Salmon", "image_path": r"C:\Users\Dell\hello\Salmon.jpg", "caption": "Salmon", "price": 3.75},
    {"name": "Blue_crab", "image_path": r"C:\Users\Dell\hello\Blue crab.jpg", "caption": "Blue crab", "price": 3.25},
    {"name": "Gravadlax", "image_path": r"C:\Users\Dell\hello\Gravadlax.jpg", "caption": "Gravadlax", "price": 3.5},
    {"name": "Fried_catfish", "image_path": r"C:\Users\Dell\hello\Fried catfish.jpg", "caption": "Fried catfish", "price": 4.25},
    {"name": "Shrimp_PoBoy", "image_path": r"C:\Users\Dell\hello\Shrimp Po'Boy.jpg", "caption": "Shrimp PoBoy", "price": 4.00},
    {"name": "Snakehead_fish", "image_path": r"C:\Users\Dell\hello\Snakehead fish.jpg", "caption": "Snakehead fish", "price": 2.75},
    # Add more items as needed
]

soup_items = [
    {"name": "Cream soup", "image_path": r"C:\Users\Dell\hello\Cream Soup.jpg", "caption": "Cream soup", "price": 1.65},
    {"name": "Puree Soup", "image_path": r"C:\Users\Dell\hello\Puree Soup.jpg", "caption": "Puree Soup", "price": 1.50},
    {"name": "Bisque", "image_path": r"C:\Users\Dell\hello\Bisque.jpg", "caption": "Bisque", "price": 2.00},
    {"name": "Chowder_Soup", "image_path": r"C:\Users\Dell\hello\Chowder Soup.jpg", "caption": "Chowder Soup", "price": 2.50},
    {"name": "Veloute_Soup", "image_path": r"C:\Users\Dell\hello\Veloute Soup.jpg", "caption": "Veloute Soup", "price": 3.35},
    # Add more items as needed
]

Rice_Meals = [
    {"name": "Mansaf", "image_path": r"C:\Users\Dell\hello\Mansaf.jpg", "caption": "Mansaf", "price": 3.00},
    {"name": "Mandi", "image_path": r"C:\Users\Dell\hello\Mandi.jpg", "caption": "Mandi", "price": 2.75},
    {"name": "Ozi", "image_path": r"C:\Users\Dell\hello\Ozi.jpg", "caption": "Ozi", "price": 2.50},
    {"name": "Kabseh", "image_path": r"C:\Users\Dell\hello\Kabseh.jpg", "caption": "Kabseh", "price": 2.50},
    {"name": "White_rice", "image_path": r"C:\Users\Dell\hello\White rice.jpg", "caption": "White_rice", "price": 2.00},
    # Add more items as needed
]

Salads = [
    {"name": "fruit_salad", "image_path": r"C:\Users\Dell\hello\fruit salad.jpg", "caption": "fruit_salad", "price": 2.50},
    {"name": "Salad", "image_path": r"C:\Users\Dell\hello\Salad.jpg", "caption": "Salad", "price": 1.75},
    {"name": "tona_salad", "image_path": r"C:\Users\Dell\hello\tona salad.jpg", "caption": "tona_salad", "price": 2.25},
    # Add more items as needed
]

Snacks = [
    {"name": "Wedges_potato", "image_path": r"C:\Users\Dell\hello\wedges potatos.jpg", "caption": "Wedges potato", "price": 1.50},
    {"name": "French_Fries", "image_path": r"C:\Users\Dell\hello\French Fries.jpg", "caption": "French_Fries", "price": 1.25},
    {"name": "Onion_rings", "image_path": r"C:\Users\Dell\hello\Onion rings.jpg", "caption": "Onion_rings", "price": 1.00},
    {"name": "Mozzarella_fingers", "image_path": r"C:\Users\Dell\hello\Mozzarella fingers.jpg", "caption": "Mozzarella_fingers", "price": 2.00},
    # Add more items as needed
]

Juices = [
    {"name": "orange_juice", "image_path": r"C:\Users\Dell\hello\orange juice.jpg", "caption": "orange_juice", "price": 1.50},
    {"name": "apple_juice", "image_path": r"C:\Users\Dell\hello\apple juice.jpg", "caption": "apple_juice", "price": 1.75},
    {"name": "pomegranate_juice", "image_path": r"C:\Users\Dell\hello\pomegranate juice.jpg", "caption": "pomegranate_juice", "price": 2.25},
    {"name": "watermelon_juice", "image_path": r"C:\Users\Dell\hello\watermelon juice.jpg", "caption": "watermelon_juice", "price": 2.00},
    # Add more items as needed
]

Breakfast = [
    {"name": "fried_eggs", "image_path": r"C:\Users\Dell\hello\fried egg.jpg", "caption": "fried_eggs", "price": 1.50},
    {"name": "coffee", "image_path": r"C:\Users\Dell\hello\coffee.jpg", "caption": "coffee", "price": 1.10},
    {"name": "donut", "image_path": r"C:\Users\Dell\hello\donut.jpg", "caption": "donut", "price": 1.00},
    {"name": "croissant", "image_path": r"C:\Users\Dell\hello\croissant.jpg", "caption": "croissant", "price": 1.35},
    {"name": "pancake", "image_path": r"C:\Users\Dell\hello\pancake.jpg", "caption": "pancake", "price": 2.5},
    {"name": "toast", "image_path": r"C:\Users\Dell\hello\toast.jpg", "caption": "toast", "price": 1.75},
    {"name": "bread", "image_path": r"C:\Users\Dell\hello\bread.jpg", "caption": "bread", "price": 0.75},
    # Add more items as needed
]

Sandwiches = [
    {"name": "Shawerma_sandwich", "image_path": r"C:\Users\Dell\hello\Shawerma sandwich.jpg", "caption": "Shawerma_sandwich", "price": 1.50},
    {"name": "burger_sandwich", "image_path": r"C:\Users\Dell\hello\burger sandwich.jpg", "caption": "burger_sandwich", "price": 1.10},
    {"name": "mexico_sandwich", "image_path": r"C:\Users\Dell\hello\mexico sandwich.jpg", "caption": "mexico_sandwich", "price": 1.00},
    {"name": "fajeta_sandwich", "image_path": r"C:\Users\Dell\hello\fajeta sandwich.jpg", "caption": "fajeta_sandwich", "price": 1.35},
    # Add more items as needed
]

Sauses = [
    {"name": "ketchup", "image_path": r"C:\Users\Dell\hello\ketchup.jpg", "caption": "ketchup", "price": 0.00},
    {"name": "mionaze", "image_path": r"C:\Users\Dell\hello\mionaze.jpg", "caption": "mionaze", "price": 0.00},
    {"name": "garlic", "image_path": r"C:\Users\Dell\hello\garlic.jpg", "caption": "garlic", "price": 0.15},
    {"name": "honey_mustard", "image_path": r"C:\Users\Dell\hello\honey mustard.jpg", "caption": "honey_mustard", "price": 0.20},
    # Add more items as needed
]


def main():
    st.title("Restaurant Menu")
    st.title("Order now!")
    video_path = r'C:\Users\Dell\hello\pexels-ron-lach-8879530 (2160p).mp4'
    video_file = open(video_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, format='video/mp4')

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)

    with col1:
        if st.button('Seafood'):
            display_items('Seafood', seafood_items)

    with col2:
        if st.button('Soups'):
            display_items('Soups', soup_items)

    with col3:
        if st.button('Rice_Meals'):
            display_items('Rice_Meals', Rice_Meals)

    with col4:
        if st.button('Salads'):
            display_items('Salads', Salads)

    with col5:
        if st.button('Snacks'):
            display_items('Snacks', Snacks)            
 
    with col6:
        if st.button('Juices'):
            display_items('Juices', Juices)   
   
    with col7:
        if st.button('Breakfast'):
            display_items('Breakfast', Breakfast)   
    
    with col8:
        if st.button('Sandwiches'):
            display_items('Sandwiches', Sandwiches)   

    with col9:
        if st.button('Sauses'):
            display_items('Sauses', Sauses)

if __name__ == "__main__":
    main()    
hashed_passwords = stauth.Hasher(['abc', 'def']).generate()  

with open(r'C:\Users\Dell\hello\pages\14_config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

if st.button('Login'):
    authenticator.login('Login', 'main')
    
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

if st.button('Reset password') and st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"], 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

if st.button('Registeration') and not st.session_state["authentication_status"]:
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)


if st.button('Forgot passward!'):
    try:
        username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password('Forgot password')
        if username_of_forgotten_password:
            st.success('New password to be sent securely')
            # Random password should be transferred to user securely
        else:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

if st.button('Forgot Username!'):
    try:
        username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username('Forgot username')
        if username_of_forgotten_username:
            st.success('Username to be sent securely')
            # Username should be transferred to user securely
        else:
            st.error('Email not found')
    except Exception as e:
        st.error(e)

if st.button('Update user details') and st.session_state["authentication_status"]:
    try:
        if authenticator.update_user_details(st.session_state["username"], 'Update user details'):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)

with open(r'C:\Users\Dell\hello\pages\14_config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)



st.header("New Products")
st.write(new_products)

st.header("Information")
st.write(information)

st.header("finv")
st.write(config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized'])

st.header("Inovice")
st.write(invoice)

st.header("Notes")
st.write(resturant)


import uuid
import pyttsx3

class Registration:
    def __init__(self, name):
        self.name = name
        self.information = {'email': [], 'passward': [], 'C/E': [], 'Phone Number': [], 'address': []}
        
    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()    

    def register(self, user_email):
     #   information = {'email': [],'passward': [],'C/E': [],'Phone Number': [],'address': []}
##st.sidebar.header("User Registration")
#user_email = st.sidebar.text_input("Email address")
#user_password = st.sidebar.text_input("Password", type="password")
        st.header("User Registration")
        user = user_email
        print('you have only 3 tries')
        # Wait for the text to be spoken


        for i in range (1, 4):
            pass1_key = f"password_{uuid.uuid4()}"
            pass1 = st.sidebar.text_input('Enter your password:', type="password", key=pass1_key)            
            
            pass2_key = f"password_confirmation_{uuid.uuid4()}"
            pass2 = st.sidebar.text_input('Enter your password again:', type="password", key=pass2_key)
            
            register_button_key = f"register_button_{uuid.uuid4()}"
            register_button = st.sidebar.button("Register", key=register_button_key)
            
            if register_button:
                if pass1==pass2:
                    number=st.sidebar.text_input('enter your number')
                    address=st.sidebar.text_input('enter your address')
                    self.information['passward'].append(pass1)
                    self.information['email'].append(user)
                    self.information['Phone Number'].append(number)
                    self.information['address'].append(address)

                    st.success("Registration successful")
                    engine = pyttsx3.init()
                    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech_OneCore\\Voices\\TTS_MS_EN-US_ZiraPro-11.0")
                    engine.say(f"Hello {user}, how are you")
                    engine.runAndWait()

                    info_button=st.sidebar.button("Information")
                    st.success(f'Welcome {user}')
                    # Wait for the text to be spoken
                    break
                else:
                    st.warning('Passwords do not match. Please try again.')
    def log_in(self):
        st.write(self.information['email'])
        email = st.sidebar.text_input('Enter your email address:')
        password = st.sidebar.text_input('Enter your password:', type="password", key="password_input_login")
        login_button = st.sidebar.button("Login")


        if login_button:
            if email in self.information['email']:
                ind = self.information['email'].index(email)
                if self.information['password'][ind] == password:
                    st.write(f'Welcome {email}')
                else:
                    st.write('Wrong authentication!')
                    st.write('Try again later')
            else:
                st.write('Email not found. Please register first.')

            #ind=information['email'].index(email)
            #while True :
                #if information['passward'][ind]==passward:
                   #st.write ('Welcome {}'.format(email))
                    
               # else:
                    #st.write('wrong enteration!!')
                   # st.write('try again later')
                  #  break
               # break
      

# Create the main Streamlit app
st.title("Restaurant Management System")

# Initialize your Registration class

#while True:
    # Run the registration and login methods based on user input
    #if st.sidebar.selectbox("Action", ["Register", "Log In", "Exit"]) == "Register":
        #registration.register()
    #elif st.sidebar.selectbox("Action", ["Register", "Log In", "Exit"]) == "Log":
       #registration.log_in()
    #elif st.sidebar.selectbox("Action", ["Register", "Log In", "Exit"]) == "Exit":
       #break
 
class Customer:
    def __init__(self):
        self
    def meals(self):
        print(pd.DataFrame([meals]))
        while True:
            pic=input('choose from the following meals/e for exit')
            if pic.lower() in meals.keys():
                size=str(input('enter size you want r/regular, m/medium, l/large'))
                if size.lower()=='m':
                    basket['unit price'].append(meals[pic]+0.35)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(meals[pic]+0.35)
                    basket['total price'].append(total_amount)
                elif size.lower()=='l':
                    basket['unit price'].append(meals[pic]+0.75)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(meals[pic]+0.75)
                    basket['total price'].append(total_amount)
                elif size.lower()=='r': 
                    basket['unit price'].append(meals[pic])
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*meals[pic]
                    basket['total price'].append(total_amount)
                
                else:
                    print('wrong enteration')
                    continue
                basket['item'].append(pic)

            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration')
                break
    def sandwitches(self):
        print(pd.DataFrame([sandwitches]))
        while True:
            pic=input('choose from the following sandwitches/e for exit')
            if pic.lower() in sandwitches.keys():
                size=str(input('enter size you want r/regular, m/medium, l/large'))
                if size.lower()=='m':
                    basket['unit price'].append(sandwitches[pic]+0.3)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(sandwitches[pic]+0.3)
                    basket['total price'].append(total_amount)
                elif size.lower()=='l':
                    basket['unit price'].append(sandwitches[pic]+0.6)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(sandwitches[pic]+0.6)
                    basket['total price'].append(total_amount)
                elif size.lower()=='r': 
                    basket['unit price'].append(sandwitches[pic])
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*sandwitches[pic]
                    basket['total price'].append(total_amount)
                else:
                    print('wrong enteration')
                    continue
                basket['item'].append(pic)

            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration')
                
                break
                
    def beverages(self):
        print(pd.DataFrame([beverages]))
        while True:
            pic=input('choose from the following beverages/e for exit')
            if pic.lower() in beverages.keys():
                size=str(input('enter size you want r/regular, m/medium, l/large'))
                if size.lower()=='m':
                    basket['unit price'].append(beverages[pic]+0.20)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(beverages[pic]+0.20)
                    basket['total price'].append(total_amount)
                elif size.lower()=='l':
                    basket['unit price'].append(beverages[pic]+0.35)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(beverages[pic]+0.35)
                    basket['total price'].append(total_amount)
                elif size.lower()=='r': 
                    basket['unit price'].append(beverages[pic])
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*beverages[pic]
                    basket['total price'].append(total_amount)
                else:
                    print('wrong enteration')
                    continue
                basket['item'].append(pic)

            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration')
                break
    def salts(self):
        print(pd.DataFrame([salads]))
        while True:
            pic=input('choose from the following salts/e for exit')
            if pic.lower() in salads.keys():
                size=str(input('enter size you want r/regular, m/medium, l/large'))
                if size.lower()=='m':
                    basket['unit price'].append(salads[pic]+0.35)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(salads[pic]+0.35)
                    basket['total price'].append(total_amount)
                elif size.lower()=='l':
                    basket['unit price'].append(salads[pic]+0.75)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(salads[pic]+0.75)
                    basket['total price'].append(total_amount)
                elif size.lower()=='r': 
                    basket['unit price'].append(salads[pic])
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*salads[pic]
                    basket['total price'].append(total_amount)
                else:
                    print('wrong enteration')
                    continue
                basket['item'].append(pic)

            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration')
                break
    def sause(self):
        print(pd.DataFrame([sause]))
        while True:
            pic=input('choose from the following beverages/e for exit')
            if pic.lower() in sause.keys():
                size=str(input('enter size you want r/regular, m/medium, l/large'))
                if size.lower()=='m':
                    basket['unit price'].append(sause[pic]+0.20)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(sause[pic]+0.20)
                    basket['total price'].append(total_amount)
                elif size.lower()=='l':
                    basket['unit price'].append(sause[pic]+0.35)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(sause[pic]+0.35)
                    basket['total price'].append(total_amount)
                elif size.lower()=='r': 
                    basket['unit price'].append(sause[pic])
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*sause[pic]
                    basket['total price'].append(total_amount)
                else:
                    print('wrong enteration')
                    continue
                basket['item'].append(pic)

            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration')
                break
    def family_meals(self):
        print('you will got 1 leter pepsi for each meal')
        print(pd.DataFrame([family_meals]))
        while True:
            pic=input('choose from the following meals/e for exit')
            if pic.lower() in family_meals.keys():
                basket['item'].append(pic)
                basket['unit price'].append(family_meals[pic])
                am=int(input('enter amount you want'))
                basket['amount'].append(am)
                total_amount=am*family_meals[pic]
                basket['total price'].append(total_amount)
            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration')
                continue
    def snacks(self):
        print(pd.DataFrame([snacks]))
        while True:
            pic=input('choose from the following snacks/e for exit')
            if pic.lower() in snacks.keys():
                size=str(input('enter size you want r/regular, m/medium, l/large'))
                if size.lower()=='m':
                    basket['unit price'].append(snacks[pic]+0.35)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(snacks[pic]+0.35)
                    basket['total price'].append(total_amount)
                elif size.lower()=='l':
                    basket['unit price'].append(snacks[pic]+0.65)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(snacks[pic]+0.65)
                    basket['total price'].append(total_amount)
                elif size.lower()=='r': 
                    basket['unit price'].append(snacks[pic])
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*snacks[pic]
                    basket['total price'].append(total_amount)
                else:
                    print('wrong enteration')
                    continue
                basket['item'].append(pic)

            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration')
                break 
    def breakfast(self):
        print(pd.DataFrame([breakfast]))
        while True:
            pic=input('choose from the breakfast department/e for exit')
            if pic.lower() in breakfast.keys():
            
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*breakfast[pic]
                    basket['total price'].append(total_amount)
                

            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration, try again')
                continue                     
    def newproducts(self):
        print(pd.DataFrame([new_products]))
        while True:
            pic=input('choose from the following items/e for exit')
            if pic.lower() in new_products.keys():
                size=str(input('enter size you want r/regular, m/medium, l/large'))
                if size.lower()=='m':
                    basket['unit price'].append(new_products[pic]+0.35)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(new_products[pic]+0.35)
                    basket['total price'].append(total_amount)
                elif size.lower()=='l':
                    basket['unit price'].append(new_products[pic]+0.65)
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*(new_products[pic]+0.65)
                    basket['total price'].append(total_amount)
                elif size.lower()=='r': 
                    basket['unit price'].append(new_products[pic])
                    am=int(input('enter amount you want'))
                    basket['amount'].append(am)
                    total_amount=am*new_products[pic]
                    basket['total price'].append(total_amount)
                else:
                    print('wrong enteration')
                    continue
                basket['item'].append(pic)

            elif pic.lower()=='e':
                print('thx for join us')
                break
            else:
                print('wrong enteration')
                break         
    def notes(self):
        #if u have any note to become better market wrote it below
        notes=input('if you have any notes write it below: \n')
        with open('readme.txt', 'w') as f:
            f.write(notes)
            print('Thank you for join us')
            resturant['notes'].append(notes)

    def show_bill(self):
        import pandas as pd
        basket1=pd.DataFrame(basket)
        
        print(basket1)

    def remove_item(self):
        while True:
            ch=str(input('enter item name: '))
            if ch in basket['item']:
                basket['item'].pop()
                basket['amount'].pop()
                basket['unit price'].pop()
                basket['total price'].pop()
                
                break
            else:
                print('item not found, rewrite again')

    def inv(self):
        a=invoice['inv_id'][-1]+1
        for i in range(0,len(basket['amount'])):
            finv['id'].append(a)
            finv['item'].append(basket['item'][i])
            finv['amount'].append(basket['amount'][i])
            finv['unit price'].append(basket['unit price'][i])
            finv['total price'].append(basket['amount'][i]*basket['unit price'][i])
            
        time = t()
        invoice['time'].append([time])
        x=pd.DataFrame(finv)
        print(x)
        print('Thanks for join us ')

class Employee:
    def __init__(self, kst):
        self.kst = kst

    def Creat_dep(self):
        while True:
            dep = st.text_input('Enter department name to create (E for exit):')
            if dep in departments.keys():
                st.write('Department already exists')
            elif dep.lower() == 'e':
                break
            departments.update({dep: []})

    def add_product(self):
        dep = st.selectbox('For which department do you want to add a product?', list(departments.keys()))
        if dep in departments.keys():
            p_name = st.text_input('Enter the product name you want to add:')
            if p_name in departments.keys():
                st.write('Product already exists')
            p_price = st.number_input('Enter product price (Format: 9.99 JD): ')
            departments[dep].append(p_name)
            new_products.update({p_name: p_price})
            st.write('Product added successfully')

    def edit(self):
        ch = st.text_input('Enter "p" to edit a product or "E" to exit:')
        while True:
            if ch.lower() == 'p':
                st.write(departments.keys())
                x = st.selectbox("From which department do you want to edit?", list(departments.keys()))
                if x.lower() == '1':
                    p_name = st.text_input('Enter product name:')
                    if p_name in meals:
                        n_price = st.number_input('Enter new price (Format: 9.99 JD) or E')
                        meals[p_name] = n_price
                        st.write('Successfully done')
                    # Implement similar sections for other departments
                elif x.lower() == 'e':
                    break
                else:
                    st.write('Wrong entry!')
                    break
            elif ch.lower() == 'e':
                st.write('Exit...')
                break
            break


    # Run the registration and login methods based on user input
    #if st.sidebar.selectbox("Action", ["Register", "Log In", "Exit"]) == "Register":
        #registration.register()
    #elif st.sidebar.selectbox("Action", ["Register", "Log In", "Exit"]) == "Log":
       #registration.log_in()
    #elif st.sidebar.selectbox("Action", ["Register", "Log In", "Exit"]) == "Exit":
       #break

def main():
    registration = Registration('khaled')
    action = st.sidebar.selectbox("Action", ["Register", "Log In", "Exit"])
    if action == "Register":
        user_email = st.sidebar.text_input('Email Address to Sign Up')
        registration.register(user_email)
        manage1()
        st.write(f'Welcome {user_email}')
    elif action == "Log In":
        registration.log_in()
        manage1()
        st.write(f'Welcome {email}')
    elif action == "Exit":
        st.write("Goodbye")
        
def manage1():
    # Implement the rest of your code here using Streamlit widgets
    while True:
        c = st.selectbox("Are you a CUSTOMER, EMPLOYEE, or EXIT", ("CUSTOMER", "EMPLOYEE", "EXIT"))
        
        if c == "CUSTOMER":
            al = Customer()
            information['C/E'].append('customer')
            # Implement the customer interactions using Streamlit widgets
            while True:
                cho = st.selectbox("Choose from the following options:", (
                    "meals", "sandwitches", "snacks", "new_products", "family meals", "salts", 
                    "sause", "beverages", "breakfast", "show bill / remove items", "invoice", "add notes", "exit"
                ))
                
                if cho == "meals":
                    # Implement the meals interaction using Streamlit widgets
                    st.write("The mentioned price is for a regular meal...")
                    al.meals()
                elif cho == "sandwitches":
                    # Implement the sandwiches interaction using Streamlit widgets
                    st.write("The mentioned price is for a regular sandwich...")
                    al.sandwitches()
                elif cho == "snacks":
                    # Implement the snacks interaction using Streamlit widgets
                    st.write("The mentioned price is for a regular snack...")
                    al.snacks()
                # Implement other options in a similar manner
                
                elif cho == "exit":
                    st.write("Goodbye")
                    break

        elif c == "EMPLOYEE":
            # Implement the employee interactions using Streamlit widgets
            for i in range(1, 4):
                pa = st.text_input('Enter employee passcode (3 attempts):')
                if pa == 'KST':
                    information['C/E'].append('employee')
                    st.write('WELCOME')
                    j = Employee('kst')
                    while True:
                        cho = st.selectbox("Choose from the following options:", (
                            "create department", "add products", "edit price", "show customer information", "show items", "exit"
                        ))
                        if cho == "create department":
                            j.Creat_dep()
                        elif cho == "add products":
                            j.add_product()
                        # Implement other employee options similarly
                        elif cho == "exit":
                            st.write("Goodbye")
                            break
                        else:
                            st.write('Wrong entry!')
                            break
                elif pa.lower() == 'e':
                    break
                else:
                    st.write('Wrong passcode!')

        elif c.lower() == "exit":
            kh = Registration('khaled')

            a = st.selectbox("Sign up, Login, or Exit", ("sign up", "login", "exit"))
            if a.lower() == 'sign up':
                kh.register()
            elif a.lower() == 'login':
                kh.log_in()
            elif a.lower() == 'exit':
                st.write("Goodbye")
        
        else:
            st.write('Wrong entry!')


if __name__ == '__main__':
    main()
