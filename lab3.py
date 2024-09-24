from abc import ABC, abstractmethod


class QueryBuilder(ABC):

    @abstractmethod
    def select(self, table: str, fields: list):
        pass

    @abstractmethod
    def where(self, condition: str):
        pass

    @abstractmethod
    def limit(self, number: int):
        pass

    @abstractmethod
    def getSQL(self) -> str:
        pass


class PostgreSQLQueryBuilder(QueryBuilder):
    def __init__(self):
        self.query = ""

    def select(self, table: str, fields: list):
        self.query = f"SELECT {', '.join(fields)} FROM {table}"

    def where(self, condition: str):
        self.query += f" WHERE {condition}"

    def limit(self, number: int):
        self.query += f" LIMIT {number}"

    def getSQL(self) -> str:
        return self.query


class MySQLQueryBuilder(QueryBuilder):
    def __init__(self):
        self.query = ""

    def select(self, table: str, fields: list):
        self.query = f"SELECT {', '.join(fields)} FROM {table}"

    def where(self, condition: str):
        self.query += f" WHERE {condition}"

    def limit(self, number: int):
        self.query += f" LIMIT {number}"

    def getSQL(self) -> str:
        return self.query


class Director:
    def __init__(self, builder: QueryBuilder):
        self.builder = builder

    def build_simple_query(self, table: str, fields: list, condition: str, limit: int):
        self.builder.select(table, fields)
        self.builder.where(condition)
        self.builder.limit(limit)
        return self.builder.getSQL()


if __name__ == "__main__":
    postgres_builder = PostgreSQLQueryBuilder()
    director = Director(postgres_builder)
    postgres_query = director.build_simple_query("users", ["id", "name", "email"], "id > 10", 5)
    print("PostgreSQL Query:", postgres_query)

    mysql_builder = MySQLQueryBuilder()
    director = Director(mysql_builder)
    mysql_query = director.build_simple_query("users", ["id", "name", "email"], "id > 10", 5)
    print("MySQL Query:", mysql_query)
