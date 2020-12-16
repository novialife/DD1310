class TV:
    def __init__(self, name, channel="", volume=""):
        self.name = name
        self.channel = channel
        self.volume = int(volume)

    def __str__(self):
        return '\n%s\nChannel: %s\nVolume: %s ' % (self.name, self.channel, self.volume)

    def device_name(self):
        return self.name

    def low_vol(self):
        if self.volume <= 0:
            self.volume = 0
        else:
            self.volume -= 1

    def inc_vol(self):
        if self.volume >= 10:
            self.volume = 10
        else:
            self.volume += 1

    def change_channel(self, channel):
        self.channel = channel

    def tv_list(self):
        return [self.name, self.channel, self.volume]