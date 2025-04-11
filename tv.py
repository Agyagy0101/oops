# tv.py

# TV class as per UML design
class TV:
    def __init__(self, brand):
        self.brand = brand        # Brand of the TV
        self.channel = 1          # Default channel
        self.volume = 50          # Default volume
        self.on = False           # TV state
        self.price = 0            # Optional: price attribute
        self.inches = 0           # Optional: size in inches

    # Increase volume (max 100)
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        print(f"Volume increased to {self.volume}")

    # Decrease volume (min 0)
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        print(f"Volume decreased to {self.volume}")

    # Set channel (1 to 50)
    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
            print(f"Channel set to {self.channel}")
        else:
            print("Channel must be between 1 and 50")

    # Reset TV settings
    def reset(self):
        self.channel = 1
        self.volume = 50
        print("TV reset to default channel and volume")

    # Return current TV status
    def status(self):
        return f"{self.brand} TV at channel {self.channel}, volume {self.volume}"


# Example usage
if __name__ == "__main__":
    my_tv = TV("Samsung")
    my_tv.increase_volume()
    my_tv.set_channel(25)
    print(my_tv.status())
    my_tv.reset()
    print(my_tv.status())
