#TODO
"""
    Metodo estático decorador que compruebe si el OS está apagado.
"""

class OS:
    BOOTED_ERROR = "Turn on the OS"
    ROOT = "/"
    NEW_FOLDER = {"files": {}}

    def __init__(self,
        architecture: str = "x64",
        ip: str = "88.90.23.16", 
        kernel: str = "5.15.57.1", 
        booted: bool = False,
        host: str = "localhost",
        distro: str = "xubuntu",
        files: dict = {"/":
        {"etc": {"files": []}, 
        'wololo': {"files": []},
        "bin": {"files": []}, 
        "tmp": {"files": []}, 
        "var": {"files": []}, 
        "home": {"files": [], "user": {"files": []}}},
        "files": []}, 
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
    
    def status(method):
        def wrapper(self, *args, **kwargs):
            if not self.booted:
                return "Device has to be on"
            return method(self, *args, **kwargs)
        return wrapper

    def boot(self) -> str:
        self.booted = not self.booted
        status = "Turning on" if self.booted else "Turning off"
        return status

    @status
    def enable_graph_enviroment(self):
        self.graph = not self.graph

    @status
    def change_name(self, name: str) -> str:
        self.name = name
        return f"Changed succesfully to {self.name}"

    @status
    def change_ip(self, ip):
        self.public_ip = ip
        return f"Your ip address is now {self.public_ip}"

    @status
    def install_packages(self, *packages: str) -> list:
        error_msgs = []
        for package in packages:
            if package not in self.packages:
                self.packages.append(package)
            else:
                error_msg = f"Unable to install {package}, package already installed"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
        return error_msgs

    @status
    def uninstall_packages(self, *packages:str) -> list:
        error_msgs = []
        for package in packages:
            if package in self.packages:
                self.packages.remove(package)
            else:
                error_msg = f"Unable to uninstall {package}, package not found"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
        return error_msgs
    
    @status
    def generate_path(self, path: str) -> tuple:
        folders = path.strip(self.ROOT).split(self.ROOT)
        current_dir = self.files[self.ROOT]
        for folder in folders:
            if folder in current_dir:
                current_dir = current_dir[folder]
            else:
                return f"Folder {folder} does not exist in the file system", False
        return current_dir, True

    @status
    def manage_files(self, operation_type:str, path1:str, file: str, folder: bool=False, path2: str = "/") -> bool:
        match operation_type:
            case "crear":
                if folder:
                    if folder in path1:
                        return False
                    path1[file] = self.NEW_FOLDER
                else:
                    if file in path1["files"]:
                        return False
                    path1["files"].append(file)
            case "eliminar":
                if folder:
                    if file not in path1:
                        return False
                    del path1[file]
                else:
                    if file not in path1["files"]:
                        return False
                    path1["files"].remove(file)
            case "mover":
                if folder:
                    if file not in path1:
                        return False
                    _folder = path1[file]
                    path2[file] = _folder
                    del path1[file]
                else:
                    if file not in path1["files"]:
                        return False
                    archive = path1["files"][path1["files"].index(file)]
                    path2["files"].append(archive)
                    path1["files"].remove(file)
            case _:
                return False
        return True

    @status
    def operate_files(self, operation_type: str, *files: str, folder: bool = False, folder_path: str = "/home/user", new_folder_path: str = "/home") -> list:
        error_msgs = []
        file_type = "folder" if folder else "file"
        match operation_type:
            case "mover":
                path1, status1 = self.generate_path(folder_path)
                path2, status2 = self.generate_path(new_folder_path)
                if status1 and status2:
                    for file in files:
                        error = False
                        if path1 != path2:
                            status = self.manage_files(operation_type, path1, file, folder, path2=path2)
                            error = True if not status else False
                        if error:
                            error_msgs.append(f"Something went wrong with the {file_type} {file}")
            case _:
                path1, status1 = self.generate_path(folder_path)
                if status1:
                    for file in files:
                        status = self.manage_files(operation_type, path1, file, folder)
                        if not status:
                            error_msgs.append(f"Something went wrong with the {file_type} {file}")
        return error_msgs

xubuntu = OS()

print(xubuntu.boot())
print(xubuntu.private_ip)
print(xubuntu.operate_files("crear", "hola_mundo.py", folder_path="/home/user"))
print(xubuntu.files)
print(xubuntu.operate_files("crear", "hola_mundo", folder_path="/etc", folder=True))
print(xubuntu.files)
print(xubuntu.operate_files("mover", "hola_mundo.py", folder_path="/home/user", new_folder_path="/etc"))
print(xubuntu.files)
print(xubuntu.operate_files("mover", "hola_mundo", folder_path="/etc", new_folder_path="/etc", folder=True))
print(xubuntu.files)