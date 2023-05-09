class StringUtility:
    
    def __init__(self, string):
        self.string = string
        
    def __str__(self):
        return self.string
    
    def vowels(self):
        count = 0
        vowels = "aeiouAEIOU"
        for i in self.string:
            for char in vowels:
                    if i == char:
                        count += 1
        if count < 5:
            return str(count)
        else:
            return "many"
                
    def bothEnds(self):
        if len(self.string) < 2:
            return ""
        else:
            return self.string[0:2] + self.string[-2:]
        
    def fixStart(self):
        if len(self.string) >= 1:
            first = self.string[0]
            return first + self.string[1:].replace(first, "*")
        else:
            return ""
    
    def asciiSum(self):
        sum = 0
        for i in self.string:
            sum += ord(i)
        return sum
    
    def cipher(self):
        in_str = self.string
        output_str = ""
        str_len = len(in_str)
        
        for char in in_str:
            if not char.isalpha():
                output_str += char
                continue  
            
            is_upper = char.isupper()
            char = char.lower()
            
            s = (ord(char) - 97 + str_len) % 26 + 97
            s_char = chr(s)
            
            if is_upper:
                s_char = s_char.upper()
            output_str += s_char
        return output_str