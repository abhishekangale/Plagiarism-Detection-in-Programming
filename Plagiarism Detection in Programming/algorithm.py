from TimeComplexityAnalyzer import browsefunc
class wagner_fischer:
    
    def __init__(self,string_1,string_2):
        self.code1 = string_1    
        self.code2 = string_2
    
    @property
    def inf(self):
        return len(self.code1) + len(self.code2)

    def complete_tabulation(self):
        length_1 = len(self.code1)
        length_2 = len(self.code2)
        if(length_1 > length_2):
            length_2,length_1 = length_1,length_2
            self.code2,self.code1 = self.code1,self.code2
        self.table = [[self.inf for x in range(length_1 + 1)] for y in range(length_2 + 1)]
        for i in range(length_1 + 1):
            self.table[0][i] = i
        for i in range(length_2 + 1):
            self.table[i][0] = i
        for i in range(length_2):
            for j in range(length_1):
                self.table[i + 1][j + 1] = min(self.table[i + 1][j] + 1,self.table[i][j + 1] + 1)
                if(self.code1[j] == self.code2[i]):
                    self.table[i + 1][j + 1] = self.table[i][j]
        self.table[0][len(self.code1)] = self.table[length_2][length_1]

    def get_restricted_table(self,x,y,current_x,allowed_length):
        if (abs(x - y) > allowed_length):
            return self.inf
        else:
            return self.table[x + 1 - current_x][y]

    def restricted_tabulation(self,thresh):
        length_1 = len(self.code1)
        length_2 = len(self.code2)
        if(length_1 > length_2):
            length_2,length_1 = length_1,length_2
            self.code2,self.code1 = self.code1,self.code2
        cmp_length = (int)(length_2*thresh)
        self.table = [[self.inf for x in range(length_1 + 1)] for y in range(2)]
        if(cmp_length > length_1):
            self.table[0][length_1] = (length_2)
            return   
        for i in range(cmp_length):
            self.table[0][i] = i
        for i in range(length_2):
            x = i + 1
            y = max(1,i + 1 - cmp_length)
            self.table[1][0] = x
            while(abs(x - y) <= cmp_length):
                if(y <= length_1):
                    self.table[1][y] = min(self.get_restricted_table(x - 1,y,x,cmp_length) + 1,self.get_restricted_table(x,y - 1,x,cmp_length) + 1)
                    if(self.code1[y - 1] == self.code2[x - 1]):
                        self.table[1][y] = self.table[0][y - 1]
                else:
                    break
                y += 1
            self.table[0] = self.table[1]
            self.table[1] = [self.inf for x in range(length_1 + 1)]
        if(self.table[0][length_1] > cmp_length):
            self.table[0][length_1] = (length_2)
    
    def table_display(self):
        length_1 = len(self.code1)
        length_2 = len(self.code2)
        for i in range(length_2):
            for j in range(length_1):
                print(self.table[i][j],end = ' ')
            print(end = '\n')
    
    def score_generator(self):
        score = 1.0 - (self.table[0][len(self.code1)]/len(self.code2))
        t1 = browsefunc(self.code1)
        t2 = browsefunc(self.code2)
        if score > 0.75:
            if t1 == t2:
                score = score * 0.75 + 0.25

        score *= 100.0
        return score 