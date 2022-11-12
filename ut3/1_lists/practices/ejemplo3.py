date = "12/31/20"
date = date.split("/")
fixed_date = "-".join([date[1],date[0],"20" + date[2]])
print(fixed_date)