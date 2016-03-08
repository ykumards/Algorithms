"""
Given a string, print all its permutations.
Runtime is O(n!)
"""

def getPermu(in_string):
    if len(in_string) < 2:
        return in_string

    ch_1 = in_string[0]
    remainder = in_string[1:]
    result_list = []
    permu_list = getPermu(remainder)

    for permu in permu_list:
        for i in xrange(len(remainder)+1):
            s = permu[:i] + ch_1 + permu[i:]
            result_list.append(s)

    return result_list


if __name__ == "__main__":
    in_string = "abcdef"
    
    result = getPermu(in_string)
    print "There are %d permutations" %(len(result))
    choice = str(raw_input("Would you like to see them all?[y/n] ")).lower()
    if choice == 'y':
        print result
