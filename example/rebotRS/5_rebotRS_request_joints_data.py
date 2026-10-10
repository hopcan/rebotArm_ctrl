
'''
    主动调用机械臂断开连接，会先自动归零，然后才会失能
    Proactively calling the robotic arm to disconnect will automatically reset to zero before it becomes disabled

    ctrl c 结束程序后机械臂会缓慢返回零点，避免突然下坠
    After the program is terminated with  ctrl c, 
    the robotic arm will slowly return to the zero point to prevent sudden drops
'''
from motorbridge import Controller
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
config_path = os.path.join(project_root, "config", "rebotRS_get_data.yaml") 

from rebotArm_handle import reBotArm_handle
import time

joints_pos = [0]*7

if __name__ == "__main__":
    channel = "can0"  
    ctrl =Controller(channel)
    
    with reBotArm_handle(ctrl,"rebotRS",config_path) as handle:
        if handle.is_connected:
            print("Controller is connected and ready.")
            print("Motor Use Modes:", handle.use_mode)
        else:
            print("Controller failed to connect.")
        while True:
            joints_pos = handle.get_joints_state()
            neg_pos = [-pos for pos in joints_pos]
            handle.move_to_joint_positions(neg_pos)
            print(joints_pos)
            time.sleep(0.002)