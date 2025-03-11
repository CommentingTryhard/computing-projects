def caesar_cipher(text, shift):
    def count(org_argv, org):
        if (org_argv<97 and org>96) or (org_argv<65 and org>64):
            return org_argv+26
        elif (org_argv>122 and org<122) or (org_argv>90 and org<91):
            return org_argv-26
        else:
            return org_argv
    # write code here
    holder = []
    for i in text:
        holder.append(i)
    for index, i in enumerate(holder):
        print(index)
        if i in "1234567890,./;':?><()*&^%$#@!{}[]_-=+ ":
            pass
        else:
            if shift<0:
                replacement = chr(count(ord(i)-abs(shift), ord(i)))
            else:
                replacement = chr(count(ord(i)+abs(shift), ord(i)))
            print(replacement)
            holder.pop(index)
            holder.insert(index, replacement)
        print(holder)
    return "".join(holder)
    #return the encrypted text
