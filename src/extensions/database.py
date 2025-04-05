
# ------------------
# Postgres Database Connection: Soon
# ------------------

# ...

# ------------------
# SQLite3 Database Connection
# ------------------

# import sqlite3

# from colorama import Fore, Style

# DATABASE_PATH = "yourdatabase.db"

# try:
#     conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
#     print(Fore.GREEN + "Connected to the database successfully" + Style.RESET_ALL)
#     conn.close()
# except sqlite3.Error:
#     raise Exception(Fore.RED + "Failed to connect to the database" + Style.RESET_ALL)


# def get_db():
#     conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
#     conn.row_factory = sqlite3.Row
#     try:
#         yield conn
#     finally:
#         conn.close()