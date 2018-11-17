from aiohttp import web
from routes import setup_routes
from settings import get_config
from db import init_pg, close_pg
import aiohttp_jinja2
import jinja2


def init_app():
    app = web.Application()

    app['config'] = get_config()

    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('sample', 'templates'))

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    setup_routes(app)

    return app


if __name__ == '__main__':
    app = init_app()
    config = get_config()
    web.run_app(app, port=8081)
