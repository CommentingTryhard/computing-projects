name, time = input("Please enter your name: "), input("Please enter your time: ")
holder = []
for index, i in enumerate(time):
    holder.append(i)
    if i == ":":
        holder.pop(index)
        holder.append(".")
time = ''.join(holder)

if time[-2:] == "pm":
    time = float(time[:-2])+12
elif time[-2:] == "am":
    time = float(time[:-2])
else:
    time = float(time)
    
dictime = [5, 12, 13, 17, 21]
dict2 = {
    5 : "Good morning",
    12: "Good day",
    13: "Good afternoon",
    17: "Good night"
}
for index, value in enumerate(dictime):
    if (time < dictime[index+1]) and (time > value):
        print("{}, {}!".format(dict2[value],name))
        break
    