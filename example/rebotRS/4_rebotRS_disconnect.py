
'''
    主动调用机械臂断开连接，会先自动归零，然后才会失能
    Proactively calling the robotic arm to disconnect will automatically reset to zero before it becomes disabled

    ctrl c 结束程序后机械臂会缓慢返回零点，避免突然下坠
    After the program is terminated with  ctrl c, 
    the robotic arm will slowly return to the zero point to prevent sudden drops
'''
# SocketCAN 使用提示：如果你使用 `can0`（socketcan），请在运行脚本前初始化接口：
# ip -br link
# sudo ip link set can0 down
# sudo ip link set can0 type can bitrate 1000000
# sudo ip link set can0 up
# 详情请参阅项目根目录下的 README.md
from motorbridge import Controller
import os
import sys
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