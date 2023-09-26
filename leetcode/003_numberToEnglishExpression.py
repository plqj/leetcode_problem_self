# 给定一个整数，打印该整数的英文描述。
#
# 示例 1:
#
# 输入: 123
# 输出: "One Hundred Twenty Three"
# 示例 2:
#
# 输入: 12345
# 输出: "Twelve Thousand Three Hundred Forty Five"
# 示例 3:
#
# 输入: 1234567
# 输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 示例 4:
#
# 输入: 1234567891
# 输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
import sys


# 输入的数要小于12


# 思路：先创建单词词典，对输入数据做逗号划分，然后

class Numebr_Convert(object):
    def __init__(self,number):
        self.number = number
        self.number_str = str(number)
        self.number_lexicon={
            0 : "zero",
            1 : "one",
            2 : "two",
            3 : "three",
            4 : "four",
            5 : "five",
            6 : "six",
            7 : "seven",
            8 : "eight",
            9 : "nine",
            10 : "ten",
            11 : "eleven",
            12 : "twelve",
            13 : "thirteen",
            14 : "fourteen",
            15 : "fifteen",
            16 : "sixteen",
            17 : "seventeen",
            18 : "eighteen",
            19 : "nineteen",
            20 : "twenty",
            30 : "thirty",
            40 : "forty",
            50 : "fifty",
            60 : "sixty",
            70 : "seventy",
            80 : "eighty",
            90 : "ninety",
        }
        self.n=len(self.number_str)
        self.digit = [i for i in self.number_str] # every digit in string compiled as a list
        self.result=[] # a list that stores every word in output

    def add_comma(self):
        """
        :return: three-digit set, use 0 to cover
        """
        l=[]
        while True:
            if len(self.digit)> 12:
                print("error, input digit exceeds")
                sys.exit()
            elif len(self.digit)<12:
                self.digit.insert(0,"0")
            else:
                break
        s=""
        for i in self.digit:
            s+=i
            if len(s)==3:
                l.append(s)
                s=""
        return l

    def fourth(self,input):
        num = int(input)
        if num==0:
            pass

        else:
            if len(str(num))==1:
                self.result.append(f"{self.number_lexicon[num]} billion")
            elif len(str(num))==2:
                if input[1] == "1":
                    self.result.append(f"{self.number_lexicon[num]} billion")
                else:
                    if input[-1] != "0":
                        last=int(input[-1])
                        tem=f"{input[1]}0"
                        intt=int(tem)

                        self.result.append(f"{self.number_lexicon[intt]} {self.number_lexicon[last]} billion")
                    else:
                        self.result.append(f"{self.number_lexicon[int(num)]} billion")
            else: # 3
                hun=int(input[0])
                if input[1] == "0" and input[2]=="0":
                    self.result.append((f"{self.number_lexicon[hun]} hundred billion"))
                elif input[1] == "1":
                    tw=int(f"{input[1]}{input[2]}")
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[tw]} billion")
                elif input[1] == "0" and input[2] != "0":
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[int(input[-1])]} billion")
                elif input[1] != "0" and input[1]!="1" and input[2] == "0":
                    tem=f"{input[1]}0"
                    intt=int(tem)
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[intt]} billion")
                else:
                    last = int(input[-1])
                    tem = f"{input[1]}0"
                    intt = int(tem)
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[intt]} {self.number_lexicon[last]} billion")

    def third(self,input):
        num = int(input)
        if num==0:
            pass

        else:
            if len(str(num))==1:
                self.result.append(f"{self.number_lexicon[num]} million")
            elif len(str(num))==2:
                if input[1] == "1":
                    self.result.append(f"{self.number_lexicon[num]} million")
                else:
                    if input[-1] != "0":
                        last=int(input[-1])
                        tem=f"{input[1]}0"
                        intt=int(tem)

                        self.result.append(f"{self.number_lexicon[intt]} {self.number_lexicon[last]} million")
                    else:
                        self.result.append(f"{self.number_lexicon[int(num)]} million")
            else: # 3
                hun=int(input[0])
                if input[1] == "0" and input[2]=="0":
                    self.result.append((f"{self.number_lexicon[hun]} hundred million"))
                elif input[1] == "1":
                    tw=int(f"{input[1]}{input[2]}")
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[tw]} million")
                elif input[1] == "0" and input[2] != "0":
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[int(input[-1])]} million")
                elif input[1] != "0" and input[1]!="1" and input[2] == "0":
                    tem=f"{input[1]}0"
                    intt=int(tem)
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[intt]} million")
                else:
                    last = int(input[-1])
                    tem = f"{input[1]}0"
                    intt = int(tem)
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[intt]} {self.number_lexicon[last]} million")

    def second(self,input):
        num = int(input)
        if num==0:
            pass

        else:
            if len(str(num))==1:
                self.result.append(f"{self.number_lexicon[num]} thousand")
            elif len(str(num))==2:
                if input[1] == "1":
                    self.result.append(f"{self.number_lexicon[num]} thousand")
                else:
                    if input[-1] != "0":
                        last=int(input[-1])
                        tem=f"{input[1]}0"
                        intt=int(tem)

                        self.result.append(f"{self.number_lexicon[intt]} {self.number_lexicon[last]} thousand")
                    else:
                        self.result.append(f"{self.number_lexicon[int(num)]} thousand")
            else: # 3
                hun=int(input[0])
                if input[1] == "0" and input[2]=="0":
                    self.result.append((f"{self.number_lexicon[hun]} hundred thousand"))
                elif input[1] == "1":
                    tw=int(f"{input[1]}{input[2]}")
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[tw]} thousand")
                elif input[1] == "0" and input[2] != "0":
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[int(input[-1])]} thousand")
                elif input[1] != "0" and input[1]!="1" and input[2] == "0":
                    tem=f"{input[1]}0"
                    intt=int(tem)
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[intt]} thousand")
                else:
                    last = int(input[-1])
                    tem = f"{input[1]}0"
                    intt = int(tem)
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[intt]} {self.number_lexicon[last]} thousand")

    def first(self,input):
        num = int(input)
        if num==0:
            pass

        else:
            if len(str(num))==1:
                self.result.append(f"{self.number_lexicon[num]}")
            elif len(str(num))==2:
                if input[1] == "1":
                    self.result.append(f"{self.number_lexicon[num]}")
                else:
                    if input[-1] != "0":
                        last=int(input[-1])
                        tem=f"{input[1]}0"
                        intt=int(tem)

                        self.result.append(f"{self.number_lexicon[intt]} {self.number_lexicon[last]}")
                    else:
                        self.result.append(f"{self.number_lexicon[int(num)]}")
            else: # 3
                hun=int(input[0])
                if input[1] == "0" and input[2]=="0":
                    self.result.append((f"{self.number_lexicon[hun]} hundred"))
                elif input[1] == "1":
                    tw=int(f"{input[1]}{input[2]}")
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[tw]}")
                elif input[1] == "0" and input[2] != "0":
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[int(input[-1])]}")
                elif input[1] != "0" and input[1]!="1" and input[2] == "0":
                    tem=f"{input[1]}0"
                    intt=int(tem)
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[intt]}")
                else:
                    last = int(input[-1])
                    tem = f"{input[1]}0"
                    intt = int(tem)
                    self.result.append(f"{self.number_lexicon[hun]} hundred and {self.number_lexicon[intt]} {self.number_lexicon[last]}")

    def convert(self):
        l=self.add_comma()
        self.fourth(l[0])
        self.third(l[1])
        self.second(l[2])
        self.first(l[3])
        if self.result == []:
            print("zero")
        else:
            out=" ".join(self.result)
        return out

if __name__ == "__main__":
    test=Numebr_Convert(100001)
    print(test.convert())