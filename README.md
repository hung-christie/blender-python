# blender-python
This is a project to teach basic python coding through Blender, a free and open-source 3D computer graphics software that can create animated films, visual effects, art, 3D printed models, motion graphics, interactive 3D applications, virtual reality, and computer games. Whether you're a Blender expert or an avid Python coder (of which I was neither when I first started undertaking this project), hopefully at the end of this we'll be able to produce a simple, but useful visualization of population pyramids from different countries! In the process, hopefully you'll be familiar with:
* the basics of Blender
* the basics of coding in Python
* 3D visualization using a powerful computer science tool and computer graphics software. 

# downloads to get started
## Blender
https://www.blender.org/download/

Click on this link and download the most recent version (currently is Blender 2.90.1) and the version that is compatible with your operating system.

## Python3
In case you're unsure if you have Python downloaded, you can open the command line in Terminal on Mac and type `python3 --version` and press `enter`. If the version number comes up, then you should have Python3 downloaded. If a version number is not returned then it probably means that you don't have python installed. 

## Atom 
Atom is a text editor which I used to write my script - you can download from this button. 
https://atom.io/

# Blender basics
- When we first open Blender, we see that the scene already has a cube and other objects. In Blender's interface, to clear the scene, we can press `A`, which will select all the objects, then `X` and confirm by pressing `return`
- Pressing `Shift` `A`, looking under `Mesh` and selecting `Cube` will create a cube object in the center of the scene
- There are plenty of ways to experiment with this cube, but for the purposes of this graph, we can edit the scaling and

Some useful hotkeys: 
- `G` is to grab whatever is under your cursor
  - If you type `G`, then `X`, `Y` or `Z`, it will grab and moving the cursor will move the object only along that axis
- `S` allows you to scale the object
- `Shift` `D` copes and pastes the cube elsewhere in the scene
- `Shift` `A` opens the panel to add something
- (maybe link or add more things from Marlon's intro video)

# Python basics for this script


*Syntax*
- Line breaks conclude a statement (not a semicolon as in other languages)
- Blocks of statement begin with a colon and identified with indent
- Declaration of variable doesn't require datatype
- Make comments by initiating the statement with a (#)

# Blender with Python basics
Import bpy module 


# making our first graph

To make this 3D graph, we are just creating many blocks inside Blender and changing their sizes (lengths), as well as their locations based on the age group. Based on what we discussed about Python basics and Blender, here is how we will graph it with python: 

## to run this script in Blender, we also need to run this script through command line 
- we will have a shell script, that will run your python script inside Blender 
- to change the read requirements, type `chmod 755 launch_population.sh` inside the directory with the script, where `launch_population.sh` is the name of the shell script that will run our python script 
- adding `echo` on the first line of the shell script is sort of like a sanity check to see that the shell script is being run in terminal 

# additions to this project
* add color and labels 
* instead of using blocks, make it look like different shapes (each graph is its own donut, so that we can learn more about Blender's functionalities

# possible future projects
* visualize population pyramids over time (possibly as a movie)
* visualize population pyramids based on location on the map
* visualize population pyramids of different countries over time (switch from one countries' population pyramid to another country's population pyramid)
* visualize incidence and prevalence of a disease 
