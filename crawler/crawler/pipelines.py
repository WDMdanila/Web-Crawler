import sqlite3


def setup_database(table_name):
    connection = sqlite3.connect('steam.db')
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (name text, sale_price text, normal_price text, quantity number)")
    return connection, cursor


class AgentsPipeline:
    def __init__(self):
        self.connection, self.cr = setup_database('agents')

    def process_item(self, item, spider):
        self.store_item(item)
        return item

    def store_item(self, item):
        if item['name'] == 'FINISHED PROCESSING' and item['normal_price'] == '%123321%' \
                and item['sale_price'] == '%123321%':
            self.connection.commit()
        else:
            pass
            self.cr.execute("INSERT INTO agents VALUES (?, ?, ?, ?)",
                            (item['name'], item['sale_price'], item['sale_price'], item['quantity']))
