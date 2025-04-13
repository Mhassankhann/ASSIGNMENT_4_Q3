def get_user_data():
    first_name = input("\nWhat is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()
    email = input("What is your email address?: ").strip()
    
    return first_name, last_name, email

def main():
    user_data = get_user_data()
    print(f'User Data: \nFirst name: {user_data[0]}, \nLast name: {user_data[1]}, \nEmail: {user_data[2]}')

if __name__ == '__main__':
    main()