# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ava")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg GroundR

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hello Engineer! You are a 30 year old man child in 30 thousand dollars worth of student loans (You never completed the program, you were kicked out for academic dishonesty). You are living at home with your parents."
    e "Time to move out! Now, go build a home! You get a 100 thousand dollar loan from your parents! Good luck!!!"
    e "Goal: Balance cost and sacrifice what you can to prevent lifelong debt on your parent's shoulders."
    e ""
    # This ends the game.



    return
