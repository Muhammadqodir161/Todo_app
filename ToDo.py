#Todo
from http.server import BaseHTTPRequestHandler
import json
from Database import DatabaseManager
db_manager = DatabaseManager("TodoBackend.db")
class TodoHttpRequestHandler(BaseHTTPRequestHandler):
    def set_header(self,status=200):
            self.send_response(status)
            self.send_header('Content-type','application/json')
            self.end_headers()
            
    def do_GET(self):
        if self.path == '/':
            self.send_response()  
            Todo=db_manager.get_all_Todo() 
            self.wfile.write(json.dumps(Todo).encode())
            
    def do_POST(self):
         if self.path == '/create-Todo':
            content_lengh = int(self.header['Content-type','application/json'])
            put_data = self.rfile.read(content_lengh)
            task_item=json.loads(put_data.decode())
            db_manager.update_Todo(
              task_id,task_item['task'],task_item['completed']
          )
            self.set_header(201)            
             
    def do_PUT(self):
         if self.path.startswith('/Todo/'):
          task_id = int(self.path.split('/')[-1])
          content_lengh = int(self.header['Content-type','application/json'])
          put_data = self.rfile.read(content_lengh)
          task_item=json.loads(put_data.decode())
          db_manager.update_Todo(
              task_id,task_item['task'],task_item['completed']
          )
          self.set_header(201)
          
    def do_DELETE(self):
        if self.path.startswith('/Todo/'):
          task_id = int(self.path.split('/')[-1])
          db_manager.delete_task(task_id)
          self.set_header(204)

def run(server_class=HTTPServer, handler_class=TodoHttpRequestHandler):
     server_address = ('', 8000)
     httpd = server_class(server_address, handler_class)
     httpd.serve_forever()
