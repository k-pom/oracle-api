import tornado.ioloop
import tornado.web
from lib.l5r import get_image_by_name

class MainHandler(tornado.web.RequestHandler):
    def get(self, name):
        get_image_by_name(name)
        self.write("url")

application = tornado.web.Application([
    (r"/cards/(.*)\.jpg", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()