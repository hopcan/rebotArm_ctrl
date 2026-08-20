
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
        else:
            print("Controller failed to connect.")
        handle.ctrl.disable_all()
        while True:
            print(handle.get_joints_state())
            time.sleep(0.002)
