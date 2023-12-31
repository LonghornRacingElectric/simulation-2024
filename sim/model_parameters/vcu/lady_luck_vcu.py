from sim.model_parameters.parameters.toggle_parameter import ToggleParameter
from sim.model_parameters.vcu.vcu import VehicleControlUnit


class LadyLuckVcu(VehicleControlUnit):
    def __init__(self):
        super().__init__()
        self._model_name = "Lady Luck VCU"

        self.traction_control_enabled = ToggleParameter(False)
        self.anti_lock_brakes_enabled = ToggleParameter(False)
