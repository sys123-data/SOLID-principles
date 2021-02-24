from .regex_str_to_int import str_to_int
def gauss_sum(n):
    n = str_to_int(str(n))
    s = 0
    for _ in range(0,n+1): s+=_
    return s