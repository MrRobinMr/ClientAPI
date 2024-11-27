import os
import subprocess
import socket
import GPUtil
from cpuinfo import get_cpu_info
import psutil

#info about computer
def Info():
    computer_info = {
        "user": os.getlogin(),
        "host_name": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname())
    }
    return computer_info

#info about gpus
def Gpu_Info():
    gpus = GPUtil.getGPUs()
    gpu_info = {
        "Count" : gpus.__len__()
    }
    for gpu in gpus:
        gpu_info |= {
            "ID" : gpu.id,
            "Name" : gpu.name,
            "Vram_Totsl": gpu.memoryTotal,
        }
    return gpu_info

#info about cpu
def Cpu_Info():
    cpu = get_cpu_info()
    cpu_info = {
        "Name" : cpu['brand_raw'],
        "Arch" : cpu['arch'],
        "Cores" : psutil.cpu_count(False),
        "Virtual_Cores" : psutil.cpu_count(True),
        "Maxhz" : cpu.get('hz_advertised_friendly', 'Brak danych')
    }
    return cpu_info