import pygame
import random

pygame.init()

# 设置屏幕
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# 自定义 Rect 类
class Rect(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(color)  # 填充颜色
        self.rect = self.image.get_rect(topleft=(x, y))  # 设置初始位置

    def update(self):
        # 更新位置
        self.rect.x += 5
        if self.rect.x >= 800:  # 如果超出屏幕底部，重置位置
            self.kill()
        screen.blit(self.image, self.rect)  # 绘制精灵
        

# 创建一个精灵组
all_sprites = pygame.sprite.Group()

# 创建一个 Rect 对象并添加到组

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if random.randint(0, 100) < 5:
        # 随机生成 Rect 对象并添加到组
        rect_sprite = Rect(-100, random.randint(0, 700), (255, 0, 0), 100, 100)
        all_sprites.add(rect_sprite)

    # 更新所有精灵
    all_sprites.update()

    # 绘制所有精灵
    screen.fill((0, 0, 0))  # 清屏
    all_sprites.draw(screen)  # 自动绘制所有精灵
    pygame.display.update()
    clock.tick(30)

pygame.quit()