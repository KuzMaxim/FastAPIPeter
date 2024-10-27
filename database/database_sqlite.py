import sqlite3 as sq


with sq.connect("longshortlink.db", check_same_thread= False) as con:
    cur = con.cursor()
    def create_db():
        cur.execute ("""CREATE TABLE IF NOT EXISTS links(
        short_link TEXT PRIMARY KEY NOT NULL,
        long_link TEXT NOT NULL
        );""")
    def add_link_to_db(short_link: str, long_link: str) -> None:
        cur.execute("""INSERT INTO links (short_link, long_link) VALUES (?, ?);""",(short_link,long_link))
        con.commit()