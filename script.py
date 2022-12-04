class Solution:
    def romanToInt(self, s: str) -> int:
        ones= 0
        fives= 0
        tens= 0
        fifties= 0
        hundreds= 0
        five_hundreds= 0
        thousands= 0
        i= 0
        while i != len(s):
            if s[i] == 'I':
                if i+1 < len(s):
                    if s[i+1] == 'V':
                        ones+= 4
                        i+= 2
                    elif s[i+1] == 'X':
                        ones+= 9
                        i+= 2
                    else:
                        ones+= 1
                        i+= 1
                else:
                    ones+= 1
                    i+= 1
            elif s[i] == 'V':
                fives+= 1
                i+= 1
            elif s[i] == 'X':
                if i+1 < len(s):
                    if s[i+1] == 'L':
                        tens+= 4
                        i+= 2
                    elif s[i+1] == 'C':
                        tens+= 9
                        i+= 2
                    else:
                        tens+= 1
                        i+= 1
                else:
                    tens+= 1
                    i+= 1
            elif s[i] == 'L':
                fifties+= 1
                i+= 1
            elif s[i] == 'C':
                if i+1 < len(s):
                    if s[i+1] == 'D':
                        hundreds+= 4
                        i+= 2
                    elif s[i+1] == 'M':
                        hundreds+= 9
                        i+= 2
                    else:
                        hundreds+= 1
                        i+= 1
                else:
                    hundreds+= 1
                    i+= 1
            elif s[i] == 'D':
                five_hundreds+= 1
                i+= 1
            elif s[i] == 'M':
                thousands+= 1
                i+= 1
        fives*= 5
        tens*= 10
        fifties*= 50
        hundreds*= 100
        five_hundreds*= 500
        thousands*= 1000
        final_sum= int(
            ones+
            fives+
            tens+
            fifties+
            hundreds+
            five_hundreds+
            thousands
        )
        return final_sum
        
