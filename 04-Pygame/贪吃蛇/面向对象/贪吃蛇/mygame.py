import pygame
import sys

class MyGame(object):
    "pygame模板类"
    # def __init__(self, **kwargs):
    #     self.game_name = kwargs.get("name") or GAME_NAME
    def __init__(self, name="My Game", size=(640, 480), fps=60,
                 font_filename="resources/Minecraft.ttf", font_size=16, icon=None):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(name)
        self.screen_size = self.screen_width, self.screen_height = size
        pygame.display.set_icon(pygame.image.load(icon)) if icon else None
        # icon and pygame.display.set_icon(pygame.image.load(icon))
        self.screen = pygame.display.set_mode((self.screen_size))
        self.fps = fps
        self.font = pygame.font.Font(font_filename, font_size)
        pygame.display.set_icon(pygame.image.load(icon)) if icon else None
        self.clock = pygame.time.Clock()
        self.now = 0
        self.background = pygame.Surface(self.screen_size)
        self.key_event_binds = {}
        self.gamedata_update_actions = {}
        # 更新画面要根据底层先画，上层后画的原则，要有次序
        self.display_update_actions = [self._draw_background]

        self.running = True
        self.key_bind(pygame.K_p, self.switch_running)

    def run(self):
        while True:
            self.now = pygame.time.get_ticks()
            self._process_events()
            if self.running:
                self._update_gamedata()
            self._update_display()
            self.clock.tick(self.fps)

    def switch_running(self):
        self.running = not self.running
        if self.running:
            for name, action in self.gamedata_update_actions.items():
                if action["next_time"]:
                    action["next_time"] = self.now + action["interval"]
    def _process_events(self):
        "事件处理"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                action, args = self.key_event_binds.get(event.key,
                                                        (None, None))
                action(**args) if args else action() if action else None
    def _update_gamedata(self):
        "更新游戏数据"
        for name, action in self.gamedata_update_actions.items():
            if not action["next_time"]:
                action["run"]()
            elif self.now >= action["next_time"]:
                action["next_time"] += action["interval"]
                action["run"]()

    def _update_display(self):
        # 更新画面显示
        for action in self.display_update_actions:
            action()
        pygame.display.flip()

    def _draw_background(self):
        # 绘制背景
        self.screen.blit(self.background, (0, 0))

    def key_bind(self, key, action, **args):
        self.key_event_binds[key] = action, args

    def add_update_action(self, name, action, interval=0):
        next_time = self.now + interval if interval else None
        self.gamedata_update_actions[name] = dict(run=action,
                                                  interval=interval,
                                                  next_time=next_time)
    def add_draw_action(self, action):
        self.display_update_actions.append(action)

    def quit(self):
        pygame.quit()
        sys.exit(0)