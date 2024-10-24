import tkinter as tk
from tkinter import filedialog, messagebox
import binary_data_handler
import huffman_coding
from tkinter import ttk

def update_ui(selection):
    if selection == "Ảnh":
        image_path_label.pack(pady=10)
        image_path_entry.pack(pady=5, fill=tk.X)
        browse_button.pack(pady=5)
        compress_button.pack(pady=5)
        decompress_button.pack(pady=5)
        compression_ratio_label.pack(pady=5)
        
        text_label.pack_forget()
        text_entry.pack_forget()
        compress_text_button.pack_forget()
        decompress_text_button.pack_forget()
        text_compression_ratio_label.pack_forget()
        decompressed_text_label.pack_forget()
    elif selection == "Chữ":
        text_label.pack(pady=10)
        text_entry.pack(pady=5, fill=tk.X)
        compress_text_button.pack(pady=5)
        decompress_text_button.pack(pady=5)
        text_compression_ratio_label.pack(pady=5)
        decompressed_text_label.pack(pady=10)
        compression_ratio_label.pack_forget()
        
        image_path_label.pack_forget()
        image_path_entry.pack_forget()
        browse_button.pack_forget()
        compress_button.pack_forget()
        decompress_button.pack_forget()

def compress_image():
    image_path = image_path_entry.get()
    if not image_path:
        messagebox.showerror("Lỗi", "Vui lòng chọn tệp hình ảnh.")
        return

    image_bit_string = binary_data_handler.read_image_bit_string(image_path)
    compressed_image_bit_string = huffman_coding.compress_data(image_bit_string, './IO/Outputs/huffman_codes_Image.txt')

    if compressed_image_bit_string:
        compressed_path = "IO/Outputs/compressed_image.bin"
        binary_data_handler.save_data(compressed_image_bit_string, compressed_path, 'image')
        compression_ratio = len(image_bit_string) / len(compressed_image_bit_string)
        compression_ratio_label.config(text=f"Tỷ lệ nén (CR): {compression_ratio:.2f}")
    else:
        messagebox.showerror("Lỗi", "Nén hình ảnh không thành công.")

def decompress_image():
    compressed_path = "IO/Outputs/compressed_image.bin"
    compressed_image_bit_string = binary_data_handler.read_image_bit_string(compressed_path)

    if compressed_image_bit_string:
        huffman_codes_path = './IO/Outputs/huffman_codes_Image.txt'
        huffman_codes = {}
        with open(huffman_codes_path, 'r') as file:
            for line in file:
                key, value = line.strip().split(':')
                huffman_codes[key] = value

        decompressed_image_bit_string = huffman_coding.decompress_data(compressed_image_bit_string, huffman_codes)
        decompressed_path = "IO/Outputs/decompressed_image.jpg"
        binary_data_handler.save_data(decompressed_image_bit_string, decompressed_path, 'image')
        decompression_complete_label.config(text="Giải nén hoàn tất!")
    else:
        messagebox.showerror("Lỗi", "Giải nén không thành công. Không tìm thấy hình ảnh đã nén.")

def browse_image_path():
    image_path = filedialog.askopenfilename(filetypes=[("Tệp hình ảnh", "*.jpg *.jpeg *.png *.bin")])
    image_path_entry.delete(0, tk.END)
    image_path_entry.insert(0, image_path)
    
def compress_text():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số văn bản.")
        return
    
    text_bit_string = binary_data_handler.text_to_bit_string(text)
    compressed_text_bit_string = huffman_coding.compress_data(text_bit_string, './IO/Outputs/huffman_codes_Text.txt')

    if compressed_text_bit_string:
        compressed_path = "IO/Outputs/compressed_text.bin"
        binary_data_handler.save_data(compressed_text_bit_string, compressed_path, 'text')
        compression_ratio = len(text_bit_string) / len(compressed_text_bit_string) if len(compressed_text_bit_string) > 0 else 0
        text_compression_ratio_label.config(text=f"Tỷ lệ nén chữ (CR): {compression_ratio:.2f}")
    else:
        messagebox.showerror("Lỗi", "Nén chữ không thành công.")

def decompress_text():
    compressed_path = "IO/Outputs/compressed_text.bin"
    compressed_text_bit_string = binary_data_handler.read_text_bit_string(compressed_path)
    
    if compressed_text_bit_string:
        huffman_codes_path = './IO/Outputs/huffman_codes_Text.txt'
        huffman_codes = {}
        with open(huffman_codes_path, 'r') as file:
            for line in file:
                key, value = line.strip().split(':')
                huffman_codes[key] = value
        decompressed_text_bit_string = huffman_coding.decompress_data(compressed_text_bit_string, huffman_codes)
        decompressed_text = binary_data_handler.bit_string_to_text(decompressed_text_bit_string)

        decompressed_text_label.config(text=f"Văn bản giải nén: {decompressed_text}")
        decompressed_text_path = "IO/Outputs/decompress_text.txt"
        with open(decompressed_text_path, 'w') as file:
            file.write(decompressed_text)

        messagebox.showinfo("Thành công", f"Văn bản giải nén đã được lưu tại: {decompressed_text_path}")
    else:
        messagebox.showerror("Lỗi", "Giải nén không thành công. Không tìm thấy văn bản đã nén.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Mã hóa Huffman Nhóm 4")

# Tạo và thiết lập kiểu tùy chỉnh
style = ttk.Style()
style.theme_use("clam")  # Thay đổi thành 'clam' để có giao diện hiện đại hơn
root.configure(bg="#e0f7fa")  # Thiết lập màu nền

# Thiết lập kích thước cửa sổ (chiều rộng x chiều cao)
root.geometry("600x600")  # Tăng chiều cao cửa sổ để cải thiện bố cục

# Thêm một tiêu đề lớn
title_label = ttk.Label(root, text="Nhóm 4", font=("Arial", 24), background="#4dd0e1", foreground="white", padding=(10, 5))
title_label.pack(pady=10)

# Tạo và đặt một combobox cho lựa chọn
selection_label = ttk.Label(root, text="Chọn kiểu nén", background="#e0f7fa", font=("Arial", 14))
selection_label.pack(pady=10)

compression_type = ttk.Combobox(root, values=["Chữ", "Ảnh"], state="readonly", font=("Arial", 12))
compression_type.pack(pady=5)
compression_type.bind("<<ComboboxSelected>>", lambda e: update_ui(compression_type.get()))

# Thêm các widget cho nén văn bản
text_label = ttk.Label(root, text="Nhập văn bản:", background="#e0f7fa", font=("Arial", 12))
text_entry = tk.Text(root, height=10, font=("Arial", 12))
compress_text_button = ttk.Button(root, text="Nén chữ", command=compress_text, style='Accent.TButton')
decompress_text_button = ttk.Button(root, text="Giải nén chữ", command=decompress_text, style='Accent.TButton')
text_compression_ratio_label = ttk.Label(root, text="Tỷ lệ nén (CR):", background="#e0f7fa", font=("Arial", 12))
decompressed_text_label = ttk.Label(root, text="", background="#e0f7fa", font=("Arial", 12))

# Tạo và đặt các widget cho nén hình ảnh
image_path_label = ttk.Label(root, text="Đường dẫn hình ảnh:", background="#e0f7fa", font=("Arial", 12))
image_path_entry = ttk.Entry(root, font=("Arial", 12))
browse_button = ttk.Button(root, text="Tìm ảnh", command=browse_image_path, style='Accent.TButton')
compress_button = ttk.Button(root, text="Nén ảnh", command=compress_image, style='Accent.TButton')
decompress_button = ttk.Button(root, text="Giải nén", command=decompress_image, style='Accent.TButton')
compression_ratio_label = ttk.Label(root, text="Tỷ lệ nén (CR):", background="#e0f7fa", font=("Arial", 12))
decompression_complete_label = ttk.Label(root, text="", background="#e0f7fa", font=("Arial", 12))

# Cấu hình kiểu cho nút
style.configure('Accent.TButton', background="#64b5f6", foreground="white", font=("Arial", 12), borderwidth=1)
style.map('Accent.TButton', background=[('active', '#42a5f5')])

# Bắt đầu vòng lặp chính
root.mainloop()
