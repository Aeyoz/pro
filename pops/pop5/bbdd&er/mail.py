import re
import sqlite3

DB_PATH = "mail.db"

"""
Diagrama de clases:
        ┌──────────┐                  ┌──────────┐
        │          │                  │          │
     ┌──┤  DBUtils ├─────┐            │ MailError│
     │  │          │     │            │          │
     │  └──────────┘     │            └──────────┘
     │                   │
     │                   │
     │                   │
     ▼                   ▼
┌─────────┐      ┌─────────────┐
│         │      │             │
│ Mail    │      │ MailServer  │
│         │      │             │
└─────────┘      └─────────────┘
"""


class DbUtils:
    def __init__(self, db_path: str = DB_PATH):
        """Crea la conexión a la base de datos y el cursor correspondiente.
        También establece la factoría de registros como filas (diccionarios).
        Atributos a crear:
        - con
        - cur
        """
        self.con = sqlite3.connect(db_path)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()


class Mail(DbUtils):
    def __init__(self, sender: str, recipient: str, subject: str, body: str):
        """Construye un objeto Mail con los mismos atributos que parámetros.
        Esta clase hereda de DbUtils..."""
        super().__init__()
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send(self) -> None:
        """Simula el envío de este correo guardando todos sus campos en la tabla activity"""
        sql = "INSERT INTO activity (sender, recipient, subject, body) VALUES (?, ?, ?, ?)"
        self.cur.execute(sql, [self.sender, self.recipient, self.subject, self.body])
        self.con.commit()

    def __str__(self):
        """Representa un objeto de tipo Mail de la siguiente forma:
        From: <remitente>
        To: <destinatario>
        ---
        <asunto pasado a mayúsculas>
        <cuerpo del correo>
        """
        return f"""From: {self.sender}\nTo: {self.recipient}\n---\n{self.subject.upper()}:\n{self.body}"""


class MailServer(DbUtils):
    def __init__(self, username: str, password: str):
        """Construye un MailServer guardando los atributos de nombre de usuario y contraseña.
        También es necesario crear un atributo logged (booleano) que indique si se ha logeado.
        Esta clase hereda de DbUtils..."""
        super().__init__()
        self.username = username
        self.password = password
        self.logged = False

    def login(self) -> None:
        """Realiza/comprueba el login del usuario actualizado los atributos:
        - domain
        - logged
        La comprobación hay que hacerla consultando la base de datos.
        """
        sql = "SELECT COUNT(*), domain FROM login WHERE password=?"
        correct_user_data = self.cur.execute(sql, (self.password,)).fetchone()
        if correct_user_data[0]:
            self.logged = True
            self.domain = correct_user_data["domain"]
        else:
            self.domain = ""

    @staticmethod
    def login_required(method):
        """Decorador que lanza una excepción MailError si el usuario no está logeado.
        El mensaje de la excepción debe ser:
        User "<username>" not logged in!
        Ojo! La excepción recibe en su constructor tanto el mensaje de error
        como el objeto actual de tipo MailServer."""

        def wrapper(self, *args, **kwargs):
            if not self.logged:
                raise MailError(f'User "{self.username}" not logged in!', self)
            return method(self, *args, **kwargs)

        return wrapper

    @property
    def sender(self) -> str:
        """Formato: <nombre-de-usuario>@<dominio>
        No hay que aplicar decorador pero debes saber que esta propiedad
        sólo va a funcionar si se ha hecho login previamente, ya que en otro caso
        no disponemos del dominio."""
        return f"{self.username}@{self.domain}"

    @login_required
    def send_mail(self, *, recipient: str, subject: str, body: str) -> None:
        """Realiza el "envío" de un correo a través del método definido en Mail.
        Si recipient no tiene un formato válido de email se debe lanzar una excepción
        de tipo MailError con el mensaje:
        Recipient "<recipient>" has invalid mail format!
        Ojo! La excepción recibe en el constructor tanto el mensaje
        como el objeto actual de tipo MailServer."""
        er = r"^\w+@\w+\.\w+$"
        if not re.match(er, recipient):
            raise MailError(f'Recipient "{recipient}" has invalid mail format!', self)
        sql = "INSERT INTO activity (sender, recipient, subject, body) VALUES (?, ?, ?, ?)"
        self.cur.execute(sql, [self.sender, recipient, subject, body])
        self.con.commit()

    @login_required
    def get_emails(self, sent: bool = True):
        """Consulta los mails almacenados hasta el momento.
        - Si el parámetro sent está a True se devuelven los enviados por el usuario.
        - Si el parámetro sent está a False se devuelven los recibidos por el usuario.
        Debe ser una función generadora que devuelva objetos de tipo Mail."""
        sql = f"SELECT * FROM activity WHERE "
        if sent:
            sql += "sender=?"
        else:
            sql += "recipient=?"
        for mail in self.cur.execute(sql, [self.username]).fetchall():
            yield Mail(mail["sender"], mail["recipient"], mail["subject"], mail["body"])


class MailError(Exception):
    def __init__(self, message: str, mail_handler: Mail | MailServer):
        """Hay que cerrar la conexión a la base de datos"""
        mail_handler.con.close()
        super().__init__(message)
