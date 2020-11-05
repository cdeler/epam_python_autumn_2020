from lib.simple_logger import Logger
from lib.database import DatabaseClient


def run():
    db = DatabaseClient(logger_cls=Logger)
    # now i need to use not_so_simple_logger, but i dont know how!
    print(db.get_data())


if __name__ == '__main__':
    run()
