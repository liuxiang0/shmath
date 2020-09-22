from math import remainder, floor

myList=[[-3,-5],[-3,5],[3,-5],[3,5], [-3,-4],[-3,4],[3,-4],[3,4], [-3,-2],[-3,2],[3,-2],[3,2], [-4,-3],[-4,3],[4,-3],[4,3], [-7,-4],[-7,4],[7,-4],[7,4], [-7,-3],[-7,3],[7,-3],[7,3]]


if __name__ == "__main__":
    print("|a \t|b \t|求商 floor(a/b)|求余 remainder(a,b)|取模 a%b|")
    print("|--- \t|--- \t|--- \t|--- \t|--- \t|")
    for grp in myList:
        a, b = grp
        print("|{a}\t|{b}\t|{f}\t|{r}\t|{m}\t|".format(a=a,b=b,f=floor(a/b),r=round(remainder(a,b)),m=a%b))
