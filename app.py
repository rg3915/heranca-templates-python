from jinja2 import Environment, FileSystemLoader
from http.server import HTTPServer, BaseHTTPRequestHandler

env = Environment(loader=FileSystemLoader('templates'))


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            template = env.get_template('index.html')
            html = template.render(
                nome='Regis',
                videos=[
                    {
                        'titulo': 'Mini Curso A Essência do Django',
                        'descricao': 'Aprenda os conceitos fundamentais do Django e como criar seu primeiro projeto.',
                        'link': 'https://youtu.be/mlaCLGItR7Q?si=7AFw4dJVkmoK7vCR',
                        'thumbnail': 'https://img.youtube.com/vi/mlaCLGItR7Q/maxresdefault.jpg'
                    },
                    {
                        'titulo': 'A Essência do Django parte 2',
                        'descricao': 'Entenda como trabalhar com models e o ORM do Django.',
                        'link': 'https://youtu.be/Qu2QTxdYfZ4?si=NsloJHNAzlF58p9b',
                        'thumbnail': 'https://img.youtube.com/vi/Qu2QTxdYfZ4/maxresdefault.jpg'
                    },
                    {
                        'titulo': 'Introdução ao Django | Review',
                        'descricao': 'Reveja os principais assuntos do Django de forma rápida e simples.',
                        'link': 'https://youtu.be/MzlznUJeP4U?si=0M55RxKPqYFAtBnq',
                        'thumbnail': 'https://img.youtube.com/vi/MzlznUJeP4U/maxresdefault.jpg'
                    },
                ]
            )

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))

        elif self.path == '/templates':
            template = env.get_template('templates.html')
            html = template.render()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))

        elif self.path == '/sobre':
            template = env.get_template('about.html')
            html = template.render()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'<h1>404 - Pagina nao encontrada</h1>')


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), MyHandler)
    print('Servidor rodando em http://localhost:8000')
    server.serve_forever()
