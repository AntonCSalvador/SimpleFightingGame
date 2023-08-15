import pygame

class Player:
    def __init__(self, x, y):
        self.start_position = (x, y)
        self.current_position = self.start_position

    def move(self, dx, dy):
        self.current_position = (self.current_position[0] + dx, self.current_position[1] + dy)

    def draw():
        print("hi")

    def update():
        print("hi")
        # this.position.y += this.velocity

# def animate():
#     requestAnimationFrame(animate)

class Projectile:
    def __init__(self, x, y, velocity):
        self.start_position = (x,y)
        self.current_position = self.start_position
        self.velocity = velocity


    def move(self, dx, dy, velocity):
        self.current_position = (self.current_position[0] + dx, self.current_position[1] + dy)

class Floor:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)  # Green color for the ground

class HealthBar():
    def __init__(self,x,y,w,h,max_hp):
        self.x=x
        self.y=y 
        self.w = w
        self.h = h
        self.hp = max_hp #bc you assume it starts at full health 
        self.max_hp = max_hp

    def draw(self, surface):
        #calculate health ratio
        ratio = self.hp/self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create player objects and a Floor object
player1 = Player(100, 400)
player2 = Player(400, 400)
floor = Floor(0, 550, 800, 50)  # Creating a floor rectangle
health_bar1 = HealthBar(10,10, 300, 40, 100)


projectiles = []  # List to store active projectiles


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    #healthbars
    health_bar1.draw(screen)

    #physics
    # Check for collisions and apply gravity
    if player1.current_position[1] + 40 <= floor.rect.y:  # Adjusted for character's height
        player1.current_position = (player1.current_position[0], floor.rect.y - 40)  # Set character on top of the floor
    else:
        player1.move(0, 2)  # Apply gravity to player1

    if player2.current_position[1] + 40 <= floor.rect.y:  # Adjusted for character's height
        player2.current_position = (player2.current_position[0], floor.rect.y - 40)  # Set character on top of the floor
    else:
        player2.move(0, 2)  # Apply gravity to player2

    # Move and draw player objects
    #if keypress  = w:
        #move player1 up in the y axis
    #if keypress = d:
        #move player1 to the right    
    keys = pygame.key.get_pressed()
    # Move player1 up in the y-axis

    #player 1 movement
    if keys[pygame.K_w]:
        player1.move(0, -20)
    if keys[pygame.K_d]:  # Move player1 to the right
        player1.move(2, 0)  # Positive dx value moves character to the right
    # if keys[pygame.K_s]:  # Move player1 up in the y-axis
    #     player1.move(0, 2)  # Negative dy value moves character upward
    if keys[pygame.K_a]:  # Move player1 to the right
        player1.move(-2, 0)  # Positive dx value moves character to the right

    if keys[pygame.K_r]:
        #might need to + the pixels of the player to current positions
        throw = Projectile(player1.current_position[0],player1.current_position[1], 2)
        projectiles.append(throw)  # Add the new projectile to the list
        print("projectile thrown")

    projectiles_to_remove = []  # List to store projectiles that should be removed

    # Move and draw projectiles
    for projectile in projectiles:
        projectile.move(projectile.velocity, 0, 2)  # Move projectile horizontally
        pygame.draw.circle(screen, (255, 255, 0), projectile.current_position, 10)  # Draw the projectile
        
        # Check for collision with player2
        if (player2.current_position[0] - 20 == projectile.current_position[0]) and \
           (player2.current_position[1] == projectile.current_position[1]):
            projectiles_to_remove.append(projectile)
            print(health_bar1.hp)
            health_bar1.hp = health_bar1.hp - 1
            print(health_bar1.hp)

        # Remove collided projectiles
    for projectile in projectiles_to_remove:
        projectiles.remove(projectile)

    #player 2 movement
    if keys[pygame.K_UP]:  # Move player1 up in the y-axis
        player2.move(0, -20)  # Negative dy value moves character upward
    if keys[pygame.K_RIGHT]:  # Move player1 to the right
        player2.move(2, 0)  # Positive dx value moves character to the right
    # if keys[pygame.K_DOWN]:  # Move player1 up in the y-axis
    #     player2.move(0, 2)  # Negative dy value moves character upward
    if keys[pygame.K_LEFT]:  # Move player1 to the right
        player2.move(-2, 0)  # Positive dx value moves character to the right


    # Draw floor
    floor.draw(screen)

    # Draw rectangles for characters
    player1_rect = pygame.Rect(player1.current_position[0] - 20, player1.current_position[1], 40, 40)
    player2_rect = pygame.Rect(player2.current_position[0] - 20, player2.current_position[1], 40, 40)
    pygame.draw.rect(screen, (255, 0, 0), player1_rect)
    pygame.draw.rect(screen, (0, 0, 255), player2_rect)

    



    pygame.display.flip()
    clock.tick(60)

pygame.quit()


#physics temp
    # Move and draw player objects
    #if keypress = d:
        #move player1 to the right

    #create a floor
    #if position =< floor:
        #position = floor
            #or
        #gravity = 0

