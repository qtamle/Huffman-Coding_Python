import heapq
import binary_data_handler
import math

# Node của cây Huffman
class Node:
    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huffman_direction = ''  # Lưu hướng đi 0 hoặc 1 trong cây

    def __lt__(self, nxt):
        return self.frequency < nxt.frequency


# Tạo mã Huffman cho từng ký tự từ cây
def calculate_huffman_codes(node, code='', huffman_codes={}):
    code += node.huffman_direction
    if node.left:
        calculate_huffman_codes(node.left, code, huffman_codes)
    if node.right:
        calculate_huffman_codes(node.right, code, huffman_codes)
    if not node.left and not node.right:  # Nếu là lá
        huffman_codes[node.symbol] = code
    return huffman_codes


# Xây dựng cây Huffman từ tần suất byte
def build_huffman_tree(frequencies):
    heap = [Node(freq, byte) for byte, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        left.huffman_direction = '0'
        right.huffman_direction = '1'
        merged = Node(left.frequency + right.frequency, left.symbol + right.symbol, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]


# Tính tần suất xuất hiện của từng byte trong chuỗi bit
def get_frequencies(bit_string):
    frequency = {}
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i + 8]
        frequency[byte] = frequency.get(byte, 0) + 1
    return frequency


# Hàm nén dữ liệu
def compress_data(bit_string, output_file):
    frequencies = get_frequencies(bit_string)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = calculate_huffman_codes(huffman_tree)
    
    # Lưu mã Huffman ra file
    binary_data_handler.save_data(huffman_codes, output_file, 'dictionary')
    
    # Tạo chuỗi nén
    compressed_bit_string = ''.join(huffman_codes[bit_string[i:i+8]] for i in range(0, len(bit_string), 8))

    return compressed_bit_string


# Giải nén dữ liệu từ chuỗi nén
def decompress_data(compressed_bit_string, huffman_codes):
    decompressed_bit_string = ""
    current_code = ""
    code_to_byte = {code: byte for byte, code in huffman_codes.items()}

    for bit in compressed_bit_string:
        current_code += bit
        if current_code in code_to_byte:
            decompressed_bit_string += code_to_byte[current_code]
            current_code = ""

    return decompressed_bit_string
