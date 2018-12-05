from typing import List


class CallingPointMirror(object):
    """
    This class is a manually maintained direct mirror of the CallingPoints enum class in include/ems_manager.h.
    Having this here allows derived EMS classes to refer to the calling points by name rather than magic integers.
    """
    AFTER_SIZING = 0
    HVAC_TIME_STEP_LOOP = 1


class EMSInterface(object):
    """
    The EMSInterface class is the base class for all PythonEMS classes.
    Derived classes should inherit from this class and override the functions which include a NotImplementedError
    here in the base class definition.
    """

    def __init__(self):
        """
        Constructor for the EMS interface base class.  Does not take any arguments, just initializes some member vars.
        """
        super().__init__()
        self.my_sensed_data = {}

    def ems_main(self) -> List[float]:
        """
        Performs the main EMS action, looking up sensed data as needed, and returning a list of floats corresponding
        to actuators in the calling program.  This function can call other functions as needed, as well as importing
        standard lib packages to use in the calculations.

        The return from this function is a list of floats, ordered according to the order of actuators listed in the
        get_actuator_list function.

        **Derived classes must override this function!**

        :return: A list of floating point values representing the actuated value of each assigned actuator.
        """
        raise NotImplementedError(
            "Encountered EMSInterface::ems_main base function -- override this in your EMS class"
        )

    def get_calling_point(self) -> int:
        """
        This function returns an integer calling point to indicate when this EMS program is to be executed.
        The list of valid integers is in the CallingPoint enum class, which is in include/ems_manager.h.

        **Derived classes must override this function!**

        :return: An integer identifier for the calling point where this EMS class should be executed.

        TODO: Could this be a list?
        """
        raise NotImplementedError(
            "Encountered EMSInterface::get_calling_point base function -- override this in your EMS class"
        )

    def get_sensed_data_list(self) -> List[str]:
        """
        Returns a list of sensor "IDs".
        At the moment this is a hardwired list of strings that match some expected strings in the C++ side.
        Ultimately this should return some form of ID that might be "ComponentType:ComponentName:SensedValue" or similar

        Example:
            return ["zone_one_temperature", "zone_two_temperature"]
        This would result in the member variable self.my_sensed_data dictionary having two keys:
        ("zone_one_temperature", "zone_two_temperature"), each of which having a value that is a floating point
        variable that is updated by E+ right before the call to this EMS function

        Tip: Since the string keys are going to be returned here, and then likely used as lookups in other functions
        in this class, it is recommended to create constants of each to avoid spelling typos and make the code cleaner.

        **Derived classes must override this function!  If your EMS does not need sensors, return an empty list**

        :return: A list of strings, each of which corresponding to a meaningful sensor in the calling program
        """
        raise NotImplementedError(
            "Encountered EMSInterface::get_sensed_data_list base function -- override this in your EMS class"
        )

    def get_actuator_list(self) -> List[str]:
        """
        Returns a list of actuator "IDs".
        At the moment this is a hardwired list of strings that match some expected strings in the C++ side.
        Ultimately this should return some form of ID that might be "ComponentType:ComponentName:ActuatorName"-ish.

        Example:
            return ["zoneOneDamperPosition", "zoneTwoDamperPosition"]
        This would result in this EMS program being responsible for actuating those values through the return values
        from the ems_main function.

        **Derived classes must override this function!  If your EMS does not need actuators, then what does it do!?**

        :return: A list of strings, each of which corresponding to a meaningful actuator in the calling program
        """
        raise NotImplementedError(
            "Encountered EMSInterface::get_actuator_list base function -- override this in your EMS class"
        )

    def update_sensed_datum(self, sensor_id: str, value: float) -> None:
        """
        This function updates the dictionary class member variable storing the sensor data (self.my_sensed_data) with
        a new value from the calling program.

        **Derived classes SHOULD NOT override this function unless there is a super reason to do so.  Tip: there's not**

        :param sensor_id: A string identifier which is meaningful to the calling program and stored here.
        :param value: The sensed value to be seen by the ems main function when it is called
        """
        self.my_sensed_data[sensor_id] = value
