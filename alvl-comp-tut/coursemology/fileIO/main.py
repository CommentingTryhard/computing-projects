def analyze_income_survey(file_name):
    incomelist = []
    mcount = 0
    fcount = 0
    file = open("{}".format(file_name), "r")
    def findline(line):
        line = line.split(",")
        if line[0][:3].isdigit() and line[0][3].isalpha():
            if line[0][3] == "M" or line[0][3] == "F":
                try:
                    income = int(line[1])
                except ValueError:
                    return False
                if income <0:
                    return False
            else:
                return False
        else:
            return False
        return line
    lines = file.read()
    for line in lines.split("\n"):
        line = findline(line)
        if line == False:
            pass
        else:
            incomelist.append(int(line[1]))
            if line[0][-1] == "M":
                mcount+=1
            else:
                fcount+=1
    return [sorted(incomelist)[0], sum(incomelist)/(mcount+fcount), sorted(incomelist, reverse=True)[0], fcount, mcount]

print(analyze_income_survey("income_survey.txt"))