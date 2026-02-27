"""
通过WiFi ADB连接手机，完成测试准备工作
"""
import subprocess
import re
import time


from utility import *

ADB_PORT = 2222
APPIUM_PORT_INITIAL = 4723
SYSTEM_PORT_INITIAL = 8201

# 获取已经连接的ADB设备
def get_adb_devices() -> list[str]:
    results = subprocess.run(['adb','devices'],capture_output=True,text=True)
    # print(results.stdout)

    s = results.stdout.split('attached')[1] # 字符串分段
    udids = re.findall(r'(\S+)\sdevice',s)
    print_diy(f'当前连接设备：{udids}')

    return udids

# 添加手机端ADB端口
def set_adb_port(udid, port):
    results = subprocess.run(['adb', '-s', udid, 'tcpip', f'{port}'], capture_output=True, text=True)
    print(results.stdout)

# 获取WiFi接口IP地址
def get_wlan0_ip(udid, cmd:str) -> str:
    results = subprocess.run(['adb', '-s', udid, 'shell', cmd], capture_output=True, text=True)
    print(results.stdout)

    if cmd == 'ifconfig':
        ip = re.search(r'inet addr:(.*?) ', results.stdout).group(1)
    if cmd == 'ip addr':
        ip = re.search( r'wlan0.*?inet (\d+\.\d+\.\d+.\d+)', results.stdout, re.S).group(1)
    else:
        raise ValueError('请输入正确的命令')

    print_diy(f'{udid}设备的IP地址：{ip}')
    return ip

# 通过WiFi ADB连接手机
def connect_phone_by_wifi_adb(ip):
    results = subprocess.run(['adb', 'connect', f'{ip}:{ADB_PORT}'], capture_output=True, text=True)
    print(results.stdout)

# 获取手机名称
def get_brand_model_name(udid) -> str:
    results = subprocess.run(['adb',
                              '-s',
                              udid,
                              'shell',
                              f'getprop'], capture_output=True, text=True)
    # print(results.stdout)

    brand = re.search(r'\[ro.product.brand\]: \[(.*?)\]',results.stdout).group(1)
    name = re.search(r'\[ro.product.name\]: \[(.*?)\]',results.stdout).group(1)
    print_diy(f'{udid}设备的名称：{brand}_{name}')

    return f'{brand}_{name}'

if __name__ == '__main__':
    '''
    # 获取当前连接设备
    udids_connect = get_adb_devices()

    for udid in udids_connect:
        # 如果是WiFi的UDID，什么也不做
        if bool(re.search(r'\d+\.\d+\.\d+\.\d+', udid)):
            pass
        # 如果是设备的UDID，通过WiFi使用ADB连接设备
        else:
            # 添加手机端ADB端口
            set_adb_port(udid, ADB_PORT)
            time.sleep(3)

            # 获取手机WiFi IP
            ip = get_wlan0_ip(udid, 'ip addr')

            # 通过WiFi ADB连接手机
            connect_phone_by_wifi_adb(ip)

            # 获取yaml已存储设备
            devices_yaml = read_yaml('data/devices.yaml')
            print_diy(f'yaml文件当前存储内容：{devices_yaml}')

            # yaml内容为空，将设备信息写入yaml
            if devices_yaml is None:
                # 获取手机名称
                name = get_brand_model_name(udid)

                device = {'name': name,
                          'udid': udid,
                          'udid_wifi': f'{ip}:{ADB_PORT}',
                          'appium_port': 4723,
                          'system_port': 8201}

                # 写入yaml
                append_yaml([device], 'data/devices.yaml')
            else:
                # 获取yaml里存储的设备信息
                udids_yaml = [dev_yaml['udid'] for dev_yaml in devices_yaml]
                udids_wifi_yaml = [dev_yaml['udid_wifi'] for dev_yaml in devices_yaml]
                appium_port_last = devices_yaml[-1]['appium_port']
                system_port_last = devices_yaml[-1]['system_port']

                # 如果设备的udid已存储，更新IP地址
                if udid in udids_yaml:
                    for dev_yaml in devices_yaml:
                        if dev_yaml['udid'] == udid:
                            dev_yaml['udid_wifi'] = f'{ip}:{ADB_PORT}'
                            write_yaml(devices_yaml,'data/devices.yaml')
                # 设备的UDID未存储在yaml里，将设备信息存储到yaml里
                else:
                    # 获取手机名称
                    name = get_brand_model_name(udid)

                    device = {'name':name,
                              'udid':udid,
                              'udid_wifi':f'{ip}:{ADB_PORT}',
                              'appium_port':appium_port_last + 1,
                              'system_port':system_port_last + 1}

                    # 写入yaml
                    append_yaml([device], 'data/devices.yaml')
    '''

    # 获取当前连接设备
    udids_connect = get_adb_devices()
    count = 0
    device_list = []

    for udid in udids_connect:
        # 如果是WiFi的UDID，什么也不做
        if bool(re.search(r'\d+\.\d+\.\d+\.\d+', udid)):
            pass
        # 如果是设备的UDID，通过WiFi使用ADB连接设备
        else:
            # 添加手机端ADB端口
            set_adb_port(udid, ADB_PORT)
            time.sleep(3)

            # 获取手机WiFi IP
            ip = get_wlan0_ip(udid, 'ip addr')

            # 通过WiFi ADB连接手机
            connect_phone_by_wifi_adb(ip)

            # 获取手机名称
            name = get_brand_model_name(udid)

            device = {'name': name,
                      'udid': udid,
                      'udid_wifi': f'{ip}:{ADB_PORT}',
                      'appium_port': APPIUM_PORT_INITIAL + count,
                      'system_port': SYSTEM_PORT_INITIAL + count}

            device_list.append(device)

            count += 1
    write_yaml(device_list,'data/devices.yaml')