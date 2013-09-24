def findLongestPalindrome(string):
    # local variables
    strLen = len(string)
    # result, initialized to be a string of length 1
    curMax = 1
    palindromeStart = 0
    palindromeEnd = 1
    # container to hold dynamic programming
    data = [[0] * strLen for x in range(strLen)]
    # init starting values: every string with length has the longest palindrome of length 1
    for x in range(strLen):
        data[x][x] = 1
    # iterate from 2 to length of string
    # flp(str): if start and end equal and flp(str.sub(start + 1, end - 1)) != 0, flp(str) = flp(sub) + 2
    for curLen in range(1, strLen):
        for startIdx in range(strLen):
            end = startIdx + curLen
            # boundary checking
            if end >= strLen:
                break
            head = string[startIdx]
            tail = string[end]
            val = 0
            subVal = data[startIdx + 1][end - 1]
            if head == tail:
                if curLen == 1:
                    val = 2
                elif subVal != 0:
                    val = subVal + 2
            data[startIdx][end] = val
            # checking whether it is the optimal solution
            if curMax < val:
                curMax = val
                palindromeStart = startIdx
                palindromeEnd = end + 1
    return string[palindromeStart:palindromeEnd]