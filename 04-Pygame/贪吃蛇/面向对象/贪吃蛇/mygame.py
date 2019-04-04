import pygame
import sys
class MyGame(object):
    "pygame模板类"
    def __init__(self, name="My Game", size=(640, 480), fps=60, icon=None):
        pygame.init()
        pygame.display.set_caption(name)
        self.screen_size = self.screen_width, self.screen_height = size
        self.screen = pygame.display.set_mode((self.screen_size))
        self.fps = fps
        pygame.display.set_icon(pygame.image.load(icon)) if icon else None
        self.clock = pygame.time.Clock()
        self.now = 0
        self.background = pygame.Surface(self.screen_size)
        self.key_event_binds = {}
        self.gamedata_update_actions = {}
        # 更新画面要根据底层先画，上层后画的原则，要有次序
        self.display_update_actions = [self._draw_background]

    def run(self):
        while True:
            self.now = pygame.time.get_ticks()
            self._process_events()
            self._update_gamedata()
            self._update_display()
            self.clock.tick(self.fps)

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                action, args = self.key_event_binds.get(event.key,
                                                        (None, None))
                action(**args) if args else action() if action else None
    def _update_gamedata(self):
        for name, action in self.gamedata_update_actions.items():
            if not action["next_time"]:
                action["run"]()
            elif self.now >= action["next_time"]:
                action["next_time"] += action["interval"]
                action["run"]()

    def _update_display(self):
        for action in self.display_update_actions:
            action()
        pygame.display.flip()

    def _draw_background(self):
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