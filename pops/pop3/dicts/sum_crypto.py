# ******************
# SUMA CRIPTOGRÁFICA
# ******************
from pathlib import Path


def run(crypto_path: Path) -> float:
    uncrypt_table = {"sd":"-", "vo":".", "ax":"0",
                    "gh":"1", "hj":"2", "uv":"3",
                    "ws":"4", "pk":"5", "et":"6",
                    "mc":"7", "rh":"8", "wb":"9"}
    sum_cr = 0
    with open(crypto_path) as f:
        for line in f:
            uncrypt_code = []
            for i in range(len(line)):
                code = line[i:i + 2]
                if code in uncrypt_table:
                    uncrypt_code.append(uncrypt_table[code])
            sum_cr += float("".join(uncrypt_code))
    return sum_cr


if __name__ == '__main__':
    run('data/sum_crypto/data1.crypto')