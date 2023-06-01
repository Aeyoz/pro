from __future__ import annotations

import re
import sqlite3

DB_PATH = "twitter.db"

TWEET_EMOJI = "🐦"
RETWEET_EMOJI = "🔁"
MAX_TWEET_LENGTH = 280


def create_db(db_path: str = DB_PATH) -> None:
    """Crea la base de datos y las siguientes tablas:
    - user (id, username, password, bio)
    - tweet (id, content, user_id, retweet_from)
        └ user_id es clave ajena de user(id)
        └ retweet_from es clave ajena de tweet(id)"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    user_table = """CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username CHAR,
    password CHAR,
    bio CHAR
    ); """
    tweet_table = """CREATE TABLE tweet (
    id INTEGER PRIMARY KEY,
    content CHAR,
    user_id INTEGER,
    retweet_from INTEGER,
    FOREIGN KEY(user_id) REFERENCES user(id),
    FOREIGN KEY(retweet_from) REFERENCES tweet(id)
    );"""
    cur.execute(user_table)
    cur.execute(tweet_table)
    con.commit()

class User:

    def __init__(self, username: str, password: str, bio: str = "", user_id: int = 0):
        """Constructor de la clase User.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row).
        - Crea los atributos username, password, bio, id y logged.
        """
        self.username = username
        self.password = password
        self.id = user_id
        self.bio = bio
        self.logged = False
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def save(self) -> None:
        """Guarda en la base de datos un objeto de tipo User.
        Además actualiza el atributo "id" del objeto a partir de lo que devuelve la inserción.
        """
        self.cur.execute(
            "INSERT INTO user (username, password, bio) VALUES (?,?,?)",
            (self.username, self.password, self.bio),
        )
        self.id = self.cur.lastrowid
        self.con.commit()

    def login(self, password: str) -> None:
        """Realiza el login del usuario."""
        self.logged = password == self.password

    def tweet(self, content: str) -> Tweet:
        """Crea un tweet con el contenido indicado y lo almacena en la base de datos.
        - Utiliza el método save propio de la clase Tweet.
        - Hay que retornar el tweet creado.
        - Si el usuario no está logeado hay que lanzar una excepción de tipo TwitterError
        con el mensaje: User <usuario> is not logged in!
        - Si el tweet supera el límite de caracteres hay que lanzar una excepción de tipo
        TwitterError con el mensaje: Tweet hasta more than 280 chars!"""
        if len(content) > 280:
            raise TwitterError("Tweet has more than 280 chars!")
        if not self.logged:
            raise TwitterError(f"User {self.username} is not logged in!")
        new_tweet = Tweet(content)
        new_tweet.save(self)
        return new_tweet

    def retweet(self, tweet_id: int) -> Tweet:
        """Crea un retweet con el contenido indicado y lo almacena en la base de datos.
        - Utiliza el método save propio de la clase Tweet.
        - Hay que retornar el tweet creado.
        - Si el usuario no está logeado hay que lanzar una excepción de tipo TwitterError
        con el mensaje: User <usuario> is not logged in!
        - Si tweet_id no existe en la base de datos hay que lanzar una excepción de tipo
        TwitterError con el mensaje: Tweet with id <id> does not exist!"""
        if not self.logged:
            raise TwitterError(f"User {self.username} is not logged in!")
        existance = self.cur.execute("SELECT COUNT(*) FROM tweet WHERE id=?", [self.id]).fetchone()
        if not existance[0]:
            raise TwitterError(f"Tweet with id {tweet_id} does not exist!")
        data = self.cur.execute("SELECT * FROM tweet WHERE id=?", [tweet_id]).fetchone()
        return Tweet.from_db_row(data)

    @property
    def tweets(self):
        """Función generadora que devuelve todos los tweets propios del usuario.
        - Lo que se devuelven son objetos de tipo Tweet (usar el método from_db_row)."""
        tweets = self.cur.execute(
            "SELECT * FROM tweet WHERE user_id=?", [self.id]
        ).fetchall()
        for tweet in tweets:
            yield Tweet.from_db_row(tweet)

    def __repr__(self):
        """Representa un usuario con el formato:
        <usuario>: <bio>"""
        return f"{self.username}: {self.bio}"

    @classmethod
    def from_db_row(cls, row: sqlite3.Row):
        """Crea un objeto de tipo User a partir de una fila de consulta SQL"""
        return User(row["username"], row["password"], row["bio"], row["id"])


class Tweet:

    def __init__(self, content: str = "", retweet_from: int = 0, tweet_id: int = 0):
        """Constructor de la clase Tweet.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row)
        - Crea los atributos _content, retweet_from e id.
        - retweet_from indica el id del tweet que se retuitea.
        - Si es un retweet el contenido debe ser la cadena vacía.
        """
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self._content = content
        self.retweet_from = retweet_from
        self.id = tweet_id

    @property
    def is_retweet(self) -> bool:
        """Indica si el tweet es un retweet."""
        return self.retweet_from > 0

    @property
    def content(self) -> str:
        """Devuelve el contenido del tweet.
        - Si es un retweet el contenido habrá que buscarlo en el tweet retuiteado."""
        if self.is_retweet:
            content = self.cur.execute("SELECT content FROM tweet WHERE id=?", [self.retweet_from]).fetchone()["content"]
            return content
        return self._content

    def save(self, user: User) -> None:
        """Guarda el tweet en la base de datos.
        - El parámetro user es el usuario que escribe el tweet.
        Además actualiza el atributo "id" del objeto a partir de lo que devuelve la inserción.
        """
        user_id = user.id
        self.cur.execute(
            "INSERT INTO tweet (content, user_id, retweet_from) VALUES (?, ?, ?)",
            (self._content, user_id, self.retweet_from),
        )
        self.id = self.cur.lastrowid
        self.con.commit()

    def __repr__(self):
        """Representa un tweet con el formato:
        <emoji> <content> (id=<id>)"""
        return f"{TWEET_EMOJI if not self.is_retweet else RETWEET_EMOJI} {self.content} (id={self.id})"

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Tweet:
        """Crea un objeto de tipo Tweet a partir de una fila de consulta SQL"""
        return Tweet(row["content"], row["retweet_from"], row["id"])


class Twitter:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self):
        """Constructor de la clase Twitter.
        - Crea los atributos con y cur para la conexión a la base de datos (con factoría Row)
        """
        pass

    def add_user(self, username: str, password: str, bio: str = "") -> User:
        """Crea un objeto de tipo User y lo guarda en la base de datos.
        - Haz uso de los métodos ya creados.
        - Hay que retornar el objeto creado.
        - La contraseña debe seguir el siguiente formato:
          * Empezar con una arroba o un signo igual.
          * Continuar con 2, 3 o 4 dígitos.
          * Continuar con 2, 3 o 4 letras de la A-Z (incluyendo minúsculas).
          * Terminar con una exclamación o un asterisco.
        Si no sigue este formato hay que elevar una excepción de tipo TwitterError
        con el mensaje: Password does not follow security rules!"""
        valid_passwd_format = r"\b@?=?\d{2,4}[A-Za-z]{2,4}\*?!?\b"
        passwd = re.search(password, valid_passwd_format)
        if isinstance(passwd, re.Match):
            raise TwitterError("Password does not follow security rules!")
        self.cur.execute("INSERT INTO user (username, password, bio) VALUES (?, ?, ?)", [username, password, bio])
        db_row = self.cur.execute("SELECT * FROM user WHERE username=?", [username]).fetchone()
        new_user = User.from_db_row(db_row)
        new_user.save()
        return new_user

    def get_user(self, user_id: int) -> User:
        """Devuelve el usuario con el user_id indicado.
        Si el usuario no existe hay elevar una excepción de tipo TwitterError con el mensaje:
        User with id <id> does not exist!"""
#        existance = self.cur.execute("SELECT COUNT(*) FROM user WHERE id=?", [user_id]).fetchone()[0] 
#        if not existance:
#            raise TwitterError(f"User with id {user_id} does not exist!")
        data = self.cur.execute("SELECT * FROM user WHERE id=?", [user_id]).fetchone()
        return User.from_db_row(data)

class TwitterError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
