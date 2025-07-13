#Chad Collard
#Chapter 14 Lab 2
#Computer lesson
#7/13/2025

class Data:
    def __init__(self, cpu_speed, ram_size, drive_size):
        self._cpu_speed = cpu_speed
        self._ram_size = ram_size
        self._drive_size = drive_size

    @property
    def cpu_speed(self):
        return self._cpu_speed

    @cpu_speed.setter
    def cpu_speed(self, value):
        self._cpu_speed = value

    @property
    def ram_size(self):
        return self._ram_size

    @ram_size.setter
    def ram_size(self, value):
        self._ram_size = value

    @property
    def drive_size(self):
        return self._drive_size

    @drive_size.setter
    def drive_size(self, value):
        self._drive_size = value

    def __str__(self):
        return (f"(_Computer__cpu_speed={self.cpu_speed}, "
                f"_Computer__ram_size={self.ram_size}, "
                f"_Computer__drive_size= {self.drive_size})")

computer1 = Data(20, 16, 2000)

print(f"Computer{computer1}")


computer2 = Data(50, 32, 5000)

print(f"Computer{computer2}")

