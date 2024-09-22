# KELOMPOK C - Factory Pattern
# Irfan Maulana Manaf 
# Melisa Novpriyanti
# Danang Wahyu
# Imam Baihaqqi
# Rizky Dhafin
# Raditya Wisnu C N
# Femas Arianda R

'''
SETELAH PERBAIKAN :
1. Loose Coupling   : Kode klien tidak lagi perlu mengetahui detail kelas konkret, hanya perlu berinteraksi dengan ShapeFactory.
2. Skalabilitas     : Jika ingin menambahkan bentuk baru, hanya perlu menambahkan kelas produk baru dan memperbarui ShapeFactory, tanpa mengubah kode klien.
3. Fleksibilitas    : Mudah untuk memperluas tipe shape yang didukung tanpa memodifikasi kode klien secara langsung.
4. Jika klien meminta bentuk yang tidak dikenal, seperti "Pentagon", factory akan mengembalikan None dan mencetak pesan kesalahan yang sesuai ditampilkan.

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

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

# Factory untuk membuat objek
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        elif shape_type == "Triangle":
            return Triangle()
        else:
            return None

'''
kode klien dibawah adalah bagian yang meminta objek dari factory untuk digunakan dalam aplikasi, 
tanpa harus mengetahui detail implementasi dari objek yang dibuat.

'''

if __name__ == "__main__":
    # Daftar shape yang diinginkan oleh klien
    shape_types = ["Circle", "Square", "Triangle", "Pentagon"]

    for shape_type in shape_types:
        shape = ShapeFactory.get_shape(shape_type)
        if shape:
            shape.draw()
        else:
            print(f"Shape '{shape_type}' is not recognized.")
