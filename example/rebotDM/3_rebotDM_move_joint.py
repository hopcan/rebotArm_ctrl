
'''
    调用控制函数会控制机械臂以期望速度转动到期望角度。
    Calling the control function will control the robotic arm to rotate at the desired speed to the desired angle
    
    ctrl c 结束程序后机械臂会缓慢返回零点，避免突然下坠
    After the program is terminated with  ctrl c, 
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
        while True:
            handle.move_to_joint_positions([0,0,0,0,0,0, -1])
            for motor_id in list(range(1,8)):
                print(f"motor {motor_id}")
                print(f"pos: {handle.motor_state[motor_id].pos:.3f} rad")
                print(f"vel: {handle.motor_state[motor_id].vel:.3f} rad/s")
                print(f"torque: {handle.motor_state[motor_id].torq:.3f} Nm\n")
            time.sleep(0.002)