from aiohttp import web
import db
import aiohttp_jinja2


@aiohttp_jinja2.template('results.html')
async def results(request):
    async with request.app['db'].acquire() as conn:
        name = request.match_info['name']

        try:
            records = await db.get_users(conn, name)
        except Exception as e:
            raise web.HTTPNotFound(text=str(e))

        return {
            'count': len(records),
            'users': records
        }


async def add(request):
    async with request.app['db'].acquire() as conn:
        name = request.match_info['name']

        try:
            await db.add_user(conn, name)
        except Exception as e:
            raise web.HTTPNotFound(text=str(e))

        return web.Response(text='Ok. Row added')
