from typing import Optional


class UnauthorizedDB:
    def query(self) -> None:
        print("RealSubject: Got Query!")

class AuthProxy:
    def __init__(self, db: UnauthorizedDB, user: Optional[str] = None) -> None:
        self._real_db = db
        self.user = user

    def query(self) -> None:
        self._real_db.query()


if __name__ == "__main__":
    real_db = UnauthorizedDB()
    
    proxy_access = AuthProxy(real_db)
    proxy_access.query()