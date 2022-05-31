from aiohttp import WSMsgType, web


async def echo(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                print('message received:', msg.data)
                await ws.send(msg.data + '/server')

    return ws


app = web.Application()
app.router.add_get('/', echo)
web.run_app(app)
