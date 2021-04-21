from Snapshot import Snapshot


class Parser:

    def __init__(self):
        pass

    def parse_database(self, database):

        snapshots = []
        for key, value in database.file_list.items():
            snapshots.append(self.parse_snapshot(key, value))
        pass

    def parse_snapshot(self, key, value):
        snapshot = Snapshot()
        
        return snapshot

