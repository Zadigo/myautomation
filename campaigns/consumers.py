import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from campaigns.models import Campaign

class ScrappingConsumer(AsyncJsonWebsocketConsumer):
    @database_sync_to_async
    async def get_campaign(self, id):
        return Campaign.objects.get(id=id)

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        await self.close()

    async def receive_json(self, content, **kwargs):
        await self.send_json({'name': 'Kendall'})

    async def campaigns_run(self):
        campaign_id = self.scope['url']['id']
        campaign = await self.get_campaign(id=None)
