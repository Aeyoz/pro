CONSUMPTION_RATES = {"POWER_ON" : 5,
                    "POWER_OFF" : 2.5,
                    "APP_OPERATIONS" : 1}
FULL_CHARGE = 100
NO_CHARGE = 0

class MobilePhone:
    def __init__(
    self,
    manufacturer: str,
    screen_size: float,
    num_cores: int,
    apps: list[str] = ["whatsapp", "instagram", "chrome"],
    status: bool = True,
    battery_level: float = FULL_CHARGE):
    
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = apps
        self.status = status
        self.battery = battery_level

    def recharge(self, recharge_battery_level) -> None:
        recharge = min(FULL_CHARGE, self.battery + recharge_battery_level)
        self.battery = recharge

    def battery_drain(self, operation_type, drainage_chart = CONSUMPTION_RATES) -> tuple:
        battery_taken = drainage_chart[operation_type.upper()]
        choice = max(self.battery - battery_taken, NO_CHARGE)
        if choice > 0:
            self.battery -= battery_taken
            return True, "The phone has battery"
        else:
            self.status = False
            self.battery = NO_CHARGE
            return False, "The phone has run out of battery"

    def switch_status(self) -> str | None:
        if self.battery < CONSUMPTION_RATES["POWER_ON"] * 2:
            return "Not enough battery"
        self.status = not self.status
        operation_type = "power_on" if self.status else "power_off"
        self.battery_drain(operation_type)

    def install_apps(self, *apps: str) -> str:
        error_msgs = []
        if not self.status:
            return "The device has to be on"
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)
            else:
                error_msg = f"Unable to install {app}, already installed"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
            outcome_status, msg = self.battery_drain("app_operations")
            if not outcome_status:
                return msg
        return "\n".join(error_msgs)

    def uninstall_apps(self, *apps: str) -> str| bool:
        error_msgs = []
        if not self.status:
            return "The device has to be on"
        for index, app in enumerate(apps):
            if app in self.apps:
                self.apps.pop(index)
            else:
                error_msg = f"Unable to install {app}, already installed"
                if error_msg not in error_msgs:
                    error_msgs.append(error_msg)
            outcome_status, msg = self.battery_drain("app_operations")
            if not outcome_status:
                return msg
        return "\n".join(error_msgs)

samsung = MobilePhone("Samsung", 7.5, 6)
print(samsung.status)
samsung.install_apps("dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede")
samsung.install_apps("dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede")
samsung.install_apps("dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede")
samsung.install_apps("dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede","dede")
print(samsung.battery)
print(samsung.status)