import os

def read_image_bit_string(image_path):
    bit_string = ""
    with open(image_path, 'rb') as image:
        byte = image.read(1)
        while byte:
            byte_value = ord(byte)
            bits = bin(byte_value)[2:].rjust(8, '0')
            bit_string += bits
            byte = image.read(1)
    return bit_string


def save_data(data, path, data_type):
    if data_type == 'image':
        # Chuyển đổi chuỗi bit thành các byte và ghi vào tệp
        byte_array = bytearray(int(data[i:i+8], 2) for i in range(0, len(data), 8))
        with open(path, 'wb') as file:
            file.write(byte_array)  # Lưu dữ liệu dưới dạng nhị phân
    elif data_type == 'dictionary':
        with open(path, 'w') as file:
            for key, value in data.items():
                file.write(f"{key}:{value}\n")  # Lưu từ điển dưới dạng văn bản
    elif data_type == 'text':
        with open(path, 'wb') as file:
            file.write(data.encode())  # Lưu chuỗi văn bản dưới dạng nhị phân
    else:
        raise ValueError("Kiểu dữ liệu không hợp lệ. Các giá trị hỗ trợ: 'image', 'dictionary', 'text'")


# Chuyển đổi văn bản thành chuỗi bit
def text_to_bit_string(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Chuyển đổi chuỗi bit về lại văn bản
def bit_string_to_text(bit_string):
    chars = [chr(int(bit_string[i:i+8], 2)) for i in range(0, len(bit_string), 8)]
    return ''.join(chars)

# Đọc chuỗi bit văn bản từ tệp
def read_text_bit_string(path):
    with open(path, 'rb') as file:
        bit_string = file.read().decode()  # Đọc dưới dạng nhị phân và giải mã thành chuỗi
    return bit_string
