
'''
    上电会自动检测电机是否全部在线、电机id是否有效、参数配置表是否配置
    Upon power-on, the system will automatically check whether all motors are online, 
    whether the motor IDs are valid, and whether the parameter configuration table is properly set up
    
    ctrl c 结束程序后机械臂会缓慢返回零点，避免突然下坠
    After the program is terminated with ctrl c, 
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
        else:
            print("Controller failed to connect.")
        while True:
            time.sleep(0.002)