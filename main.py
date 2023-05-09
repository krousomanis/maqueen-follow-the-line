def line_patrol():
    if DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_L1) == 0 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_M) == 1 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_R1) == 0:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_ALL_MOTOR, MyEnumDir.E_FORWARD, 100)
    if DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_L1) == 1 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_M) == 1 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_R1) == 0:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_FORWARD, 40)
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_FORWARD, 100)
    if DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_L1) == 1 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_M) == 0 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_R1) == 0:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_FORWARD, 0)
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_FORWARD, 100)
    if DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_L1) == 0 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_M) == 1 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_R1) == 1:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_FORWARD, 100)
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_FORWARD, 40)
    if DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_L1) == 0 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_M) == 0 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_R1) == 1:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_FORWARD, 100)
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_FORWARD, 0)


DFRobotMaqueenPlusV2.init()

def on_forever():
    line_patrol()
    if DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_L2) == 1:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_BACKWARD, 100)
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_FORWARD, 100)
        line_patrol()
    if DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_L2) == 0 and DFRobotMaqueenPlusV2.read_line_sensor_state(MyEnumLineSensor.E_R2) == 1:
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_LEFT_MOTOR, MyEnumDir.E_FORWARD, 100)
        DFRobotMaqueenPlusV2.control_motor(MyEnumMotor.E_RIGHT_MOTOR, MyEnumDir.E_BACKWARD, 100)
        line_patrol()  
         


basic.forever(on_forever)
