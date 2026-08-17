# rebotArm_ctrl

## 项目简介

`rebotArm_ctrl` 是一个用于控制 Rebot 机械臂的简单 Python 工程。它通过 `motorbridge` 控制器接口，加载 YAML 配置文件，并支持两种机械臂版本：

- `rebotDM`
- `rebotRS`

核心入口为 `rebotArm_handle.py`，提供连接、断开、归零、关节运动等操作。

## 目录结构

- `rebotArm_handle.py` - 机械臂控制封装类
- `config/rebotDM.yaml` - rebotDM 版本电机参数与关节配置
- `config/rebotRS.yaml` - rebotRS 版本电机参数与关节配置
- `example/` - 示例脚本目录
  - `example/rebotDM/` - rebotDM 使用示例
  - `example/rebotRS/` - rebotRS 使用示例

## 依赖

本项目依赖以下 Python 环境与包：

- Python 3.10+
- `motorbridge`
- `pyyaml`

请根据你的 Python 环境安装：

```bash
python3 -m pip install pyyaml motorbridge
```

> `motorbridge` 包名和安装方式可能依赖你的本地环境，请确认是否需要从源码安装或使用特定版本。

## 配置

项目使用 YAML 文件定义每个关节的参数：

- `MIT` 模式参数：`kp`, `kd`
- `POS_VEL` 模式参数：`vel_kp`, `vel_ki`, `pos_kp`, `pos_ki`, `vlim`
- `posmax` / `posmin`：关节运动范围
- `use_mode`：当前电机使用模式，可选 `MIT` 或 `POS_VEL`

两种版本的配置文件分别位于：

- `config/rebotDM.yaml`
- `config/rebotRS.yaml`

如果配置无效，程序会在启动时打印错误并停止连接。

## 使用方法

### 1. 运行示例脚本

在 `example/rebotDM/` 或 `example/rebotRS/` 目录下已有示例脚本。

```bash
cd /home/pan/rebotArm_ctrl/example/rebotDM
python3 1_rebotDM_connect.py
```

或者：

```bash
cd /home/pan/rebotArm_ctrl/example/rebotRS
python3 1_rebotRS_connect.py
```

### 2. 通过 `rebotArm_handle` 控制机械臂

`rebotArm_handle.py` 可直接作为模块使用：

```python
from motorbridge import Controller
from rebotArm_handle import reBotArm_handle

channel = "/dev/ttyACM0"  # rebotDM 示例
ctrl = Controller.from_dm_serial(channel, 921600)

with reBotArm_handle(ctrl, "rebotDM") as arm:
    if arm.is_connected:
        print("已连接")
        arm.move_to_joint_positions([0,0,0,0.5,0.5,0, -1])
```


对于 `rebotRS`，一般使用 CAN 总线：

```python
channel = "can0"
ctrl = Controller(channel)
with reBotArm_handle(ctrl, "rebotRS") as arm:
  ...
```

> 注意：`rebotDM` 与 `rebotRS` 的 socketcan 使用方式相同，若你使用 socketcan 版本，请参阅下面的 SocketCAN 设置。

### SocketCAN 设置（适用于 `rebotDM` 与 `rebotRS` 的 socketcan 版本）

如果你使用的是 socketcan 版本，需在使用前配置好主机上的 `can0` 接口。常用的设置步骤如下（需要 `sudo` 权限）：

```bash
ip -br link
sudo ip link set can0 down
sudo ip link set can0 type can bitrate 1000000
sudo ip link set can0 up
```

说明：
- `ip -br link`：简洁地查看当前网络接口状态，确认是否存在 `can0`。
- `bitrate 1000000`：示例比特率，需与硬件设备的实际波特率一致，可根据需要调整。
- 如果你在虚拟机或没有物理 CAN 设备上测试，可以使用 `vcan`（虚拟 CAN）替代真实接口。

运行上述命令后，使用 `ip -br link` 或 `ifconfig can0` 检查 `can0` 是否为 `UP` 状态，然后再运行示例脚本。


## 主要功能

- `connect()`：加载配置、注册电机、检查 ID、使能电机并切换工作模式
- `disconnect()`：返回零点、关闭电机并断开总线
- `set_zero_position()`：设置所有电机的零点位置
- `move_to_joint_positions(positions, velocity=None, torgue=None)`：运动到指定关节位置
- `return_zero_position()`：平稳返回预设零点姿态

## 注意事项

- 启动前确保机械臂电源已接通
- `rebotDM` 示例默认串口为 `/dev/ttyACM0`
- `rebotRS` 示例默认 CAN 接口为 `can0`
 - `rebotRS` 示例默认 CAN 接口为 `can0`
 - 注意：`rebotDM` 与 `rebotRS` 的 socketcan 版本默认使用 `can0` 作为 CAN 接口（可按需修改）
- 运行示例脚本时会将项目根目录加入 `sys.path`，无需额外安装包
- 若出现 PID / 电机参数错误，请检查对应 YAML 文件中的 `MIT` 和 `POS_VEL` 配置

## 贡献

如需扩展功能，可在 `rebotArm_handle.py` 中增加运动指令、状态读取、PID 参数更新等逻辑。