import re

num = "24.,24e0,4.4345545345343543,.456464"

er = r"\d*\.\d*|\d*e\d*"

def get_float(num):
    return re.findall(er, num)

#for i in num.split(","):
print(get_float(num))