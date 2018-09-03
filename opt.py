#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options  # 新导入的options模块

tornado.options.define("port", default=8000, type=int, help="run server on the given port.")  # 定义服务器监听端口选项
tornado.options.define("itcast", default=[], type=str, multiple=True, help="itcast subjects.")  # 无意义，演示多值情况


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Itcast!")


if __name__ == "__main__":
    # tornado.options.parse_command_line()
    tornado.options.parse_config_file("./config.py")  # 仅仅修改了此处
    print(tornado.options.options.itcast)  # 输出多值选项
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
