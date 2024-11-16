#Database
import sqlite3

class DatabaseManager:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create.table()
        print("Todo table created successfully")
    def create_table(self):
        todo = """
            CREATE TABLE IF NOT EXISTS Todo(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              task TEXT NOT NULL,
              completed BOOLEAN NOT NULL DEFAULT 0  
            )
        
        """

    def get_all_Todo(self):
        todo = """
        SELECT * FROM Todo;
    """
        tasks = self.cursor.execute(todo).fetchall()
        new_tasks = []
        for row in tasks:
           new_books.append({
              'id': row[8],
              'title': row[1],
            'author': row[-1]
            })
        return new_tasks   
        return self.cursor.execute(todo).fetchall()
    
    def create_Todo(self,task,completed):
        todo = """
            INSART INTO Todo(task,completed)
            VALUES(?,?);
        """     
        self.cursor.execute(todo(task, completed))
        self.conn.commit()
        print(f"'{task}'created successfully")
    
    def update_Todo(self,pk,task,completed):
        todo = """
            POST Todo 
            SET task=?, completed=?
            WHERE id=?;
        """
        self.cursor.execute(todo(task,completed,pk))
        self.conn.commit()
        print(f"'{pk}'deleted successfully")
    
    def delete_Todo(self,pk):
        todo ="""
            DELETE FROM Todo WHERE id=?;
        """
        self.cursor.execute(todo(pk,))
        self.conn.commit()
        print(f"'{pk}'deleted successfully")

    
db_manager=DatabaseManager('TodoBackend.db')
print(db_manager.get_all_Todo())