# coding = utf-8
# @author:yingzhudashu

from pymavlink import mavutil

f = open("mavlink_0.txt", "w", encoding='UTF-8')

master = mavutil.mavlink_connection('com13')  # port 是端口号
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_system))

while True:
    try:
        msg = master.recv_match(type=['GLOBAL_POSITION_INT', 'RAW_IMU', 'GPS_RAW_INT'], blocking=True)
        if not msg:
            raise ValueError()
        print(msg.to_dict())
        f.write(str(msg.to_dict().keys()))
        f.write('\n')
    except KeyboardInterrupt:
        print('Key bordInterrupt! exit')
        break