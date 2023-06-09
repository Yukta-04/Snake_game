from tkinter import *
import random
#constants in our game
GAME_WIDTH=1000
GAME_HEIGHT=500
SPEED=100
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="#00FF00"
FOOD_COLOR="#FF0000"
BACKGROUND_COLOR="#000000"
class Snake:
    #this will create snake object
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.squares=[]
        #we need to create a listb of coordinates
        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        #to craete some squares
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.squares.append(square)




class Food:
    #this function will construct food object for us
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        #setting coordinates
        self.coordinates=[x,y]
        #drawing food objects
        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")


#we will call this function as we start the game
def next_turn(snake,food):
    x,y=snake.coordinates[0]#head of the snake
    if direction == "up":
        y-=SPACE_SIZE

    elif direction=="down":
        y+=SPACE_SIZE

    elif direction=="left":
        x-=SPACE_SIZE

    elif direction=="right":
        x+=SPACE_SIZE
    snake.coordinates.insert(0,(x,y))
    #to create new graphics for the head of the snake
    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    #need to update snake list of squares
    snake.squares.insert(0,square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")#we can just use the name of the tag to delete it
        food=Food()#create Food object
    else:#we will only delet a part of a snake when we dont eat a food
        #we need to delete the last square of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()#collision then call game_over function
    else:#update to the next turn

    #call the next turn function again for next turn
        window.after(SPEED,next_turn,snake,food)
def change_direction(new_direction):
    global direction#old direction
    if new_direction=='left':
        if direction!="right":
            direction=new_direction
    if new_direction == 'right':
        if direction != "left":
            direction = new_direction
    if new_direction == 'up':
        if direction != "down":
            direction = new_direction
    if new_direction == 'down':
        if direction != "up":
            direction = new_direction
def check_collisions(snake):
    #head of the snake  x,y
    x,y=snake.coordinates[0]
    if x<0 or x>=GAME_WIDTH:
        print("Game Over")
        return True
    if y<0 or y>=GAME_HEIGHT:
        print("Game Over")
        return True
    #if snake touches its own body part
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            print("Game Over")
            return True
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="Game Over",fill="red",tag="gameover")

window=Tk()
window.title("Snake Game")
window.resizable(False,False)
score=0
direction="down"
#to add label to the game
label=Label(window,text="score:{}".format(score),font=("consolas",40))
label.pack()
#to add background color
canvas=Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()
#to center the screen
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>',lambda event:change_direction('left'))
window.bind('<Right>',lambda event:change_direction('right'))
window.bind('<Up>',lambda event:change_direction('up'))
window.bind('<Down>',lambda event:change_direction('down'))

#creating snake object and food object
snake=Snake()
food=Food()
next_turn(snake,food)
window.mainloop()

