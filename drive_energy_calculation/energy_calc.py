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

    def calc_max_torque(self,
                        max_dynamic_torque,
                        max_stat_torque,
                        gear_ratio=1):
        """Функция для расчета максимального момента. Если КПД еще неизвестен, считаем равным 1"""
        max_torque = (max_dynamic_torque + max_stat_torque) / gear_ratio
        return max_torque

    def calc_max_power(
        self,
        max_dynamic_torque,
        stat_torque,
        max_vel,
        gear_ratio=1,
    ):
        """Функция для расчета требуемой максимальной мощности"""
        max_torque = self.calc_max_torque(
            max_dynamic_torque,
            stat_torque,
            gear_ratio=gear_ratio,
        )
        max_power = max_torque * max_vel
        return max_power

    def gear_ratio_opt_calc(self, max_power, max_vel, max_acc,
                            moment_of_inertia):
        """
        Функция для расчета оптимального передаточного отношения редуктора.
        """
        #TODO подумать как передавать значения
        gear_ratio_opt = math.sqrt(
            max_power / (self.moment_of_inertia * self.max_acc * self.max_vel))

        return gear_ratio_opt

    def calc_torque_motor(self):
        """Функция для расчета требуемого момента"""
        torque_motor = self.moment_inertia_motor * self.gear_ratio * self.max_acc + (
            self.torque_max / self.gear_ratio)
        return torque_motor

    def validate_torque(self):
        """Метод для проверки требуемого момента"""
        #TODO добавить объявление переменных, хватит ли одного возвращаемого значения
        torque_motor = self.calc_torque_motor()
        return torque_motor <= self.torque_nom

    def calc_max_rational_speed_motor(self):
        """Функция для расчета необходимой частоты вращения двигателя"""
        max_rational_speed_motor = self.max_vel * self.gear_ratio

    def validate_rational_speed(self):
        """Метод для проверки необходимой частоты вращения двигателя"""
        #TODO добавить объявление переменных, хватит ли одного возвращаемого значения
        max_rational_speed_motor = self.calc_max_rational_speed_motor()
        return max_rational_speed_motor < self.speed_motor_nom

    def sum_moment_inertia(self):
        """Функция для расчета суммарного момента инерции"""
        equivalent_moment_inertia_motor = self.equivalent_moment_inertia / (
            self.gear_ratio**2 * self.efficiency_gearbox)
        sum_moment_inertia = equivalent_moment_inertia_motor + self.moment_inertia_motor
        return sum_moment_inertia

    def acc_motor(self):
        """Функция для расчета ускорения двигателя"""
        acc_motor = self.max_acc * self.gear_ratio
        return acc_motor
