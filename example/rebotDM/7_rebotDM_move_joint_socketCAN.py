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
    channel = "can0"  
    ctrl =Controller(channel)

    with reBotArm_handle(ctrl,"rebotDM") as handle:
        if handle.is_connected:
            print("Controller is connected and ready.")
            print("Motor Use Modes:", handle.use_mode)
        else:
            print("Controller failed to connect.")
        while True:
            handle.move_to_joint_positions([0,0,0,0,0,0, -1])
            for motor_id in list(range(1,8)):
                print(f"motor {motor_id}")
                print(f"pos: {handle.motor_state[motor_id].pos:.3f} rad")
                print(f"vel: {handle.motor_state[motor_id].vel:.3f} rad/s")
                print(f"torque: {handle.motor_state[motor_id].torq:.3f} Nm\n")
            time.sleep(0.002)