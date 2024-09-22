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

class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

# Factory untuk membuat objek
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        else:
            return None

'''
kode klien dibawah adalah bagian yang meminta objek dari factory untuk digunakan dalam aplikasi, 
tanpa harus mengetahui detail implementasi dari objek yang dibuat.

'''
if __name__ == "__main__":
    shape_type = "Circle"
    
    shape = ShapeFactory.get_shape(shape_type)
    if shape:
        shape.draw()
    else:
        print("Invalid shape type")
