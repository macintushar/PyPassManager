import pyrebase
from hash import GeneratePassword, HashPassword, UnhashPassword

config = {
    "apiKey": "AIzaSyDNk2ypVy0tkTyQHN0Q5Mupf-H7YQco-Fw",
    "authDomain": "django-password-manager.firebaseapp.com",
    "databaseURL": "https://django-password-manager-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "django-password-manager",
    "storageBucket": "django-password-manager.appspot.com",
    "messagingSenderId": "465490596553",
    "appId": "1:465490596553:web:676fbbd48bd7393138b318",
    "measurementId": "G-1TM8K24P4K",
    "serviceAccount":"keys/.firebase-config.json"
  }

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def write_to_database(appName, category, email, password, url, username):
    data = {'app_name':appName,
        'category':category,
        'email':email,
        'password':password,
        'url':url,
        'username':username
        }
    database.child('Passwords').child('tushar').child(appName).set(data)

def retrieveSpecificPassword(appName):
    appDetails = database.child('Passwords').child('tushar').child(appName).get().val()
    print(appDetails)
    print(type(appDetails))

    keys = list(appDetails)
    print(keys)

    vals = list(appDetails.values())
    print(vals)

    appData = {}
    
    for key in keys:
        for val in vals:
            appData[key] = val
            vals.remove(val)
            break
    
    print("App Data:\n",appData)
    return appData

def retrieveAllPasswords():
    all_passwords = database.child('Passwords').child('tushar').get()
    for password in all_passwords.each():
        print("\n",password.key()) # Morty
        print(password.val())

def updatePassword(NewPassword):
    print("Hi")


retrieveSpecificPassword(appName="Google")

retrieveAllPasswords()

newPass = GeneratePassword()
encPass = HashPassword(newPass)
encPassStr = encPass.decode('latin-1')
encPassStr = str(encPassStr)
'''
write_to_database(appName="TestSite0", category="Email", 
    email="tusharkumar91111@gmail.com", password=encPassStr, 
    url="https://mail.google.com/", username="tusharkumar91111@gmail.com")
'''

appData = retrieveSpecificPassword(appName="TestSite0")
retPass = appData["password"]
print(retPass)

decPass = UnhashPassword(retPass.encode('latin-1'))
print(decPass)