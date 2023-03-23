CONSUMPTION_CHART = {"POWER_ON" : 5, "POWER_OFF" : 2.5, "APP_POWER" : 1}

class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int\
        , apps: list[str] = ["whatsapp", "instagram", "chrome"], status: bool =\
        False, battery_level: float = 100):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = apps
        self.status = status
        self.battery = battery_level

    def recharge(self, recharge_battery_level) -> None:
        for i in range(recharge_battery_level + 1):
            if i == recharge_battery_level:
                break
            self.battery += 0.5 if 100 - self.battery < 1 else 1

    def battery_drainage(self, operation_type, dreinage_chart = CONSUMPTION_CHART) -> None:
        self.battery -= dreinage_chart[operation_type.upper()]

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
            self.battery_drainage("app_power")
        return "\n".join(error_msgs)

    def uninstall_apps(self, *apps) -> str:
        error_msgs = []
        if self.status == 0:
            return f"The device has to be on"
        for index, app in enumerate(apps):
            if app in self.apps:
                self.apps.pop(index)
            else:
                error_msgs.append(f"Unable to install {app}, already installed")
            self.battery_drainage("app_power")
        return "\n".join(error_msgs)

samsung = MobilePhone("Samsung", 7.5, 6)