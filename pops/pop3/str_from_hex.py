# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
    hex_codes = [chr(int(i, 16)) for i in hex_codes]
    text = "".join(hex_codes)
    return text


if __name__ == '__main__':
    run(['1f49a', '2728', '1f389', '1f3c6'])


