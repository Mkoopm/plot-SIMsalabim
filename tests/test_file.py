import pytest
import simulation.file


class test_file_parameter():
    def __init__(self) -> None:
        self.par = simulation.file.Parameters()
        self.par.read('device_parameters.txt')

    def test_parameter_get(self):
        assert self.par.get_val('log_file') == 'log.txt'
        assert self.par.get_comment('log_file') == 'name of log file'

        assert self.par.get_category('Ions') == ['CNI', 'CPI', 'mob_ion_spec', 'ion_red_rate']
        