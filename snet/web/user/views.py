import json
from aiohttp import web
from snet.web.root import views as rest
from snet.utils.mixins import LogMixin


class Create(rest.BaseRestFull, LogMixin):
    async def post(self):
        try:
            data = await self.request.json()
        except json.JSONDecodeError as error:
            self._log.error(error.args[0])
            self._exlog.error(self._trace)
            
            return web.json_response({"massage": "INVALID DATA"}, status = 503)
        self._log.debug(data)
        return web.json_response({"message": "CREATED"}, status = 201)