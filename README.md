# PlotIt
**<ins>MEET THE TEAM !</ins>**
  
Hello! PlotIt is a project made by Cupșan Vanessa (321CB), Ignătescu Darius (321CB), Manea Andrei (321CB) and Pleșcan Matei (323CA). We were eager to know more about basic programming in Python, so making this project was a pleasant and useful learning experience. This README will present a brief summary of our contributions to the project and its functionalities.
  
**<ins>WHAT IS PLOTIT ?</ins>**
  
PlotIt is a plotting application in which the user can store data and get statistics and predictions regarding future measurements. The output of the app consists mostly in 2D graphs and stats coming from this graphs. The functionalities that PlotIt has are as following:
  
	-adding / removing points from the graph;
	-performing a linear regression with the data given;
	-calculating the derivative / integral for the graph obtained;
	-predicting the next value the user might want to plot to the graph;
	-extrapolate a point belonging to the linear regression graph;
	-displaying the working dataset at any point of plotting;
	-performing the best fitting for a dataset and drawing the graph accordingly;
  
**<ins>LANGUAGES AND TECHNOLOGIES WE USED</ins>**
  
For the implementation, we used Python for both the backend and frontend of the app. Some of the libraries we used were PySimpleGUI, matplotlib.pyplot, matplotlib.backends.backend_tkagg, numpy, sklearn.linear_model and scipy. 
  
**<ins>HOW TO USE PLOTIT?</ins>**
  
To use PlotIT, push the "Run Main" button(!["Run 'main'" button](DataPlotter/utils/run_button.jpg?raw=true "Title")) and let the magic happen. The app has a simple GUI and lets the user choose the functionality he needs by pressing one of the app's buttons. 
![TEXT](DataPlotter/utils/welcome_popup.jpg?raw=true "Title")
![TEXT](DataPlotter/utils/main_menu.jpg?raw=true "Title")
  
**<ins>WHO DID WHAT ?</ins>**
  
For the most part, all of us collaborated on most of the tasks, as we found working together the most efficient way of doing this project as a team. However we did have some individual tasks, such as: Darius did the addPoint, removePoint and findExtremes functions and also contributed to the update_plot (GUI function); Andrei worked on the basic GUI interface and planned the layout of the welcome window and buttons, also did the extrapolate function (I am also writing the present README if that counts); Matei was responsible for the backend part and implemented the classes in data_processing, also responsible for the code's modularity; Vanessa implemented the predict_next and display_dataset functions, as well as contributing to the refactorisation of the code after it was written. Again, it is worth mentioning that we all contributed equally to the project and helped each other with our tasks, as we believe that is what teamwork is all about.
  
**<ins>ERRORS OCCURANCE AND HANDLING</ins>**
  
One part that really took a lot of time to figure out was having our graph inside the GUI window, as we kept having it in a sepparate window in the beggining. That lead to a wannabe-refactorisation of the code and we had to reimplement our backend, which took quite some time, but in the end we figured it out. Also, we had to keep in mind the fact that we were losing parts of the dataset at some point because they weren't properly stored. That was solved after some hours of debugging. Besides that, the project went pretty much smoothly and probably the toughest thing to figure out was how to handle the frontend part using Python libraries, there was a lot of research done in that area. In the end, we are happy with the result and hope users find the app useful.

# Thank you for using PlotIt <3
