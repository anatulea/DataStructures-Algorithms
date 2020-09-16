
import time
myList = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(100000)]

def findNemo(aList):
    t0 = time.time()
    for i in aList:
        if (i == 'nemo'):
            print('found nemo!')
    t1 = time.time()
    print(f'Time taken = {t1-t0}')
findNemo(myList) #O(n) ---> liniar time
findNemo(everyone)
findNemo(large)

def funchallenge(input):
    temp = 10 #O(1)
    temp = temp +50 #O(1)
    for i in range(len(input)): #O(n)
        var = True #n*O(1)
        a += 1 #n*O(1)
    return a #O(1)

funchallenge(myList)
funchallenge(everyone)
funchallenge(large)

#Total running time of the funchallenge function =
#O(1 + 1 + n + n*1 + n*1 + n*1 + 1) = O(3n +3) = O(3(n+1))
#Any constant in the Big-O representation can be replaced by 1, as it doesn't really matter what constant it is.
#Therefore, O(3(n+1)) becomes O(n+1)
#Similarly, any constant number added or subtracted to n or multiplied or divided by n can also be safely written as just n
#This is because the constant that operates upon n, doesn't depend on n, i.e., the input size
#Therefore, the funchallenge function can be said to be of O(n) or Linear Time Complexity.
