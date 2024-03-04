from collections import Counter
def makeString(st1,st2):
    a=Counter(st1)
    b=Counter(st2)
    result=a&b
    return result==a

if __name__ == "__main__":

    s1 = 'ABHISHEKsinGH'
    s2 = 'gfhfBHkooIHnfndSHEKsiAnG'
    if (makeString(s1,s2)==True):
        print("possible")
    else:
        print("not possible")