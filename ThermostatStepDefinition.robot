*** Settings ***
Library  Collections
Library  ${EXECDIR}/modbus_rtu.py  WITH NAME  MOD
Library  String
Library  OperatingSystem
Library  DateTime
Library  XML

***variables***

*** Keywords ***
Flag Status

    Log To Console  ${FLAG}

Set Differential temperature 2 degree Celsius  PNU 101

    MOD.write_holding_register   2   101   COM2  2
    log to console   Set Differential temperature 2 degree Celsius  PNU 101 -> Writing completed

Set Cut-out temperature 2 degree Celsius  PNU 100

    MOD.write_holding_register   2   100   COM2  2
    log to console   Set Cut-out temperature 2 degree Celsius  PNU 100 -> Writting completed

Check Cut-in temp = 4 (PNU 2612) And Cut-out temp = 2 (PNU 2613)

    ${RESULT} =  MOD.read_holding_registers  2    2612    1    COM2
    #log to console    ${RESULT}
    Should Be True    ${RESULT} == [4]
    log to console    Cut-in temp = 4 (PNU 2612)
    ${RESULT} =  MOD.read_holding_registers  2    2613    1    COM2
    #log to console    ${RESULT}
    Should Be True   ${RESULT} == [2]
    log to console  Cut-out temp = 2 (PNU 2613)

Set temperature on the Simulator_S1 (AI1) to 5 degree Celsius  PNU 40001

    MOD.write_holding_register   2   40001   COM2  5
    log to console   Set temperature on the Simulator_S1 (AI1) to 5 degree Celsius  PNU 40001 -> Writting completed

Set temperature on the Simulator_S2 (AI2) to 5 degree Celsius  PNU 40002

    MOD.write_holding_register   2   40002   COM2  5
    log to console   Set temperature on the Simulator_S2 (AI2) to 5 degree Celsius  PNU 40002 -> Writting completed

Set temperature on the Simulator_S3 (AI3) to 3 degree Celsius  PNU 40003

    MOD.write_holding_register   2   40003   COM2  3
    log to console   Set temperature on the Simulator_S3 (AI3) to 3 degree Celsius  PNU 40003 -> Writting completed

Set temperature on the Simulator_S4 (AI4) to 6 degree Celsius  PNU 40004

    MOD.write_holding_register   2   40004   COM2  6
    log to console   Set temperature on the Simulator_S4 (AI4) to 6 degree Celsius  PNU 40004 -> Writting completed

Set temperature on the Simulator_S5 (AI5) to 11 degree Celsius  PNU 40005

    MOD.write_holding_register   2   40005   COM2  11
    log to console   Set temperature on the Simulator_S5 (AI5) to 11 degree Celsius  PNU 40005 -> Writting completed

Wait 5 Seconds

    log to console  wait 5 seconds
    BuiltIn.Sleep  5

Check Compressor Status ON  PNU 2510
    ${RESULT} =  MOD.read_holding_registers  2    2510    1    COM2
    log to console    ${RESULT}
    Should Be True   ${RESULT} == [1]
    log to console    Compressor Status ON  PNU 2510

Set temperature on the Simulator_S4 to 0 degree Celsius  PNU 40004
    MOD.write_holding_register   2   40004   COM2  0
    log to console   Set temperature on the Simulator_S4 to 0 degree Celsius  PNU 40004 -> Writting completed

Check Compressor Status OFF  PNU 2510

    ${RESULT} =  MOD.read_holding_registers  2    2510    1    COM2
    log to console    ${RESULT}
    Should Be True    ${RESULT} == [0]
    log to console    Compressor Status OFF  PNU 2510