def add_three_copies(my_list, data):
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    msg = input('\nEnter a message to copy: ')
    my_list = []
    print(f'\nBefore List: {my_list}\n')
    add_three_copies(my_list, msg)
    print(f'After List: {my_list}')

if __name__ == '__main__':
    main()