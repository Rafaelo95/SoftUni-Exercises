from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        hardware_found = False
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_found = True
                try:
                    hardware.install(ExpressSoftware(name, capacity_consumption, memory_consumption))
                except Exception:
                    return "Software cannot be installed"
                System._software.append(ExpressSoftware(name, capacity_consumption, memory_consumption))

        if not hardware_found:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        hardware_found = False
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                hardware_found = True
                try:
                    hardware.install(LightSoftware(name, capacity_consumption, memory_consumption))
                except Exception:
                    return "Software cannot be installed"
                System._software.append(LightSoftware(name, capacity_consumption, memory_consumption))
                break

        if not hardware_found:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        hardware_found = False
        software_found = False
        hardware = None
        software = None

        for h in System._hardware:
            if h.name == hardware_name:
                hardware_found = True
                hardware = h
                break

        for s in System._software:
            if s.name == software_name:
                software_found = True
                software = s
                break

        if hardware_found and software_found:
            hardware.uninstall(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f'''System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)} 
Total Operational Memory: {sum([s.memory_consumption for s in System._software])} / {sum([h.memory for h in System._hardware])}
Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} / {sum([h.capacity for h in System._hardware])}'''

    @staticmethod
    def system_split():
        pass


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)

System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("SSD", "Linux", 50, 100)

System.release_software_component("SSD", "Linux")


