import os
import csv


class CsvManager:
    def __init__(self, filename):
        self.filename = filename

    def check_exists(self):
        if not os.path.exists(self.filename):
            return False
        return True

    def read(self):
        if self.check_exists():
            with open(file=self.filename, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                return list(reader)
        return []

    def write(self, data: list):
        with open(file=self.filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def append(self, row: list):
        rows = self.read()
        rows.append(row)
        self.write(data=rows)

    def write_headers(self, headers: list):
        rows = self.read()
        if rows:
            rows[0] = headers
        else:
            rows.append(headers)

        self.write(rows)


users_manager = CsvManager(filename="data/users.csv")
message_manager = CsvManager(filename="data/messages.csv")
chat_manager = CsvManager(filename="data/chats.csv")
