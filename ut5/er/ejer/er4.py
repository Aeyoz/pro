import re

num = "elpay_ov2@@gmail.com elpayov2@@gmail.com elpayov2@gmail.com elpayov2@gmail. elpayoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaav2@gmail.com" 


er = r"\b[a-z0-9]+@[a-z0-9]+\.\w+\b"

def get_float(num):
    return re.findall(er, num)


print(get_float(num))