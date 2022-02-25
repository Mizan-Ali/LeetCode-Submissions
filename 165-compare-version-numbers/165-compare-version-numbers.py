class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1 = version1.split('.')
        num2 = version2.split('.')
        
        if len(num1) < len(num2):
            for _ in range(len(num2)-len(num1)):
                num1.append('0')
        if len(num1) > len(num2):
            for _ in range(len(num1)-len(num2)):
                num2.append('0')
        
        print(num1)
        print(num2)
        
        a = ''
        for i in num1:
            a += str(int(i))
        b = ''
        for i in num2:
            b += str(int(i))
        # print(a)
        # print(b)
        a = a if a != '' else '0'
        b = b if b != '' else '0'
        
       
        a = int(a)
        b = int(b)
        
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0