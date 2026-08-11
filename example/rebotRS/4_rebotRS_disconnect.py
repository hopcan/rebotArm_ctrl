from motorbridge import Controller

#主动调用机械臂断开连接，会先自动归零，然后才会失能

import os
import sys
# 获取项目根目录
# 1_rebotDM_connect.py -> rebotDM -> example -> rebotArm_ctrl (根目录)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)


from rebotArm_handle import reBotArm_handle
import time


if __name__ == "__main__":
    channel = "can0"  
    ctrl =Controller(channel)

    with reBotArm_handle(ctrl,"rebotRS") as handle:
        if handle.is_connected:
            print("Controller is connected and ready.")
            print("Motor Use Modes:", handle.use_mode)
        else:
            print("Controller failed to connect.")
        while True:
            time.sleep(2)
            handle.disconnect()