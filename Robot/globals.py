from multiprocessing import Manager,Lock


def initilizeGlobals():
    manager = Manager()

    # Data shared between communication process and main process
    global sharedData
    sharedData = manager.dict()
    sharedData["DataToSend"] = {"CameraFrames":[]}
    sharedData["DataRecieved"] = {"commands":[]}
    sharedData["NewDataRecieved"] = False
    sharedData["Ping"] = .1
    sharedData["LastConnectTime"] = 0

    global sharedMotorSpeedData
    sharedMotorSpeedData = manager.dict()
    sharedMotorSpeedData["RRSpeed"] = 0
    sharedMotorSpeedData["RLSpeed"] = 0
    sharedMotorSpeedData["FRSpeed"] = 0
    sharedMotorSpeedData["FLSpeed"] = 0

    # import motor
    # global motors
    # motors = motor.motors()

    global ThreadLock
    ThreadLock = Lock()