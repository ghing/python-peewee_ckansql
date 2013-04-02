from peewee import Database
import ckansql


class CkanDatabase(Database):
    def _connect(self, database, **kwargs):
        return ckansql.connect(database, **kwargs)
