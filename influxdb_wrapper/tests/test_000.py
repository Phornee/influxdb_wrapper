import unittest
import os
import sys
import inspect
from pathlib import Path

THIS_FOLDER = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(0, os.path.dirname(THIS_FOLDER))
from influxdb_conn import InfluxDBConn  # noqa
from mockdb_conn import InfluxMockDBConn  # noqa


class Testing(unittest.TestCase):
    db = InfluxMockDBConn()

    def test_index(self):
        points = [
                    {
                        "tags": {"sensorid": self.config['id']},
                        "fields": {"temp": 20.0, "humidity": 50.0}
                    }
                ]
        self.db.insert('DHT22', points)


if __name__ == '__main__':
    unittest.main()
