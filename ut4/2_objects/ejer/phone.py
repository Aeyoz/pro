CONSUMPTION_CHART = {"POWER_ON" : 5, "POWER_OFF" : 2.5, "APP_POWER" : 1}
FULL = 100
EMPTY = 0
class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int\
        , apps: list[str] = ["whatsapp", "instagram", "chrome"], status: bool =\
        True, battery_level: float = 100):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = apps
        self.status = status
        self.battery = battery_level

    def recharge(self, recharge_battery_level) -> None:
        for i in range(recharge_battery_level + 1):
            if i == recharge_battery_level or self.battery == FULL:
                break
            self.battery += 0.5 if 100 - self.battery < 1 else 1

    def battery_drainage(self, operation_type, dreinage_chart = CONSUMPTION_CHART) -> tuple:
        battery_taken = dreinage_chart[operation_type.upper()]
        if self.battery - battery_taken > 0:
            self.battery -= battery_taken
            return True, "The phone has battery"
        if self.battery - battery_taken <= 0:
            self.status, self.battery = False, EMPTY
            return False, "The phone has run out of battery"

    def switch_status(self, operation_type: str = "power_on" ) -> None:
        self.status = not self.status
        operation_type = "power_on" if self.status else "power_off"
        self.battery_drainage(operation_type)

    def install_apps(self, *apps) -> str:
        error_msgs = []
        if self.status == 0:
            return f"The device has to be on"
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)
            else:
                error_msgs.append(f"Unable to install {app}, already installed")
            outcome_status, msg = self.battery_drainage("app_power")
            if not outcome_status:
                return msg
        return "\n".join(error_msgs)

    def uninstall_apps(self, *apps) -> str| bool:
        error_msgs = []
        if self.status == 0:
            return f"The device has to be on"
        for index, app in enumerate(apps):
            if app in self.apps:
                self.apps.pop(index)
            else:
                error_msgs.append(f"Unable to install {app}, already installed")
            outcome_status, msg = self.battery_drainage("app_power")
            if not outcome_status:
                return msg
        return "\n".join(error_msgs)




output = len(["dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede"])
print(output * 2)

samsung = MobilePhone("Samsung", 7.5, 6)
print(samsung.status)
samsung.install_apps("dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede")
samsung.install_apps("dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede")
print(samsung.battery)
print(samsung.status)