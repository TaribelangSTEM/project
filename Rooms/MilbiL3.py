from GameFrame import Level


class MilbiL3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("PlaceHolderBackgroundMLBL3.png")
