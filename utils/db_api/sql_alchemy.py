from sqlalchemy import create_engine, text
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+pg8000://postgres:1@localhost/biz_db")
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()  # extracting the metadata
index_userdata = db.Table('index_userdata', metadata, autoload=True,
                          autoload_with=engine)  # Table object
query = index_userdata.select()  # SELECT * FROM cat
exe = conn.execute(query)  # executing the query
result = exe.fetchmany(5)  # extracting top 5 results
output = conn.execute(index_userdata.select()).fetchall()


async def add_user(fullname, born_address, residential_country, residential_city,
                   hobbies, telegram, reason_chat, your_superpower, your_value,
                   help_community, instagram_link, linkedin_link, chat_id,
                   company_city, company_country, company_name, company_position,
                   company_website):
    # fullname = 'fullnamesojojitr'
    # sql_query = f"-- INSERT INTO index_userdata"
    # sql = text(sql_query)
    result_query = conn.execute(
        """INSERT INTO index_userdata (
        fullname, born_address, residential_country, residential_city,
        hobbies, telegram, reason_chat, your_superpower, your_value,
        help_community, instagram_link, linkedin_link, chat_id,
        company_city,company_country,company_name,company_position,
        company_website
        ) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)returning  id""",
        (fullname, born_address, residential_country, residential_city,
         hobbies, telegram, reason_chat, your_superpower, your_value,
         help_community, instagram_link, linkedin_link, chat_id,
         company_city, company_country, company_name, company_position,
         company_website
         ))
    rows = [dict(data) for data in result_query]
    return result_query

# def count_elements(table):
#     sql_query = f"SELECT COUNT(*) FROM {table};"
#     sql = text(sql_query)
#     result_query = conn.execute(sql)
#     count = [dict(data) for data in result_query]
#     return count[0]['count']


# print(add_user())
