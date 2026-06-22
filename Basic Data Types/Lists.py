if __name__ == '__main__':
    n = int(input())

    result_list = []

    for _ in range(n):
        command_args = input().split()
        command = command_args[0]

        if command == 'insert':
            result_list.insert(int(command_args[1]),int(command_args[2]))
            print("insert: ",result_list)
    
        elif command == 'print':
            print(result_list)

        elif command == 'remove':
            result_list.remove(int(command_args[1]))
            print("remove: ",result_list)

        elif command == 'append':
            result_list.append(int(command_args[1]))
            print("append: ",result_list)

        elif command == 'sort':
            result_list.sort()
            print("sort: ",result_list)

        elif command == 'pop':
            result_list.pop()
            print("pop: ",result_list)

        elif command == 'reverse':
            result_list.reverse()
            print("reverse: ",result_list)






