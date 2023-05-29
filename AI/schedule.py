def printJobScheduling(arr, t):
    n = len(arr)
    #Sorting jobs in decreasing profit order by bubble sort 
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


    result = [False] * t  #keep track whether space is occupied or not
    job = ['-1'] * t       #used to store job name 
    total_profit = 0

      # Find a free slot for this job 
    for i in range(n):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            #Free slot found    
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                total_profit += arr[i][2]
                break

    print("Job Sequence:", job)
    print("Total Profit:", total_profit)

def main():
    n = int(input("Enter the number of jobs: "))
    arr = []
    print("Enter job details:")
    for i in range(n):
        name = input("Enter job name: ")
        deadline = int(input("Enter job deadline: "))
        profit = int(input("Enter job profit: "))
        arr.append([name, deadline, profit])

    t = int(input("Enter the number of slots: "))
    
    print("Following is the maximum profit sequence of jobs:")
    printJobScheduling(arr, t)

if __name__ == '__main__':
    main()
