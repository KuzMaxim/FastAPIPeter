from fastapi import FastAPI, Response, status, Path, HTTPException
from pydantic import BaseModel
from services.short_link_service import ShortLinkService
import re
#from database.database_sqlite import create_db


app = FastAPI(title = "Сервис генерации коротких ссылок")

short_link_service = ShortLinkService()
#create_db()

@app.get("/health")
def hello_world() -> str:
    """
        функция возвращает ok
        практической пользы не несет, но очень дорога моему сердцу
    """
    return "ok"

class PutLink (BaseModel):
    link: str
    
@app.put("/link")
async def put_link(long_link: PutLink) -> PutLink:
    """добавляем длинную ссылку
    проводим валидацию: если ссылка вида 
    1)http(s)://(любые символы в любом количестве).(любые латинские буквы в любом количестве)
    2)(любые символы в любом количестве).(любые латинские буквы в любом количестве)
    Иначе выдаем ошибку 422
    """
    if re.match(r"https?://.+\.\w+", long_link.link) == None:
        if re.match(r".+\.\w+", long_link.link) == None:
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            short_link = await short_link_service.put_link("https://" + long_link.link)
    else:
        short_link = await short_link_service.put_link(long_link.link)
    return PutLink(link = f"http://localhost:8000/short/{short_link}")

@app.get("/short/{short_link}")
async def get_link(short_link:str = Path(...))->Response:
    """
    проверка на наличие ссылки
    в случае неудачи 404
    """
    long_link = await short_link_service.get_link(short_link)
    if long_link is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return Response(
        content = None,
        headers = {"Location" : long_link},
        status_code = status.HTTP_301_MOVED_PERMANENTLY
    )