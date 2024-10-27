from utils.utils_random import random_alphanum
from repositories.db.link_repository import LinkRepository

class ShortLinkService:
    def __init__(self):
        self.link_repository = LinkRepository()
        
    def get_link(self, short_link: str) -> str | None:
        return self.short_link_to_long_link.get(short_link, None)
    
    async def put_link(self, long_link: str) ->str:
        short_link = random_alphanum(n = 5)
        
        await self.link_repository.put_link(short_link, long_link)
        
        return short_link
    
    
    async def get_long_link(self, short_link: str) -> str|None:
        
        return await self.link_repository.get_long_link(short_link)