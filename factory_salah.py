# KELOMPOK C - Factory Pattern
# Irfan Maulana Manaf 
# Melisa Novpriyanti
# Danang Wahyu
# Imam Baihaqqi
# Rizky Dhafin
# Raditya Wisnu C N
# Femas Arianda R


'''
MASALAH :
1. Kode klien harus mengetahui kelas-kelas spesifik yang ingin diinstansiasi.
2. Jika ada jenis shape baru (misalnya Rectangle), kita harus memodifikasi kode klien.

'''

# Produk spesifik
class Circle:
    def draw(self):
        print("Drawing a Circle")

class Square:
    def draw(self):
        print("Drawing a Square")

# Kode Klien
if __name__ == "__main__":
    shape_type = "Circle"
    
    if shape_type == "Circle":
        shape = Circle()
    elif shape_type == "Square":
        shape = Square()
    
    shape.draw()
