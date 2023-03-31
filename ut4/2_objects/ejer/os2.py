#TODO
"""
- Añadir docstrings a los ultimos 3 metodos
- Cambiar el nombre de los ultimos 3 metodos
- Refactorizar lo que se pueda
"""

class OS:
    ROOT = "/"
    NEW_FOLDER = {"files": []}
    BOOTED_ERROR = "You may want to turn on the OS\n"
    INVALID_USER = "The username provided does not exists\n"
    USER_EXISTANCE = "The username provided already exists\n"
    INVALID_FOLDER = "The path given to the folder is invalid\n"

    def __init__(self,
        distro: str,
        architecture: str,
        ip: str, # Privada 
        kernel: str = "5.15.57.1", 
        host: str = "localhost",
        booted: bool = False,
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
        self.users = {"root" : {"passwd": "matraca", "access": "all"}, 
        "ayoze": {"passwd": "carcassone", "access": "restricted"}, 
        "nuhazet": {"passwd": "wololo", "access": "restricted"},
        "user": {"passwd": "user", "access": "restricted"}}
        self.user = "" #No hay usuario que haya iniciado sesión al iniciar el SO
        self.files = {"/":
        {"root": {"files": []},
        "etc": {"files": []}, 
        "wololo": {"files": []},
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
    def logged_in(method):
        """
        Comprueba el usuario ha iniciado sesión
        """
        def wrapper(self, *args, **kwargs):
            if not self.user in self.users:
                return "You are not logged in"
            return method(self, *args, **kwargs)
        return wrapper
    
    @staticmethod
    def status(method):
        """
        Comprueba si la máquina está encendida
        """
        def wrapper(self, *args, **kwargs):
            if not self.booted:
                return self.BOOTED_ERROR
            return method(self, *args, **kwargs)
        return wrapper

    @status
    def log_in(self, user: str, password: str) -> str:
        """Hace posible el inicio de sesión"""
        if self.users[user]["passwd"] == password:
            self.user = user
            return "You are now logged in"
        return "Invalid password or user provided"
    
    @property
    @logged_in
    @status
    def package_list(self):
        packages = self.packages
        return ", ".join(packages)

    def boot(self) -> str:
        self.booted = not self.booted
        if not self.booted:
            self.user = ""
        return "Turning on" if self.booted else "Turning off"

    @logged_in
    @status
    def enable_graph_enviroment(self) -> str:
        self.graph = not self.graph
        return "Enabling graphical enviroment" if self.booted else "Disabling graphical enviroment"

    @logged_in
    @status
    def change_name(self, name: str) -> str:
        self.name = name
        return f"Changed succesfully to {self.name}"

    @logged_in
    @status
    def change_ip(self, ip):
        self.public_ip = ip
        return f"Your ip address is now {self.public_ip}"

    @logged_in
    @status
    def install_packages(self, *packages: str) -> str:
        """Instala paquetes"""
        error_msgs = []
        for package in packages:
            if package in self.packages:
                error_msg = f"Unable to install {package}, package already installed"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
            self.packages.append(package)
        return "\n".join(error_msgs)

    @logged_in
    @status
    def uninstall_packages(self, *packages:str) -> str:
        """Desinstala paquetes"""
        error_msgs = []
        for package in packages:
            if package not in self.packages:
                error_msg = f"Unable to uninstall {package}, package not found"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
            self.packages.remove(package)
        return "\n".join(error_msgs)

    @logged_in
    @status
    def generate_path(self, path: str, folder: bool) -> tuple:
        """Genera una tupla, el primer valor apunta a una zona especifica del 
        diccionario self.files, el segundo valor determina si esa operación se realizó
        correctamente"""
        if path == self.ROOT:
            return self.files[self.ROOT], True
        if self.ROOT not in path:
            return f"You cannot create files out of the bounds of the file hierarchy", False
        folders = path.strip(self.ROOT).split(self.ROOT)
        current_dir = self.files[self.ROOT]
        for folder in folders:
            if folder in current_dir:
                current_dir = current_dir[folder]
            else:
                return f"Folder {folder} does not exist in the file system", False
        return current_dir, True

    @logged_in
    @status
    def manage_files(self, operation_type:str, path1:str, file: str, folder: bool=False, path2: str = "/") -> bool:
        """Comprueba el tipo de operación y el estado del argumento folder y crear
        carpetas o ficheros en función de esto"""
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

    @logged_in
    @status
    def operate_files(self, operation_type: str, *files: str, folder: bool = False, folder_path: str = "/home/user", new_folder_path: str = "/home") -> list:
        """Recibe el tipo de operación que se quiere realizar, los ficheros 
        sobre los que se va a trabajar, y la o las carpetas de destino,
        además del parámetro folder que determina si lo que se va a crear es 
        una carpeta o un fichero, y un new_folder_path si se va a mover ficheros o carpetas """
        error_msgs = []
        file_type = "folder" if folder else "file"
        path1, status1 = self.generate_path(folder_path, folder)
        if not status1:
            error_msgs.append(path1)
            return "".join(error_msgs)
        match operation_type:
            case "mover":
                path2, status2 = self.generate_path(new_folder_path, folder)
                if not status2:
                    error_msgs.append(path2)
                    return "".join(error_msgs)
                for file in files:
                    error = False
                    status = self.manage_files(operation_type, path1, file, folder, path2=path2)
                    if error:
                        error_msgs.append(f"Something went wrong with the {file_type} {file}\n")
            case "crear" | "eliminar":
                for file in files:
                    status = self.manage_files(operation_type, path1, file, folder)
                    if not status:
                        error_msgs.append(f"Something went wrong with the {file_type} {file}\n")
            case _:
                return f"This operation is not registered"
        return "".join(error_msgs)

    @logged_in
    @status
    def manage_users(self, operation_mode: str, user: str, access_mode: str, password: str, autentication_string:str) -> str:
        """Permite la creación y borrado de usuarios, siempre y 
        cuando se pasen los permisos adecuados"""
        user_dirs = self.files[self.ROOT]["home"]
        if autentication_string != self.users["root"]["passwd"]:
            return "Invalid password, try again"
        match operation_mode, access_mode:
            case "crear", "sudo":
                if user in self.users:
                    return self.USER_EXISTANCE
                self.users[user] = {"passwd": password, "access":"restricted"}
                user_dirs[user] = self.NEW_FOLDER
                return f"The user {user} has been created"
            case "eliminar", "sudo":
                if user not in self.users:
                    return self.INVALID_USER
                del self.users[user]
                del user_dirs[user]
                return f"The user {user} has been deleted"
            case _:
                return f"You may need a higher status to continue"

    @logged_in
    @status
    def manage_user_data(
        self, operation_mode: str, user: str, 
        user_data: str, access_mode: str,
        new_password: str = "", 
        new_access_mode: str = "restricted") -> str:
        """Permite modificar la contraseña y los permisos que tienen los usuarios
        e impide modificar los permisos del usuario root"""
        match operation_mode, access_mode:
            case "modificar", "sudo":
                if user not in self.users:
                    return self.INVALID_USER
                if user == "root" and user_data != "password":
                    return "Root user permissions cannot be modified"
                match user_data:
                    case "password":
                        if new_password == "":
                            return "You forgot to enter your new password"
                        self.users[user][user_data] = new_password
                    case "permissions":
                        self.users[user][user_data] = new_access_mode
                    case _:
                        return "Invalid atribute to modify"
                return f"{user.capitalize()}'s {user_data} has been modified successfully"
            case _:
                return f"You may need a higher status to continue"

xubuntu = OS("xubuntu", "x64", "192.168.1.125")
xubuntu.boot()
print(xubuntu.log_in("ayoze", "carcassone"))
xubuntu.private_ip
xubuntu.operate_files("crear", "hola_mundo.py", folder_path="/home/user")
xubuntu.operate_files("crear", "hola_mundo", folder_path="/etc", folder=True)
xubuntu.operate_files("mover", "hola_mundo.py", folder_path="/home/user", new_folder_path="/etc")
xubuntu.operate_files("crear", "hola", folder_path="/", folder=True)
xubuntu.operate_files("crear", "hola", folder_path="/etc")
xubuntu.operate_files("crear", "hola.py", folder_path="hola")
xubuntu.operate_files("mover", "hola", folder_path="/", new_folder_path="/etc", folder=True)
print(xubuntu.operate_files("crear", "hola", folder_path="/", folder=True))
print(xubuntu.operate_files("crear", "holaa", folder_path="", folder=True))
print(xubuntu.operate_files("crear", "hola.py", folder_path="/hola"))
print(xubuntu.files)
print(xubuntu.package_list)
print(xubuntu.manage_users("crear", "pepe", "sudo", "pepee", "matraca"))
print(xubuntu.manage_users("eliminar", "pepe", "sudo", "pepee", "matrac"))
print(xubuntu.users)
print(xubuntu.manage_user_data("modificar", "pepe", "password", "sudo", new_password="zambomba"))
print(xubuntu.manage_user_data("modificar", "pepe", "permissions", "sudo", new_password="zambomba"))
xubuntu.boot()