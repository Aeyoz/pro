from __future__ import annotations

import sqlite3

DB_PATH = 'todo.db'
TASK_DONE_SYMBOL = '✔'
TASK_PENDING_SYMBOL = '⎕'


class Task:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como diccionarios.
    - cur: para el cursor de manejo.'''

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    con.row_factory = sqlite3.Row

    def __init__(self, name: str, done: bool = False, id: int = -1):
        '''Crea los atributos homónimos a los parámetros'''
        self.name = name
        self.done = done
        self.id = id

    def save(self):
        '''Guarda esta tarea en la base de datos.
        El identificador asignado en la base de datos se debe usar para actualizar el
        atributo id de la tarea.'''
        Task.cur.execute("INSERT INTO tasks (name, done) VALUES (?,?)", (self.name, self.done))


    def update(self):
        '''Actualiza la tarea (nombre y estado) en la base de datos'''
        Task.cur.execute("UPDATE tasks SET name=?, done=?", (self.name, self.done))

    def check(self):
        '''Marca la tarea como completada. Haz uso también de .update()'''
        self.done = True
        self.update()

    def uncheck(self):
        '''Marca la tarea como no completada. Haz uso también de .update()'''
        self.done = False
        self.update()

    def __repr__(self):
        '''Muestra la tarea en formato:
        <SYMBOL> <name> (id=<id>)'''
        symbol = TASK_DONE_SYMBOL if self.done else TASK_PENDING_SYMBOL
        return f"{symbol}{self.name} (id={self.id})"

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        '''Construye una nueva tarea a partir de una fila de consulta devuelta por execute()'''
        _id, name, done = row
        return Task(name, done, _id)

    @classmethod
    def get(cls, task_id: int) -> Task:
        '''Devuelve un objeto Task desde la consulta a la base de datos'''
        sql = Task.cur.execute("SELECT * from tasks WHERE id=?", (task_id,))
        task = sql.fetchone()
        return Task.from_db_row(task)

class ToDo:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como diccionarios.
    - cur: para el cursor de manejo.'''
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    con.row_factory = sqlite3.Row

    def create_db(self):
        '''Crea la base de datos con los campos "id", "name" y "done"'''
        ToDo.cur.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY, name CHAR, done INTEGER)")

    def get_tasks(self, *, done: int = -1):
        '''Devuelve todas las tareas como objetos de tipo Task consultando la BBDD.
        - Si done = 0 se devuelven las tareas pendientes.
        - Si done = 1 se devuelven las tareas completadas.
        Ojo! Esto es una función generadora.'''
        if done != -1:
            tasks_objs = self.cur.execute("SELECT * FROM tasks WHERE done = ?", bool(done))
            tasks = tasks_objs.fetchall()
            for task in tasks:
                yield f"{task}"
        tasks_objs = self.cur.execute("SELECT * FROM tasks")
        tasks = tasks_objs.fetchall()
        for task in tasks:
            yield f"{task}"

    def add_task(self, name: str):
        '''Añade la tarea con nombre "name"'''
        new_task = Task(name)
        new_task.save()
        
    def complete_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como completada'''
        

    def reopen_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como pendiente'''
        pass
