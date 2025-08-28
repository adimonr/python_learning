import array

def revadder(self,array1,array2): 
        op1=int("".join(map(str,array1)))
        op2=int("".join(map(str,array2)))
        rev1=int(str(op1)[::-1])
        rev2=int(str(op2)[::-1])
        real=rev1+rev2
        real2 = array.array('i', map(int, str(real)))
        return list(real2)

print(revadder(1,[2,3,4,5],[7,8,9]))