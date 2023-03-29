#TODO
"""
    Metodo estático decorador que compruebe si el OS está apagado.
"""

class OS:
    BOOTED_ERROR = "Turn on the OS"

    def __init__(self,
        architecture: str = "x64",
        ip: str = "88.90.23.16", 
        kernel: str = "5.15.57.1", 
        booted: bool = True,
        host: str = "localhost",
        distro: str = "xubuntu",
        files: dict = {"/etc": [], "/bin": [], "/tmp": {}, "/var":[]}, 
        packages: list = ["cmatrix"]):

        self.__private_ip = ip
        self.__kernel = kernel
        self.host = host
        self.os_distro = distro
        self.packages = packages
        self.architecture = architecture
        self.public_ip = "192.168.19.5"
        self.booted = booted
        self.graph = True
        self.files = files

    @property
    def kernel(self):
        return self._OS__kernel

    @property
    def private_ip(self):
        return self._OS__private_ip

    def boot(self):
        self.booted = not self.booted
        status = "Turning on" if self.booted else "Turning off"
        return status

    def enable_graph_enviroment(self):
        if not self.booted:
            return self.BOOTED_ERROR
        self.graph = not self.graph

    def change_name(self, name):
        if not self.booted:
            return self.BOOTED_ERROR
        old_name = self.name
        self.name = name
        return f"Changed succesfully from {old_name} to {self.name}"

    def change_ip(self, ip):
        if not self.booted:
            return self.BOOTED_ERROR
        self.public_ip = ip
        return f"Your ip address is now {self.public_ip}"

    def install_packages(self, *packages):
        error_msgs = []
        if not self.booted:
            return self.BOOTED_ERROR
        for package in packages:
            if package not in self.packages:
                self.packages.append(package)
            else:
                error_msg = f"Unable to install {package}, package already installed"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
        return error_msgs

    def uninstall_packages(self, *packages):
        error_msgs = []
        if not self.booted:
            return self.BOOTED_ERROR
        for package in packages:
            if package in self.packages:
                self.packages.remove(package)
            else:
                error_msg = f"Unable to uninstall {package}, package not found"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
        return error_msgs
    
    def operate_files(self, operation_type: str, *files:str, folder:str = "/etc", new_folder:str = "/etc"):
        if not self.booted:
            return self.BOOTED_ERROR
        error_msgs = []
        match operation_type:
            case 'crear':
                for file in files:
                    if file not in self.files:
                        self.files[folder].append(file)
                    else:
                        error_msgs.append(f"File {file} already exists\n")
                return error_msgs
            case 'mover':
                for file in files:
                    if file in self.files[folder]:
                        archive = self.files[folder][self.files[folder].index(file)]
                        self.files[new_folder].append(archive)
                        self.files[folder].remove(archive)
                    else:
                        error_msgs.append(f"File {file} not found\n")
                return error_msgs
            case 'eliminar':
                for file in files:
                    if file in self.files[folder]:
                        self.files[folder].remove(file)
                    else:
                        error_msgs.append(f"File {file} not found\n")
                return error_msgs
            case _:
                return False
files = {'/':{"etc":{},"bin":{pepe{lola}},"tmp":{},"var":{}}}
relative_path = []
path = "/bin/bash"
matraca = files[bin]
matraca = matraca[pepe]
matraca = matraca[lola]
for dir in path.strip('/').split('/'):
    files[] += {}
    relative_path.append(dir)

bin pepe lola karla lopez dionisio

{"/":{}}

xubuntu = OS()

print(xubuntu.operate_files("crear", "hola_mundo.py", folder="/etc"))
print(xubuntu.files)
print(xubuntu.operate_files("mover", "hola_mundo.py", folder="/etc", new_folder="/bin"))
print(xubuntu.files)
print(xubuntu.operate_files("eliminar", "hola_mundo.py", folder="/etc"))
print(xubuntu.operate_files("eliminar", "hola_mundo.py", folder="/bin"))
print(xubuntu.files)
print(xubuntu.private_ip)