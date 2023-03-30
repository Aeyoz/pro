class OS:
    ROOT = "/"
    NEW_FOLDER = {"files": []}
    BOOTED_ERROR = "You may want to turn on the OS\n"
    INVALID_FOLDER = "The path given to the folder is invalid\n"

    def __init__(self,
        architecture: str = "x64",
        ip: str = "88.90.23.16", 
        kernel: str = "5.15.57.1", 
        booted: bool = False,
        host: str = "localhost",
        distro: str = "xubuntu",
        packages: list = ["cmatrix", "apt", "mysql-server", "fillezilla", "vscode"]):

        self.__private_ip = ip
        self.__kernel = kernel
        self.host = host
        self.os_distro = distro
        self.packages = packages
        self.architecture = architecture
        self.public_ip = "192.168.19.5"
        self.booted = booted
        self.graph = True
        self.files = {"/":
        {"etc": {"files": []}, 
        'wololo': {"files": []},
        "bin": {"files": []}, 
        "tmp": {"files": []}, 
        "var": {"files": []}, 
        "home": {"files": [],
        "user": {"files": []}}},
        "files": []} 

    @property
    def kernel(self):
        return self._OS__kernel

    @property
    def private_ip(self):
        return self._OS__private_ip
    
    @staticmethod
    def status(method):
        def wrapper(self, *args, **kwargs):
            if not self.booted:
                return self.BOOTED_ERROR
            return method(self, *args, **kwargs)
        return wrapper
    
    @property
    def package_list(self):
        packages = self.packages
        return ", ".join(packages)

    def boot(self) -> str:
        self.booted = not self.booted
        return "Turning on" if self.booted else "Turning off"

    @status
    def enable_graph_enviroment(self):
        self.graph = not self.graph
        return "Enabling graphical enviroment" if self.booted else "Disabling graphical enviroment"

    @status
    def change_name(self, name: str) -> str:
        self.name = name
        return f"Changed succesfully to {self.name}"

    @status
    def change_ip(self, ip):
        self.public_ip = ip
        return f"Your ip address is now {self.public_ip}"

    @status
    def install_packages(self, *packages: str) -> str:
        error_msgs = []
        for package in packages:
            if package in self.packages:
                error_msg = f"Unable to install {package}, package already installed"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
            self.packages.append(package)
        return "\n".join(error_msgs)

    @status
    def uninstall_packages(self, *packages:str) -> str:
        error_msgs = []
        for package in packages:
            if package not in self.packages:
                error_msg = f"Unable to uninstall {package}, package not found"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
            self.packages.remove(package)
        return "\n".join(error_msgs)
    
    @status
    def generate_path(self, path: str) -> tuple:
        if path == self.ROOT:
            return self.files, True
        if self.ROOT not in path:
            return self.files[path], True
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
                    if file in path1:
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
                    del path1[file]
                    path2[file] = _folder
                else:
                    if file not in path1["files"]:
                        return False
                    archive = path1["files"][path1["files"].index(file)]
                    path1["files"].remove(file)
                    path2["files"].append(archive)
            case _:
                return False
        return True

    @status
    def operate_files(self, operation_type: str, *files: str, folder: bool = False, folder_path: str = "/home/user", new_folder_path: str = "/home") -> list:
        error_msgs = []
        file_type = "folder" if folder else "file"
        path1, status1 = self.generate_path(folder_path)
        if not status1:
            error_msgs.append(self.INVALID_FOLDER)
            return "".join(error_msgs)
        match operation_type:
            case "mover":
                path2, status2 = self.generate_path(new_folder_path)
                if not status2:
                    error_msgs.append(self.INVALID_FOLDER)
                    return "".join(error_msgs)
                for file in files:
                    error = False
                    status = self.manage_files(operation_type, path1, file, folder, path2=path2)
                    if error:
                        error_msgs.append(f"Something went wrong with the {file_type} {file}\n")
            case _:
                for file in files:
                    status = self.manage_files(operation_type, path1, file, folder)
                    if not status:
                        error_msgs.append(f"Something went wrong with the {file_type} {file}\n")
        return "".join(error_msgs)

xubuntu = OS()

xubuntu.boot()
print(xubuntu.private_ip)
print(xubuntu.operate_files("crear", "hola_mundo.py", folder_path="/home/user"))
print(xubuntu.operate_files("crear", "hola_mundo", folder_path="/etc", folder=True))
print(xubuntu.operate_files("mover", "hola_mundo.py", folder_path="/home/user", new_folder_path="/etc"))
print(xubuntu.operate_files("crear", "hola", folder_path="/", folder=True))
print(xubuntu.files)
print(xubuntu.operate_files("crear", "hola", folder_path="/etc"))
print(xubuntu.files)
print(xubuntu.operate_files("crear", "hola.py", folder_path="hola"))
print(xubuntu.files)
xubuntu.operate_files("mover", "hola", folder_path="/", new_folder_path="/etc", folder=True)
print(xubuntu.files)
print(xubuntu.package_list)