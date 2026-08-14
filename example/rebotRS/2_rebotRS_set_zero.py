
'''
    调用设置零点函数会将机械臂当前电机的角度设置成零位。
    calling the zero setting function will set the angle of the current motor of the robotic arm to zero.
    
    ctrl c 结束程序后机械臂会缓慢返回零点，避免突然下坠
    After the program is terminated with  ctrl c, 
    the robotic arm will slowly return to the zero point to prevent sudden drops
'''
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

    with reBotArm_handle(ctrl,"rebotRS") as handle:
        if handle.is_connected:
            print("Controller is connected and ready.")
            print("Motor Use Modes:", handle.use_mode)
            handle.set_zero_position()
        else:
            print("Controller failed to connect.")
        while True:
            time.sleep(0.002)