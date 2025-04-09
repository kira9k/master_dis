from abc import ABC, abstractmethod
import math


class Motor(ABC):
    """Абстрактный класс для моторов."""

    def __init__(self, torque: float, power: float):
        self.torque = torque
        self.power = power

    @abstractmethod
    def validate_power(self):
        """
        Метод для расчета мощности.
        """
        pass

    @abstractmethod
    def validate_torque(self):
        """
        Метод для расчета момента.
        """
        pass


class DCBrushledMotor(Motor):
    """Класс для энергетического расчета приводов."""

    def __init__(self, max_vel, max_acc, max_vel_working_move,
                 max_acc_working_acc, acc_duration, relative_duration,
                 max_stat_moment, max_dynamic_moment):
        self.max_vel = max_vel
        self.max_acc = max_acc
        self.max_vel_working_move = max_vel_working_move
        self.max_acc_working_acc = max_acc_working_acc
        self.acc_duration = acc_duration
        self.relative_duration = relative_duration
        self.max_stat_moment = max_stat_moment
        self.max_dynamic_moment = max_dynamic_moment

    def validate_torque(self):
        """Метод для проверки требуемого момента"""
        #TODO добавить объявление переменных, хватит ли одного возвращаемого значения
        torque = self.moment_inertia_motor * self.gear_ratio * self.max_acc + (
            self.torque_max / self.gear_ratio)

        return torque <= self.torque_nom

    def validate_rational_speed(self):
        """Метод для проверки необходимой частоты вращения двигателя"""
        #TODO добавить объявление переменных, хватит ли одного возвращаемого значения
        max_rational_speed_motor = self.max_vel * self.gear_ratio

        return max_rational_speed_motor <= self.speed_motor_nom
