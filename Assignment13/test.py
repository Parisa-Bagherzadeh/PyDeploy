import bcrypt

password = "salamparisa"
print(password)

password_byte = password.encode("utf-8")

hashed = bcrypt.hashpw(password_byte, bcrypt.gensalt())
print(hashed)


if bcrypt.checkpw(password_byte, hashed):
    print("It matches")
else:
    print("Not mathced")    
