holder = []

for i in range(3):
    numinput = int(input("Enter number {}:").format(i))
    holder.append(numinput)
if max(holder) < 0:
    ops = "negative"
else:
    ops = "positive"
print("The biggest number is : {}\nThe biggest number is {}".format(max(holder), ops))