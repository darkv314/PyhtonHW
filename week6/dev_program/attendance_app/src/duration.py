class Duration:

    # Every Object to class Duration, is contructed by passing this values  hours, minutes, seconds
    def __init__(self, hours: int, minutes: int, seconds: int):
        # atributes of "Duration" class
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    
    def __str__(self) -> str:
        return f"{self.hours}h {self.minutes}m {self.seconds}s"