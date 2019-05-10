#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Tao Huang'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

port = 9000
host = '127.0.0.1'

def index(request):
    return web.Response(body=b'<h1>Python3 web app</h1>',headers={'content-type':'text/html'})

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), host, port)
    logging.info('server started at http://'+host+':'+str(port))
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
