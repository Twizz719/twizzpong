import pygame, sys, random #import modules

def reset_ball(): # function for resetting ball
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])
    
def point_won(winner): # function for score
    global cpu_point, player_point
    if winner == "cpu":
        cpu_point += 1
    if winner == "player":
        player_point += 1
        
    reset_ball()
        
def animate_ball(): #function for collisions with ball
    global ball_speed_x, ball_speed_y
    if ball.bottom >= screen_height or ball.top <= 0:
      ball_speed_y *= -1
      
    if ball.right >= screen_width:
      point_won("cpu")
        
    if ball.left <= 0: 
      point_won("player")
      
    if ball.colliderect(player) or ball.colliderect(cpu):
      ball_speed_x *= -1
              
def animate_player(): # function for keeping players in screen
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
        
    if player.bottom >= screen_height:
        player.bottom = screen_height
        
def animate_cpu(): # function to keep AI hitting ball
    global cpu_speed
    cpu.y += cpu_speed
    
    if ball.centery <= cpu.centery:
      cpu_speed = -6
    if ball.centery >= cpu.centery:
      cpu_speed = 6
        
    if cpu.top <= 0:
      cpu.top = 0
    if cpu.bottom >= screen_height:
      cpu.bottom = screen_height  
    

pygame.init() #initializes program

screen_width = 1280 #pixels
screen_height = 800 #pixels

# creates display using pygames (set)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONG!") # game name

clock = pygame.time.Clock() # Defines variable clock to module from pygame

ball = pygame.Rect(0,0,30,30) # Ball variable from a class that defines rectangle(X,Y,W,H)
ball.center = (screen_width/2, screen_height/2) #Defines "handle" of how to move rectangle

cpu = pygame.Rect(0, 0, 20, 100) # position of cpu
cpu.centery = screen_height / 2

player = pygame.Rect(0, 0, 20, 100) # position of player
player.midright = (screen_width, screen_height/2)

ball_speed_x = 6 # variables
ball_speed_y = 6
player_speed = 0
cpu_speed = 6
cpu_point, player_point = 0, 0
score_font = pygame.font.Font(None, 100)

while True:# boolean for game loop that allows exit of game
    for event in pygame.event.get(): # explains path to pull object from
        if event.type == pygame.QUIT:
          pygame.quit() # explains what it is
          sys.exit() # performs function to exit the game
          
        if event.type == pygame.KEYDOWN: # assigns keyboard actions from pygame library
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
              player_speed = 6
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
              player_speed = 0
            if event.key == pygame.K_UP:
              player_speed = 0     
                  
          
    ball.x += ball_speed_x
    ball.y += ball_speed_y 
    
    animate_ball() 
    animate_player()
    animate_cpu()
  
    
    screen.fill('black')
    
    # displays score on screen
    cpu_score_surface = score_font.render(str(cpu_point), True, "white")
    player_score_surface = score_font.render(str(player_point), True, "white")
    screen.blit(cpu_score_surface,(screen_width/4, 20))
    screen.blit(player_score_surface,(3* screen_width/4, 20))
    
    # draws objects onto screen
    pygame.draw.aaline(screen, 'white',(screen_width / 2, 0), (screen_width / 2 , screen_height))    
    pygame.draw.ellipse(screen,'white',ball) # Draws rectangle with ball paramaters  
    pygame.draw.rect(screen, 'white', cpu)
    pygame.draw.rect(screen, 'white', player)     
 
    pygame.display.update() # Updates current screen to user
    clock.tick(60) # fps in clock module

# Drawing the screen
# 1. Display surface
# 2. Draw surface
# 3. Objects within rectangle

# Remember rect object attributes








