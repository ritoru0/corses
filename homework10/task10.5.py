class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        if len(self) % len(s) != 0:
            return False
        return s * (len(self) // len(s)) == self

    def is_palindrom(self):
        clean_str = self.lower()
        return clean_str == clean_str[::-1]

print(SuperStr("abcabc").is_repeatance("abc"))  
print(SuperStr("abcab").is_repeatance("abc"))    
print(SuperStr("level").is_palindrom())           
print(SuperStr("").is_palindrom())                 
