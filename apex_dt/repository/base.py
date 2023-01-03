import sqlite3
from contextlib import contextmanager
from typing import TypeVar, Generic, Iterator, Union

from loguru import logger
from pypika import Table, Query
from pypika.terms import Field
from pypika.queries import QueryBuilder

from apex_dt.config import SQLITE_DB_PATH


_T = TypeVar('_T')


class BaseSQLiteRepository(Generic[_T]):
    __slots__ = ('url', 'table')

    def __init__(self, *, table_name: str, schema: str = None, url: str = SQLITE_DB_PATH):
        self.url = url
        self.table = Table(name=table_name, schema=schema)

    @contextmanager
    def connection(self, *, con: sqlite3.Connection = None) -> Iterator[sqlite3.Connection]:
        if con is not None:
            yield con
        else:
            c: sqlite3.Connection
            with sqlite3.connect(self.url) as c:
                yield c

    def table_columns(self) -> tuple[Field, ...]:
        return (self.table.star,)

    def deserialize(self, *, row: Union[sqlite3.Row, None]) -> Union[_T, None]:
        """Repositories inheriting this base class should implement this."""
        raise NotImplementedError()
    
    def serialize(self, *, model: _T) -> dict:
        """Repositories inheriting this base class should implement this."""
        raise NotImplementedError()

    def fetchone(self, *, query: QueryBuilder, con: sqlite3.Connection = None) -> sqlite3.Row:
        c: sqlite3.Connection
        with self.connection(con=con) as c:
            cursor: sqlite3.Cursor = c.execute(str(query))
            row = cursor.fetchone()

        return row

    def get(self, *, id: int, con: sqlite3.Connection = None) -> Union[_T, None]:
        query = (Query
                .from_(self.table)
                .select(*self.table_columns())
                .where(self.table.id == id))
        logger.trace(f'{query=}')

        row = self.fetchone(query=query, con=con)
        return self.deserialize(row=row)

    def create(self, *, instance: _T, con: sqlite3.Connection = None) -> Union[_T, None]:
        data = self.serialize(model=instance)
        query = (Query
                .into(self.table)
                .insert((*data.values(),))
                .returning(*self.table_columns()))
        logger.trace(f'{query=}')

        row = self.fetchone(query=query, con=con)
        return self.deserialize(row=row)

    def update(self, *, instance: _T, con: sqlite3.Connection = None) -> Union[_T, None]:
        data = self.serialize(model=instance)
        query = (Query
                .into(self.table)
                .update((*data.values(),))
                .where(self.table.id == instance.id)
                .returning(*self.table_columns()))
        logger.trace(f'{query=}')

        row = self.fetchone(query=query, con=con)
        return self.deserialize(row=row)

    def delete(self, *, id: int, con: sqlite3.Connection = None) -> int:
        query = (Query
                .from_(self.table)
                .delete()
                .where(self.table.id == id))
        logger.trace(f'{query=}')

        row = self.fetchone(query=query, con=con)
        return row[0]


