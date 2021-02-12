# server code derived from https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json


class Handler(BaseHTTPRequestHandler):
    user_steamID = 0
    media_playing = False

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print(post_data)
        data = json.loads(post_data)

        try:
            if data['map']['phase'] == 'live':
                if data['round']['phase'] == 'freezetime':
                    self.user_steamID = data['player']['steamid']
                    # can't be spectating during freezetime, and match starts in freezetime
                    # so no risk of having this variable be "uninitialized" when we need it
                    # we only really need this once but nothing bad should happen from repeating

                if data['player']['steamid'] == self.user_steamID and data['player']['state'][
                    'health'] == 0 and not self.media_playing:
                    # when dead, start media
                    # TODO: implement hit media button
                    self.media_playing = True
                    print("I died!")

                if data['round']['phase'] == 'live' and self.media_playing:
                    # when round goes live again, pause media
                    # TODO: implement hit media button
                    self.media_playing = False
                    print("Round's starting!")


        except KeyError:
            print("Not in game yet!")
            pass

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=Handler, port=4750):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
