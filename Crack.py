class Crack:
    def __init__(self):
        self.crack()


    def PassWord(self):
        Password = input("비밀번호를 입력하세요(8글자, 특수문자안됨):")
        return str(Password)


    def crack(self):
        crack=[]
        for i in range(0, 123):
            crack.append(chr(i))
        Password = Crack.PassWord(self)
        found_pw=[]

        for i in range(0, 8):
            for j in range(0, len(crack)):
                if (Password[i] == crack[j]):
                    found_pw.append(crack[j])
        print(str(found_pw))


if __name__ == '__main__':
    user = Crack()



