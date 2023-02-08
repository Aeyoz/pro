# ******************
# SUMA CRIPTOGRÁFICA
# ******************
from pathlib import Path


def run(crypto_path: Path) -> float:
    uncryp_table = {"sd":"-", "vo":".", "ax":"0",
                    "gh":"1", "hj":"2", "uv":"3",
                    "ws":"4", "pk":"5", "et":"6",
                    "mc":"7", "rh":"8", "wb":"9"}
    sum_cr = 0
    di = {}
    with open(crypto_path) as f:
        for line in f:
            uncrypt_code = ""
            for i in range(len(line)):
                code = line[i:i + 2]
                if code in uncryp_table:
                    uncrypt_code += uncryp_table[code]
            sum_cr += float(uncrypt_code)
    return sum_cr


if __name__ == '__main__':
    run('data/sum_crypto/data1.crypto')