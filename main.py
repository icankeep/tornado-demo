import os
import asyncio
import math

import tornado.ioloop
import tornado.web
from tornado.web import StaticFileHandler


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        print('index...')
        self.render('index.html')


class LoopHandler(tornado.web.RequestHandler):
    async def get(self):
        # print('sleep 5s...')
        # await asyncio.sleep(5)
        print('start')
        for k in range(20000):
            for i in range(200):
                for j in range(20000):
                    # with open('/tmp/a.log', 'w') as f:
                    #     f.write(str(i + j))
                    math.pow(35, 13)
                    math.sqrt(j)
            await asyncio.sleep(0.00001)
        self.write("Hello, world")


def make_app():
    current_path = os.path.join(os.path.dirname(__file__))
    return tornado.web.Application([
            (r"/", MainHandler),
            (r"/loop", LoopHandler),
            (r"/static/.*", StaticFileHandler, {"path": os.path.join(current_path, "static")})
        ],
        debug=True,
        static_path=os.path.join(current_path, 'static'),
        template_path=os.path.join(current_path, 'template')
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8989)
    tornado.ioloop.IOLoop.current().start()
