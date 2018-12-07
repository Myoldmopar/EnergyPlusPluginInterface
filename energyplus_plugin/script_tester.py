#!/usr/bin/env python3

"""
This file is a standalone PyEMS script tester.
It is called using a single argument, the path to a PyEMS file
"""

import inspect
import os
import sys
from importlib import util as import_util


class PyEMSTesting(object):

    @staticmethod
    def py_ems_file_tester(file_path):
        modules = []

        if os.path.exists(file_path):
            print("   OK : File path exists at: " + file_path)
        else:
            print("ERROR : File path does not exist!  Path: " + file_path)
            return 1

        if file_path.endswith('.py'):
            print("   OK : File ends with .py")
        else:
            print("ERROR : File path does NOT end with .py")
            return 1

        module_spec = import_util.spec_from_file_location('py_ems_module', file_path)
        this_module = import_util.module_from_spec(module_spec)
        try:
            modules.append(this_module)
            module_spec.loader.exec_module(this_module)
            print("   OK : Python import process completed successfully!")
        except ImportError as ie:
            # this error generally means they have a bad py_ems class or something
            print("ERROR : Import error occurred on py_ems file %s: %s" % (file_path, str(ie)))
            return 1
        except SyntaxError as se:
            # syntax errors are, well, syntax errors in the Python code itself
            print("ERROR : Syntax error occurred on py_ems file %s, line %s: %s" % (file_path, se.lineno, se.msg))
            return 1
        except Exception as e:
            # there's always the potential of some other unforeseen thing going on when a py_ems is executed
            print("ERROR : Unexpected error occurred trying to import py_ems: %s: %a" % file_path, str(e))
            return 1

        successful_classes = []
        for this_module in modules:
            class_members = inspect.getmembers(this_module, inspect.isclass)
            for this_class in class_members:
                this_class_name, this_class_type = this_class
                print(" INFO : Encountered class: \"" + this_class_name + "\", testing now...")
                # so right here, we could check is_subclass, but this would also match the base class, which
                # is imported in each PyEMS class.  No need to do that.  For now I'm going to check the direct
                # parent class of this class to verify we only get direct descendants.  We can evaluate this later.
                # if is_subclass(this_class_type, EMSInterface):
                num_inheritance = len(this_class_type.__bases__)
                base_class_name = this_class_type.__bases__[0].__name__
                py_ems_base_class_name = 'EMSInterface'
                if num_inheritance == 1 and py_ems_base_class_name in base_class_name:
                    print("   OK : Basic inheritance checks out OK for class: " + this_class_name)

                    try:
                        py_ems_instance = this_class_type()
                        print("   OK : Instantiation of derived class works")
                    except Exception as e:
                        print("ERROR : Instantiation of derived class malfunctioning; reason: " + str(e))
                        return 1

                    try:
                        this_calling_point = py_ems_instance.get_calling_point()
                        print("   OK : Overridden get_calling_point() function execution works")
                    except Exception as e:
                        print("ERROR : get_calling_point() function not overridden, or is broken; reason: " + str(e))
                        return 1

                    if isinstance(this_calling_point, int):
                        print("   OK : Calling point comes back as an integer, this is the expected condition")
                    else:
                        print("ERROR : Bad get_calling_point return; must be int from EMSInterface.CallingPointsMirror")
                        return 1

                    try:
                        sensors = py_ems_instance.get_sensed_data_list()
                        print("   OK : Overridden get_sensed_data_list() function execution works")
                    except Exception as e:
                        print("ERROR : get_sensed_data_list() function not overridden, or is broken; reason: " + str(e))
                        return 1

                    if isinstance(sensors, list):
                        print("   OK : get_sensed_data_list returns a list, this is the expected condition")
                    else:
                        print("ERROR : Bad return from get_sensed_data_list(); it must return a list of strings!")
                        return 1

                    bad_sensor = False
                    for i, val in enumerate(sensors):
                        if isinstance(val, str):
                            print("   OK : argument #%s from get_sensed_data_list is a string" % i)
                        else:
                            bad_sensor = True
                            print("ERROR : argument #%s from get_sensed_data_list must be a string!" % i)
                    if bad_sensor:
                        return 1

                    try:
                        actuators = py_ems_instance.get_actuator_list()
                        print("   OK : Overridden get_actuator_list() function execution works")
                    except Exception as e:
                        print(
                            "ERROR : get_actuator_list() function not overridden, or is broken; reason: " + str(e))
                        return 1

                    if isinstance(actuators, list):
                        print("   OK : get_actuator_list returns a list, this is the expected condition")
                    else:
                        print("ERROR : Bad return from get_actuator_list(); it must return a list of strings!")
                        return 1

                    bad_actuator = False
                    for i, val in enumerate(actuators):
                        if isinstance(val, str):
                            print("   OK : argument #%s from get_actuator_list is a string" % i)
                        else:
                            bad_actuator = True
                            print("ERROR : argument #%s from get_actuator_list must be a string!" % i)
                    if bad_actuator:
                        return 1

                    # now we need to instantiate the sensor dictionary by calling the base class method for each sensor
                    try:
                        for sensor in sensors:
                            py_ems_instance.update_sensed_datum(sensor, 0.0)
                    except Exception as e:
                        print("ERROR : Could not call update_sensed_data - this method should not be overridden!")
                        print("       Error message for diagnostics: " + str(e))

                    try:
                        py_ems_instance.ems_main()
                        print("   OK : Overridden ems_main() function execution works")
                    except Exception as e:
                        print("ERROR : ems_main() function not overridden, or is broken; reason: " + str(e))
                        return 1

                    successful_classes.append(this_class_name)

                else:
                    print(" INFO : Inheritance does not check out, will continue with other classes in this file")
                    continue

        if len(successful_classes) > 0:
            print("   OK : Found %s successful py_ems imports:" % len(successful_classes))
            for c in successful_classes:
                print("   OK :   " + c)
            return 0
        else:
            print("ERROR : Did not find ANY successful py_ems imports in this file!")
            return 1


def main():
    if len(sys.argv) != 2:
        print("Bad call to tester, give one command line argument, the full path to a py_ems file")
        sys.exit(2)
    else:
        arg_file_path = sys.argv[1]
        response = PyEMSTesting.py_ems_file_tester(arg_file_path)
        sys.exit(response)


if __name__ == "__main__":
    main()

