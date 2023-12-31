from sim.model_parameters.cars.car import Car
from sim.system_models.vectors.state_dot_vector import StateDotVector
from sim.system_models.vectors.state_vector import StateVector


class TimeIntegrator:
    """
    Uses Euler's method to do an integral of vehicle's state over time.
    """

    def __init__(self, time_step: float, car: Car):
        self.time_step = time_step
        self.car = car

    def eval(self, state: StateVector, state_dot: StateDotVector) -> StateVector:
        state.hv_battery_charge -= state_dot.hv_battery_current * self.time_step
        state.lv_battery_charge -= state_dot.lv_battery_current * self.time_step
        # state.motor_rpm needs motor torque as well as rolling resistance from tire
        state.hv_battery_temperature += (state_dot.hv_battery_net_heat
                                         * self.car.hv_battery_thermal_resistance * self.time_step)
        state.inverter_temperature += (state_dot.inverter_net_heat
                                       * self.car.inverter_thermal_resistance * self.time_step)
        state.motor_temperature += (state_dot.motor_net_heat
                                    * self.car.hv_battery_thermal_resistance * self.time_step)
        state.coolant_temperature += (state_dot.coolant_net_heat
                                      * self.car.hv_battery_thermal_resistance * self.time_step)
        # state.wheelspeed_fl, fr, bl, br based on applied torque and
        return state
