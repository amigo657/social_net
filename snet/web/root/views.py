from aiohttp import web


class BaseRestFull(web.View):
    async def get(self):
        return web.json_response({"message": "NOT IMPLEMENTED"}, status = 206)


    async def post(self):
        return web.json_response({"message": "NOT IMPLEMENTED"}, status = 206)

    async def put(self):
        return web.json_response({"message": "NOT IMPLEMENTED"}, status = 206)

    async def patch(self):
        return web.json_response({"message": "NOT IMPLEMENTED"}, status = 206)

    async def delete(self):
        return web.json_response({"message": "NOT IMPLEMENTED"}, status = 206)