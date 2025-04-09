from dataclasses import dataclass


@dataclass
class InputData:
    """
    Класс для описания входных данных для энергетического расчета.
    """
    max_vel: float
    max_acc: float
    max_vel_working_move: float
    max_acc_working_acc: float
    acc_duration: float
    relative_duration: float
    max_stat_torque: float
    max_dynamic_torque: float

    def __post_init__(self):
        # Ensure all paths are strings
        assert isinstance(self.max_vel, float), "input_file must be a float"
        assert isinstance(self.max_acc, float), "input_file must be a float"
        assert isinstance(self.max_vel_working_move,
                          float), "input_file must be a float"
        assert isinstance(self.max_acc_working_acc,
                          float), "input_file must be a float"
        assert isinstance(self.acc_duration,
                          float), "input_file must be a float"
        assert isinstance(self.relative_duration,
                          float), "input_file must be a float"
        assert isinstance(self.max_stat_moment,
                          float), "output_file must be a float"
        assert isinstance(self.max_dynamic_moment,
                          float), "config_file must be a float"
