from http.server import SimpleHTTPRequestHandler, test


class InlineHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        mimetype = self.guess_type(self.path)
        is_file = not self.path.endswith('/')
        if is_file and mimetype in ['text/plain', 'application/octet-stream']:
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Disposition', 'inline')
        super(InlineHandler, self).end_headers()

if __name__ == '__main__':
    handler_class = InlineHandler
    test(HandlerClass=handler_class, port=5000, bind='')
