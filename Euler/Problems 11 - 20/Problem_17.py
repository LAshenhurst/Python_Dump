units = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
teens = {11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
tens = {10:'ten', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
others = ['and', 'hundred']

def Problem_17():
    count = sum(len(units[x]) for x in range(1, 10)) + len(tens[10]) + sum(len(teens[x]) for x in range(11, 20)) + len(tens[20])
    for i in range(1, 1001):

        if i <