# blender-python
This is a project to teach basic python coding through Blender, a free and open-source 3D computer graphics software that can create animated films, visual effects, art, 3D printed models, motion graphics, interactive 3D applications, virtual reality, and computer games. Whether you're a Blender expert or an avid Python coder (of which I was neither when I first started undertaking this project), hopefully at the end of this we'll be able to produce a simple, but useful visualization of population pyramids from different countries! The goal is to learn: 
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
- There are plenty of ways to experiment with this cube, but for the purposes of this graph, we can edit the scaling and location by looking the transform options under the Cube object. We can find this at the bottom right panel, click `Object Properties` (the orange square), and select `Transform`. From there, we can edit details about this cube such as location on the X, Y, or Z axes, as sell as how we want to scale in the X, Y or Z directions.  

Some useful hotkeys: 
- `G` is to grab whatever is under your cursor
  - If you type `G`, then `X`, `Y` or `Z`, it will grab and moving the cursor will move the object only along that axis
- `S` allows you to scale the object
- `Shift` `D` copes and pastes the cube elsewhere in the scene
- `Shift` `A` opens the panel to add something
- (maybe link or add more things from Marlon's intro video)

# Python basics for this script
- Lists are used to store multiple items in a single variable and are created using square brackets `[]` and assigning them to a variable name
  - We can access list items by their indices, which start at 0 and end at the (length - 1)
  - There are various data types in Python that lists can stores, including strings, ints, and boolean:
    - string_list = ['computer', 'phone', 'tv']
    - int_list = [1, 2, 3, 4, 5]
    - boolean_list = [True, False, True, False, True]
- Loops are useful in python to help iterate over sequences or execurte a set of statements. For loops are particularly useful for iterating through a list. We can go through all the elements in a list and do an action. For example, if we were to iterate through our `string_list` we can print each element in the list. 
- To import a data file, such as a .csv file, we can use the `with open('_.csv') as f` function to open parse through the datafile. 

*Syntax*
- Line breaks conclude a statement (not a semicolon as in other languages)
- Blocks of statement begin with a colon and identified with indent
- Declaration of variable doesn't require datatype
- Make comments by initiating the statement with a (#)

# Blender with Python basics
- Blender provides the `bpy` module to the python interpreter. To access blender data, classes, and functions, we will need to import the module with `import bpy` at the top of the script. 
- To add a cube as discussed before, we can use the the bpy module to create a mesh object (in this case, a cube). The specific line is `bpy.ops.mesh.primitive_cube_add()`. To specify the size of the cube, `primitive_cube_add()`, takes in an argument called `size`. 
- To get access to the cube in the 3D, we will just call the `bpy.context.active_object`. This will help us change the parameters of the cube cube, such as its location and scaling. 
  - By calling `.location` on our cube, we can specify if we want to change the location on a specific axis. For example, `.location[0] = 10` will change the position of the cube on the x axis to position 10. 
  - By calling `.scale` on our cube, we can specify how we can to transform the objects size. For example, `.scale = (1, 100, 1)` will scale the object by 100 times along the y axis, but it will remain the same along the x and z axes. 

# making our first graph
The scripts can be found in this folder (it'll be easier to reference directly while looking at this). To make this 3D graph, we are just creating many blocks inside Blender and changing their sizes (lengths), as well as their locations based on the age group. This folder has two data files, the population numbers for both male and female for different age groups in `.csv` files for the USA and Japan. Based on what we discussed about Python basics and Blender, here is how we will graph it with python: 
- intialize lists to store male and female population numbers for different age groups for different countries by assigning it to a variable to store datapoints
- open each `.csv` file. We have a `US_2020.csv` and a `Japan_2019.csv`. We will parse through the data files to add to the lists we had initialized before hand. Parsing through the lists will require some cleaning, but at the end, we want a list with just population numbers, ordered by the age group from youngest to oldest. 
- Then we can plot the population pyramids. To plot the US population pyramid, we will parse through the US female population first, adding a cube for each datapoint, putting the cube on a location in Blender based on the age group, and then scaling it based on the population size. We will use the `for` loops and `bpy` module to achieve this. We will then do the same for the US male population, but plotting it at a different location. This can also be repeated for the Japanese population, also just at a different location, which we can do by changing the location of the cubes. 

## to run this script in Blender, we also need to run this script through command line 
- we will also have to write a shell script, that will run your python script inside Blender 
  - the script will call the Blender application, and then call the Python script that we just wrote with `--python` and then the location of the script in our directory
  - adding `echo` on the first line of the shell script is sort of like a sanity check to see that the shell script is being run in terminal 
- to run the script, we first have to change the read requirements, type `chmod 755 launch_population.sh` inside the directory with the script using `Terminal`, where `launch_population.sh` is the name of the shell script that will run our python script 
- then right after, we can launch the shell script with `./launch_population.sh` inside our Terminal. This will open up Blender with our population pyramid. 

# some notes
- my scripts that I added are specific to my directory on my machine, so you may have to edit locations when accessing data files, Blender, or the python script 

# currently working on 
* adding color and labels 
* instead of using blocks, making it look like different shapes (each graph is its own donut, so that we can learn more about Blender's functionalities)

# possible future projects
* visualize population pyramids over time (possibly as a movie)
* visualize population pyramids based on location on the map
* visualize population pyramids of different countries over time (switch from one countries' population pyramid to another country's population pyramid)
* visualize incidence and prevalence of a disease 
