from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config as s_config
# !/usr/bin/python
import psycopg2

# !/usr/bin/python

import psycopg2
from utils.db_api.db_config import config


# def add_user(self,
#                    # fullname, born_address, residential_country, residential_city,
#                    # hobbies, username, reasons_chat, your_superpower, your_value,
#                    # help_community, instagram_link, linkedin_link, chat_id
#                    ):
#     sql = "INSERT INTO index_userdata (fullname, born_address, residential_country, residential_city," \
#           "hobbies, telegram, reason_chat, your_superpower, your_value," \
#           "help_community, instagram_link, linkedin_link, chat_id) " \
#           "VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13) returning *"
#     return await self.execute(sql,
#                               'fullname', 'born_address', 'residential_country', 'residential_city',
#                               'hobbies', 'username', 'reasons_chat', 'your_superpower', 'your_value',
#                               'help_community', 'instagram_link', 'linkedin_link', 123456, fetchrow=True
#                               )
async def insert_user(fullname
                      # fullname, born_address, residential_country, residential_city,
                      # hobbies, telegram, reason_chat, your_superpower, your_value,
                      # help_community, instagram_link, linkedin_link, chat_id
                      ):
    fullname = 'ff'
    """ insert a new vendor into the vendors table """
    # sql = """INSERT INTO index_userdata(
    # fullname, born_address, residential_country, residential_city,
    # hobbies, telegram, reason_chat, your_superpower, your_value,
    # help_community, instagram_link, linkedin_link, chat_id
    # )
    #     VALUES(
    #         fullname, born_address, residential_country, residential_city,
    #     hobbies, telegram, reason_chat, your_superpower, your_value,
    #     help_community, instagram_link, linkedin_link, chat_id) RETURNING id;"""
    sql = "INSERT INTO index_userdata (fullname) VALUES(fullname) returning *"

    sql += f"VALUES({fullname})  RETURNING id;"
    conn = None
    id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (fullname
                          # born_address, residential_country, residential_city,
                          # hobbies, telegram, reason_chat, your_superpower, your_value,
                          # help_community, instagram_link, linkedin_link, chat_id
                          ))
        # get the generated id back
        id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


# print(insert_user())
# !/usr/bin/python
from configparser import ConfigParser

# def config(filename='D:\python\BizNetwork\BizNetwork\database.ini', section='postgresql'):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)
#
#     # get section, default to postgresql
#     db = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             db[param[0]] = param[1]
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))
#
#     return db
#
#
# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()
#
#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
#
#         # create a cursor
#         cur = conn.cursor()
#
#         # execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')
#
#         # display the PostgreSQL database server version
#         db_version = cur.fetchone()
#         print(db_version)
#
#         # close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')
#
#
# if __name__ == '__main__':
#     connect()


# class Database:
#     def __init__(self):
#         self.pool: Union[Pool, None] = None
#
#     async def create(self):
#         self.pool = await asyncpg.create_pool(
#             user=config.DB_USER,
#             password=config.DB_PASS,
#             host=config.DB_HOST,
#             database=config.DB_NAME,
#         )

# async def execute(
#         self,
#         command,
#         *args,
#         fetch: bool = False,
#         fetchval: bool = False,
#         fetchrow: bool = False,
#         execute: bool = False,
# ):
#     async with self.pool.acquire() as connection:
#         connection: Connection
#         async with connection.transaction():
#             if fetch:
#                 result = await connection.fetch(command, *args)
#             elif fetchval:
#                 result = await connection.fetchval(command, *args)
#             elif fetchrow:
#                 result = await connection.fetchrow(command, *args)
#             elif execute:
#                 result = await connection.execute(command, *args)
#         return result

# async def create_table_users(self):
#     sql = """
#     CREATE TABLE IF NOT EXISTS Users (
#     id SERIAL PRIMARY KEY,
#     full_name VARCHAR(255) NOT NULL,
#     username varchar(255) NULL,
#     telegram_id BIGINT NOT NULL UNIQUE
#     );
#     """
#     await self.execute(sql, execute=True)

# @staticmethod
# def format_args(sql, parameters: dict):
#     sql += " AND ".join(
#         [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
#     )
#     return sql, tuple(parameters.values())

# async def add_user(self,
#                    # fullname, born_address, residential_country, residential_city,
#                    # hobbies, username, reasons_chat, your_superpower, your_value,
#                    # help_community, instagram_link, linkedin_link, chat_id
#                    ):
#     sql = "INSERT INTO index_userdata (fullname, born_address, residential_country, residential_city," \
#           "hobbies, telegram, reason_chat, your_superpower, your_value," \
#           "help_community, instagram_link, linkedin_link, chat_id) " \
#           "VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13) returning *"
#     return await self.execute(sql,
#                               'fullname', 'born_address', 'residential_country', 'residential_city',
#                               'hobbies', 'username', 'reasons_chat', 'your_superpower', 'your_value',
#                               'help_community', 'instagram_link', 'linkedin_link', 123456, fetchrow=True
#                               )

# async def select_all_users(self):
#     sql = "SELECT * FROM Users"
#     return await self.execute(sql, fetch=True)

# async def select_user(self, **kwargs):
#     sql = "SELECT * FROM Users WHERE "
#     sql, parameters = self.format_args(sql, parameters=kwargs)
#     return await self.execute(sql, *parameters, fetchrow=True)

# async def count_users(self):
#     sql = "SELECT COUNT(*) FROM index_userdata"
#     return await self.execute(sql, fetchval=True)

# async def update_user_username(self, username, telegram_id):
#     sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
#     return await self.execute(sql, username, telegram_id, execute=True)

# async def delete_users(self):
#     await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

# async def drop_users(self):
#     await self.execute("DROP TABLE Users", execute=True)

### Mahsulotlar uchun jadval (table) yaratamiz
# async def create_table_products(self):
#     sql = """
#     CREATE TABLE IF NOT EXISTS Products (
#     id SERIAL PRIMARY KEY,
#
#     -- Mahsulot kategoriyasi
#     category_code VARCHAR(20) NOT NULL,
#     category_name VARCHAR(50) NOT NULL,
#
#     -- Mahsulot kategoriya ichida ketgoriyasi ("Go'sht"->"Mol go'shti")
#     subcategory_code VARCHAR(20) NOT NULL,
#     subcategory_name VARCHAR(50) NOT NULL,
#
#     -- Mahsulot haqida malumot
#     productname VARCHAR(50) NOT NULL,
#     photo varchar(255) NULL,
#     price INT NOT NULL,
#     description VARCHAR(3000) NULL
#     );
#     """
#     await self.execute(sql, execute=True)

# async def add_product(
#         self,
#         category_code,
#         category_name,
#         subcategory_code,
#         subcategory_name,
#         productname,
#         photo=None,
#         price=None,
#         description="",
# ):
#     sql = "INSERT INTO Products (category_code, category_name, subcategory_code, subcategory_name, productname, photo, price, description) VALUES($1, $2, $3, $4, $5, $6, $7, $8) returning *"
#     return await self.execute(
#         sql,
#         category_code,
#         category_name,
#         subcategory_code,
#         subcategory_name,
#         productname,
#         photo,
#         price,
#         description,
#         fetchrow=True,
#     )

# async def get_categories(self):
#     sql = "SELECT DISTINCT category_name, category_code FROM Products"
#     return await self.execute(sql, fetch=True)

# async def get_subcategories(self, category_code):
#     sql = f"SELECT DISTINCT subcategory_name, subcategory_code FROM Products WHERE category_code='{category_code}'"
#     return await self.execute(sql, fetch=True)

# async def count_products(self, category_code, subcategory_code=None):
#     if subcategory_code:
#         sql = f"SELECT COUNT(*) FROM Products WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
#     else:
#         sql = f"SELECT COUNT(*) FROM Products WHERE category_code='{category_code}'"
#     return await self.execute(sql, fetchval=True)
#
# async def get_products(self, category_code, subcategory_code):
#     sql = f"SELECT * FROM Products WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
#     return await self.execute(sql, fetch=True)

# async def get_product(self, product_id):
#     sql = f"SELECT * FROM Products WHERE id={product_id}"
#     return await self.execute(sql, fetchrow=True)

# async def drop_products(self):
#     await self.execute("DROP TABLE Products", execute=True)
