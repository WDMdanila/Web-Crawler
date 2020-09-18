import sqlite3


def setup_database():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(title text, price text, in_stock number)")
    return connection, cursor


class BookPipeline:
    def __init__(self):
        self.connection, self.cr = setup_database()

    def process_item(self, item, spider):
        self.store_item(item)
        return item

    def store_item(self, item):
        if item['title'] == 'FINISHED PROCESSING' and item['price'] == '%123321%':
            self.connection.commit()
        else:
            self.cr.execute("INSERT INTO books VALUES (?, ?, ?)", (item['title'], item['price'], item['in_stock']))
