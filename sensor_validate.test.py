import unittest
import sensor_validate
import Constant


class SensorValidatorTest(unittest.TestCase):
    def test_reports_none_error_when_stream_none(self):
        self.assertEqual(
            sensor_validate.validate_sensor_stream("soc", None),
            Constant.STATUS_CODES["400"]
        )

    def test_reports_invalid_param(self):
        self.assertEqual(
            sensor_validate.validate_sensor_stream("temp", [20.2, 20.3, 20.4, 20.5]),
            Constant.STATUS_CODES["404"]
        )

    def test_reports_spike_when_soc_jumps(self):
        self.assertEqual(
            sensor_validate.validate_sensor_stream("soc", [0.0, 0.01, 0.5, 0.51]),
            Constant.STATUS_CODES["500"]
        )

    def test_reports_spike_when_current_jumps(self):
        self.assertEqual(
            sensor_validate.validate_sensor_stream("current", [0.03, 0.03, 0.03, 0.33]),
            Constant.STATUS_CODES["500"]
        )


if __name__ == "__main__":
    unittest.main()
