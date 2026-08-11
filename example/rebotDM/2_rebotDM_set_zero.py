from motorbridge import Controller

import os
import sys
# 获取项目根目录
# 1_rebotDM_connect.py -> rebotDM -> example -> rebotArm_ctrl (根目录)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)


from rebotArm_handle import reBotArm_handle
import time


if __name__ == "__main__":
    channel = "/dev/ttyACM0"  
    ctrl =Controller.from_dm_serial(channel, 921600)

    with reBotArm_handle(ctrl,"rebotDM") as handle:
        if handle.is_connected:
            print("Controller is connected and ready.")
            print("Motor Use Modes:", handle.use_mode)
            handle.set_zero_position()
        else:
            print("Controller failed to connect.")
        while True:
            time.sleep(0.002)