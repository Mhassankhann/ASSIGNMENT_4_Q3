import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password, users):
    return users.get(email) == hash_password(password)

def main():
    users = {
        "user@example.com": hash_password("securepassword123"),
        "samad@gmail.com": hash_password("mysecretpass"),
    }

    email = input("Enter email: ")
    password = input("Enter password: ")

    print("✅ Login successful!" if login(email, password, users) else "❌ Login failed! Incorrect email or password.")

if __name__ == '__main__':
    main()
