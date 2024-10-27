from persistent.db.link import Link
from infruatructure.sql.connect import sqlite_connection
from utils.utils_random import random_alphanum
from sqlalchemy import insert, select



class LinkRepository:
    def __init__(self):
            self._sessionmaker = sqlite_connection()
            
    async def put_link(self, short_link: str, long_link: str) -> None:
        stmp = insert(Link).values({"short_link": short_link, "long_link": long_link})
        
        async with self._sessionmaker() as session:
            await session.execute(stmp)
    async def get_link(self, short_link: str) -> str | None:
        stmp = select(Link).where (Link.short_link == short_link).limit(1)
        
        async with self._sessiomaker() as session:
            resp = await session.execute(stmp)
        row = resp.fetchone()
        if row is None:
            return None
        else:
            return row