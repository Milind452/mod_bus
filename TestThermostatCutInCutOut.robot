*** Settings ***
Resource    ./ThermostatStepDefinition.robot
Metadata    Feature Test Thermostat Cut in/Cut-out
Default Tags  POC Test Simulator
Test Setup  Set Global Variable  ${FLAG}

*** Variables ***
${FLAG}  0

*** Test Cases ***
Simulator test thermostat Cut in/Cut-out
    Given Flag Status
    # Given Set Differential temperature 2 degree Celsius  PNU 101
    # And Set Cut-out temperature 2 degree Celsius  PNU 100
    # When Check Cut-in temp = 4 (PNU 2612) And Cut-out temp = 2 (PNU 2613)
    # And Set temperature on the Simulator_S1 (AI1) to 5 degree Celsius  PNU 40001
    # And Set temperature on the Simulator_S2 (AI2) to 5 degree Celsius  PNU 40002
    # And Set temperature on the Simulator_S3 (AI3) to 3 degree Celsius  PNU 40003
    # And Set temperature on the Simulator_S4 (AI4) to 6 degree Celsius  PNU 40004
    # And Set temperature on the Simulator_S5 (AI5) to 11 degree Celsius  PNU 40005
    # And Wait 5 Seconds
    # Then Check Compressor Status ON  PNU 2510
    # #Read DO3 Relay is ON (24V in DMM) (Applicable only for hardware)
    # And Set temperature on the Simulator_S4 to 0 degree Celsius  PNU 40004
    # And Wait 5 Seconds
    # And Check Compressor Status OFF  PNU 2510
    # #Read DO3 Relay is OFF (0V in DMM) (Applicable only for hardware)
