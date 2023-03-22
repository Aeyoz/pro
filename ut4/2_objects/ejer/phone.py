CONSUMPTION_CHART = {"POWER_ON" : 5, "POWER_OFF" : 2.5, "APP_POWER" : 1}

class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int, apps: list[str] = [], status: bool = False, battery_level: float = 100):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = apps
        self.status = status
        self.battery = battery_level

    def recharge(self, recharge_battery_level):
        for _ in range((recharge_battery_level + 1) * 2):
            if self.battery != 100.0:
                self.battery += 0.5

    def take_of_battery_unit(self, battery_level=CONSUMPTION_CHART["APP_POWER"]):
        self.battery -= battery_level

    def power_on(self, battery_level = CONSUMPTION_CHART["POWER_ON"]):
        if self.status:
            return f"Phone already on"
        self.status = True
        self.take_of_battery_unit(battery_level)

    def power_off(self, battery_level = CONSUMPTION_CHART["POWER_OFF"]):
        if not self.status:
            return f"Phone already off"
        self.status = False
        self.take_of_battery_unit(battery_level)

    def install(self, *apps):
        error_msgs = []
        if self.status == 0:
            return f"The device has to be on"
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)
            else:
                error_msgs.append(f"Unable to install {app}, already installed")
            self.take_of_battery_unit()
        return error_msgs

    def uninstall(self, *apps):
        error_msgs = []
        if self.status == 0:
            return f"The device has to be on"
        for app in apps:
            if app in self.apps:
                index = self.apps.index(app)
                self.apps.pop(index)
            else:
                error_msgs.append(f"Unable to install {app}, already installed")
            self.take_of_battery_unit()
        return error_msgs


samsung = MobilePhone("Samsung", 7.5, 6, ["whatsapp", "reddit", "discord"], status=True)

samsung.install("aliexpress", "amazon", "duolingo")
samsung.install("zzzzz", "sssss", "duolingo")
samsung.uninstall("zzzzz", "sssss", "duolingo", "asdasdw")
samsung.power_on()
samsung.power_off()

print(samsung.battery)