class OS:
    BOOTED_ERROR = "Turn on the OS"

    def __init__(self, host: str,
        architecture: str,
        ip: str, 
        kernel: str, 
        booted: bool,
        file_operations: dict = {"crear":"mkdir", "eliminar":"rm", "mover":"mv"}, 
        distro: str = "Linux",
        files: dict = {"etc": [], "bin": []}, 
        packages: list = ["cmatrix"]):

        self.host = host
        self.os_distro = distro
        self.packages = packages
        self.architecture = architecture
        self.__private_ip = ip
        self.public_ip = "192.168.19.5"
        self.kernel = kernel
        self.booted = booted
        self.graph = True
        self.file_operations = file_operations
        self.files = files

    def boot(self):
        self.booted = not self.booted

    def enable_graph_enviroment(self):
        if not self.booted:
            return self.BOOTED_ERROR
        self.graph = not self.graph

    def change_name(self, name):
        if not self.booted:
            return self.BOOTED_ERROR
        self.name = name

    def change_ip(self, ip):
        if not self.booted:
            return self.BOOTED_ERROR
        self.public_ip = ip

    def install_packages(self, *packages):
        if not self.booted:
            return self.BOOTED_ERROR
        for package in packages:
            if package not in self.packages:
                self.packages.append(package)

    def uninstall_packages(self, *packages):
        if not self.booted:
            return self.BOOTED_ERROR
        for package in packages:
            if package in self.packages:
                self.packages.remove(package)

    def operate_files(self, operation_type, first_location:str, second_location, file:str):
        match operation_type:
            case 'crear':
                self.files[first_location].append(file)
            case 'mover':
                pass
            case 'eliminar':
                self.files[first_location].append(file)
            case _:
                return False

    @property
    def prueba(self):
        return self

windows = OS(host="ayoze", architecture="x64", ip="80.90.61.13", kernel="15.25.2.5", booted=True)

print(windows.prueba)