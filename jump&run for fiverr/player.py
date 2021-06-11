import pygame

class Player():

    def __init__(self, rect, color):
        self.movement = [0, 0]
        self.jumoingRangeValue = 20
        self.jumpingRange = self.jumoingRangeValue
        self.isJumping = False
        self.rect = rect
        # 0 = left | 1 = right
        self.headDirection = 0 
        self.color = color
    
    def show(self, win, bgColor):
        
        pygame.draw.rect(win, self.color, self.rect)

        width = self.rect.right - self.rect.left
        height = self.rect.bottom - self.rect.top

        if self.headDirection == 0:
            pygame.draw.rect(win, bgColor, (self.rect.left + width * 0.1, self.rect.top + height * 0.1, width * 0.3, height * 0.3))

        else:    
            pygame.draw.rect(win, bgColor, (self.rect.left + width * 0.6, self.rect.top + height * 0.1, width * 0.3, height * 0.3))


    def move(self):
        # x axis
        self.rect.left += self.movement[0]

        # y axis
        if self.isJumping:
            if self.jumpingRange >= self.jumoingRangeValue * -1:
                self.rect.top -= self.jumpingRange
                self.jumpingRange -= 1
            else:
                self.jumpingRange = self.jumoingRangeValue   
                self.isJumping = False
    
    def shoot(self):
        pass