from peewee import *
from config import *
from datetime import datetime

db = MySQLDatabase(DATABASE.get("database"),
                   host=DATABASE.get("host"),
                   port=DATABASE.get("port"),
                   user=DATABASE.get("user"),
                   passwd=DATABASE.get("password"))

class BaseModel(Model):
    id = PrimaryKeyField(primary_key=True, unique=True)
    database = db
    created_at = DateTimeField(default=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    updated_at = DateTimeField(default=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    def save(self, *args, **kwargs):
        self.update_at = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    class Meta:
        database = db
        order_by = ("id", )
