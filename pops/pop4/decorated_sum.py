# ****************************
# DECORANDO LA SUMA DE VALORES
# ****************************

def run(values: list) -> dict:
    
    def result_as_status(func):
        def wrapper(*args, **kwargs) -> tuple:
            result = func(*args, **kwargs)
            rstatus = dict(status=result[0], result=result[1])
            return rstatus
        return wrapper

    def _sum(values: list[int|str]) -> dict:
        types = set(type(item) for item in values)
        status = True if len(types) == 1 else False
        output = sum(values) if status else "Not int value found"
        return status, output

    addition = result_as_status(_sum)
    result = addition(values)
    return result
