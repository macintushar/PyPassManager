from models import Passwords

data = Passwords.objects.all().values()
data = list(data)
data = data[0]
print(data)