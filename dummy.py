
def decimalToBinary(n):  
    return n.replace("0b", "")

def binarycode(s):
    a_byte_array = bytearray(s, "utf8")
    print(a_byte_array)
    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(decimalToBinary(binary_representation))

    #print(byte_list)
    a=""
    for i in byte_list:
        a=a+i
    return a


print(bytearray(3))
binarycode()