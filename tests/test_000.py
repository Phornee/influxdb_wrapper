import unittest
import sys

from influxdb_wrapper import influxdb_factory

import logging

log = logging.getLogger('influxdb_wrapper')
sh = logging.StreamHandler(sys.stdout)
log.addHandler(sh)
log.setLevel(logging.INFO)

class Testing(unittest.TestCase):
    db = influxdb_factory(db_type='mock')
    db.openConn(None)

    def test_insert(self):
        points = [
                    {"tags": {"sensorid": 0}, "fields": {"temp": 20.0, "humidity": 50.0}},
                    {"tags": {"sensorid": 0}, "fields": {"temp": 21.0, "humidity": 50.1}},
                    {"tags": {"sensorid": 1}, "fields": {"temp": 10.0, "humidity": 100.0}}
                 ]
        self.db.insert('DHT22', points)

    def test_select(self):
        points = self.db. select('DHT22', [('sensorid', 0)], order_by='time', order_asc=False, limit=1)
        self.assertEqual(len(points), 1)


if __name__ == '__main__':
    unittest.main()
