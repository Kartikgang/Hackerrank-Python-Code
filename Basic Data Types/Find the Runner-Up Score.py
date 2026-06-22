if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()))

    x = arr[0]
    y = arr[1]

    for i in range(n):
        if(arr[i] > x):
            y = x
            x = arr[i]
        elif(arr[i] < x and arr[i] >= y and x != y):
            y = arr[i]
        elif(x == y and arr[i]<x):
            y = arr[i]

    print(y)