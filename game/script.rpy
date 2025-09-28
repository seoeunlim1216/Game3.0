# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ava")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg basementt

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    e "Hella Fella! You are a 30 year old man child in 30 thousand dollars worth of student loans (You never completed the program, you were kicked out for academic dishonesty). You are now living in your parents' basement."
    e "Time to move out! Now, go build a home! You get a 50 thousand dollar loan from your parents! Good luck!!!"
    e "Goal: Balance cost and sacrifice what you can to prevent lifelong debt on your parent's shoulders."
    e "You will have to build a FUNCTIONING house"

    scene bg gr

    e "Lets start with a FOUNDATION."
    e "Choose ONE of the following to SACRIFICE"

    scene bg foundation

menu:
    "Land survey - establish property boundaries, prevent legal disputes and financial loss, allow proper site planning (if not, you might get sued for encroachment or violating zoning law)":
        jump choice1_landsurvey
    "Site prep - prepare site by removing obstructions, make land a desired level, install necessary infrastructure (if not, you will be fined $50 000 by the Ontario government)":
        jump choice1_siteprep
    "Dig Trenches - create stable base for foundation, allow proper placement of concrete footings that support the house's structure (if not, your house will shift up and down)":
        jump choice1_digtrenches
    "Rebar - steel reinforcing bar to strengthen concrete in structural components like foundations, walls, and slabs (if not, your house will be weak to twists and pulls and crack or completely fail)":
        jump choice1_rebar

label choice1_landsurvey:
    e "Ehhh you sure about that???"
    jump choice1_done
label choice1_siteprep:
    e "That is a bad choice..."
    jump choice1_done
label choice1_digtrenches:
    e "Actually???"
    jump choice1_done
label choice1_rebar:
    e "oh ok that's concerning"
    jump choice1_done

label choice1_done:
    e "You have used $20 000"
    e "It is time for to build the WALLS"
    e "Choose ONE of the following to SACRIFICE"
    scene bg frame
    
menu:
    "Framing - create structure's framework using wood to provide support and shape to house (if not, you will basically not have a house :)":
        jump choice2_framing
    "Draining pipes - system for managing water from roofs, surface water, subsurface water (if not, you will have a flood every time it rains)":
        jump choice2_draining
    "Drywall - instal large, heavy panels of gypsum board onto studs to create walls and ceilings (if not, you will be wall-less, you will feel every drop of rain, wind, and snow on your bare skin)":
        jump choice2_drywall

label choice2_framing:
    e "REALLY???"
    jump choice2_done
label choice2_draining:
    e "DAMN."
    jump choice2_done
label choice2_drywall:
    e "THATS ACTUALLY CRAZY"
    jump choice2_done

label choice2_done:
    e "You have used $10 000"
    e "It is time build the ELECTRICITY"
    scene bg electricity
menu:
    "Electrical boxes, switches, outlets - switches control power, outlets provide power (if not, you can't control the power, therefore, you cannot have electricity)":
        jump choice4_boxes
    "Main electrical Panel - central hub of a home's electrical system (if not, you can't have electricity)":
        jump choice4_panel
    "Wire through studs - transmit the electricity from source to whatever needs the powers (If not, why even have electricity if you can't carry the electricity? :/":
        jump choice4_studs

label choice4_boxes:
    e "WOW...."
    jump choice4_done
label choice4_panel:
    e "ARE YOU SERIOUS"
    jump choice4_done
label choice4_studs:
    e "No way"
    jump choice4_done

label choice4_done:
    e "You have used $5000"
    e "It is time build the PLUMBING"
    e "Choose ONE of the following to SACRIFICE"
    scene bg plumbing

menu:
    "Rough-In - underground and above-ground pipes, drains, and vents are installed before walls are closed (if not, you will have feces and piss filled water in your wall :)":
        jump choice5_rough
    "Top-Out - vertical vent stacks are run through the building (if not, you will also have feces and piss filled water in your wall :)":
        jump choice5_top
    "Trim-Out - installing all the visible fixtures and appliances (if not, you will have feces and piss filled water on your floor :)":
        jump choice5_trim

label choice5_rough:
    e "Ewwwwww bro what"
    jump choice5_done
label choice5_top:
    e "Ya... No."
    jump choice5_done
label choice5_trim:
    e "Oh..."
    jump choice5_done

label choice5_done:
    e "You have used $15 000"
    e "It is time build the ROOFING"
    e "Choose ONE of the following to SACRIFICE"
    scene bg roofing

menu:
    "Framing - supporting structure of roof, primarily using pre-fabricated trusses or traditional rafters and ceiling joists (if not, don't even think about having a roof)":
        jump choice6_frame
    "Sheathing - structural layer of wood panels like plywood or OSB attached to the roof's rafters or trusses (if not, expect to wear a umbrella indoors)":
        jump choice6_sheath
    "Tiling - installing chosen roof covering like shingles or tiles (if not, your house will look like it's under construction forever)":
        jump choice6_tile

label choice6_frame:
    e "REALLY???"
    jump choice6_done
label choice6_sheath:
    e "what?!"
    jump choice6_done
label choice6_tile:
    e "No you are joking"
    jump choice6_done

label choice6_done:
    e "You have used $20 000"
    show bg modern

    e "YAY YOUR HOUSE IS DONE"
    e "Time to plan a houswarming party!"

    show bg house
    e "oh wait, nevermind..."
    e "WOW that's rough..."
    show bg basementt
    e "See no matter what u do, your house would have collaped"
    e "You're too broke"
    e "Look at you, in your parent's basement again..."
    e "Get a job"
    e "Then an apartment..."
    e "Also, you went over budget"
    e "your debt is now $100 000"
    e "Good luck in life <3"

    # This ends the game.
    return