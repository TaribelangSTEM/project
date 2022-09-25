from GameFrame import Globals, Story, EnumLevels


class Mil_S4(Story):
    def __init__(self, screen, joysticks):
        
        # - Information for Controller Overlay
        self.roomNum = EnumLevels.Mil_S4

        Story.__init__(self, screen, joysticks, "Milbi_4.wav", 'MilbiS', "Milbi_Background_4.png")
        self.set_timer(1050, self.complete)
    def complete(self):
        self.running = False
        Globals.next_level = EnumLevels.Home
