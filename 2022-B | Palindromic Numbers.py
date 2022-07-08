# Google Kick Start
# 2022: Round B
# Palindromic Numbers

def palindromic(number):
    for x in range(len(number)//2 + 1): # Up to halfway
        if number[x] != number[-(x+1)]: # equates first and last, working inwards
            return False # NOT palindromic
    return True # palindromic

end = 100 # Test Set A: 1000; B: 10^10

for dividend in range(1, end + 1):

    pdCount = 0 # Number of palindromic factors

    for divisor in range(1, int(dividend ** 0.5) + 1): # incremented up to sqrt(dividend)
        if dividend % divisor == 0: # if factor
            for each in {divisor, dividend // divisor}: # for divisor and quotient (SET handles perfect sqrt)
                if palindromic(str(each)): # if palindromic
                    pdCount += 1

    print(f'Case #{dividend}: {pdCount}')