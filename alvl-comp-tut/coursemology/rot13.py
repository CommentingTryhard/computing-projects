def ROT13(char):
    def checker(chr_rac, chr_org):
        if str(chr(chr_org)) in " 1234567890!@#$%^&*()[]{};':<>,.?/-":
            return chr_org
        else:
            if (chr_rac > 90 and chr_org < 91) or (chr_rac > 122 and chr_org < 121):
                return chr_rac - 26
        return chr_rac
    holder = []
    for i in char:
        appended = ord(i)+13
        holder.append(chr(checker(appended, ord(i))))
    return ''.join(holder)
    
print(ROT13("ALL &&&& CAPITALS"))
        
