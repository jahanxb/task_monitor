import wmi
import json
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

sys_info = dict(
    Manufacturer=str(my_system.Manufacturer),
    Model=str(my_system.Model),
    Name=str(my_system.Name),
    NumberofProcessors=str(my_system.NumberOfProcessors),
    SystemType=str(my_system.SystemType),
    SystemFamily=str(my_system.SystemFamily)
)


print(sys_info)
with open('D://PycharmProjects//monitor_me//sys_info.json', 'w') as file:
    json.dump(sys_info, file)