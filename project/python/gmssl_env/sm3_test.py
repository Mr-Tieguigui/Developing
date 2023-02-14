from gmssl import sm3, func


def test(strs):
# strs = "20210201173824975258"
    str_b = bytes(strs, encoding='utf-8')
    result = sm3.sm3_hash(func.bytes_to_list(str_b))
    print("加密后：", result) 

if __name__ == '__main__':
    print("sm3 begin")
    strs = input("strs:\n")
    test(strs)
    input('Press Enter to exit…')
    