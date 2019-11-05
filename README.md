# Project description

## Overview
These two visualizations aim at giving insight into internet users and how their
level of comfort with technology and their attitude towards an internet-connected future
relates to the devices they own.

The first visualization is a heatmap that combines 2 categorical "somethings"
about the users. The y-axis shows the users' description of their level of experience
with technology. The 4 options are:  

*I consider myself:*
- **Ultra Nerd**: I build my own computers, run my own servers, code my own apps. I’m basically Mr. Robot.
- **Technically Savvy**: I know my way around a computer pretty well. When anyone in my family needs technical help, I’m the one they call.
- **Average User**: I know enough to get by.
- **Luddite**: Technology scares me! I only use it when I have to.

The x-axis shows the users' attitude. The 5 categories are:  

*Thinking about a future in which so much of your world is connected to the internet leaves you feeling:*
- **Super excited!** I can’t wait for everything to be connected. My life will be so much better.
- **Cautiously optimistic.** I’m hopeful we’re building a better world by becoming more connected in everything we do.
- **On the fence.** I’m not sure about all this. I think I’ll wait and see.
- **A little wary.** All this being connected to the internet in every part of our lives makes me a little nervous. What’s going to happen to our privacy?
- **Scared as hell.** The future where everything is connected has me scared senseless. We’re all doomed!

Each cell in the heatmap shows how many users are in that particular intersection of user level and
user attitude. For example, there is a large amount of average users that feel *a little wary* about the future. On the other hand, there is only a very small group of users that describes themselves as "Luddites" and that are very excited about the future. This first visualization answers the question: what is the relationship between the user level and
attitude towards the future? It also allows us to compare the sizes of these groups and therefore gives us information
about which internet user types are most common.

The second visualization is a stacked barplot that - for a number of internet connected devices like routers, smart phones, but also smart door locks - shows the total number of users that own that device. Each of the individual rectangles in the stacked bar represents the number of users that owns the device for one of the user groups defined in the heatmap. This visualization answers the question: for each subtype of users, how many of them use certain devices?

The two visualizations are connected through interaction. Clicking on any of the squares on the heatmap shows that subgroup of users highlighted in the stacked barplot. The tooltip on these highlighted items shows which percentage of users in the selected subgroup uses a particular device. The heatmap also has a small tooltip that shows how many users are in each subgroup.

## Implementation
#### Preprocessing
Both the heatmap and the stacked barplot require a different type of access to the data  than, for example, a simple scatterplot. Because of that, we preprocessed the data using two different scripts.

[preprocess_user_data.py](https://github.com/INFO-4602-5602/project-1-mozilla-5602_project1_annebeth_-chandan_telly/blob/master/preprocessed_data/preprocess_user_data.py) is used to preprocess the heatmap data. It takes the columns from the original csv and calculates how many of the survey takers are in each of the user subgroups (for example: *Average User x A little wary*).

[preprocess_device_data.py](https://github.com/INFO-4602-5602/project-1-mozilla-5602_project1_annebeth_-chandan_telly/blob/master/preprocessed_data/preprocess_device_data.py) is used to preprocess the stacked barplot data. It creates a new csv file that has the user subgroups (for example: *Average User x A little wary*) as columns and the devices as rows. Each integer then represents the number of users in a subgroup owning a certain device.

#### Interaction
The interaction in the visualizations consists of two types of components:
1. Tooltips and
2. A click that connects the heatmap to the barplot

With the tooltips, we tried to add information that was not obvious from the visualization itself. For example, in the heatmap, it is clear which groups have higher values, but it is not possible to retrieve the exact values. Because of that, we added a tooltip with this information. The tooltip for the barplot is a little bit more complex: instead of showing the exact value of devices owned per group, it shows the percentage of people in that group owning a device. Since the group sizes are so dissimilar, this gives much more insightful information. For example, even though the Ultra Nerds only represent a very small number of respondents (and therefore only small "slices" in the stacked barchart) more than 90% of them owns a router - independent of whether they are feeling "Scared as hell" or "Super excited". Note: the tooltips are only visible for selected subgroups, so not for the initial/total barplot.

Clicking on any of the squares in the heatmap triggers the selection of that subgroup in the stacked bar chart. This emphasizes the connection between the two visualizations and lets a user of the visualization do interesting tasks like seeing which kind of users own which kinds of devices. For example: do people who feel scared about internet connectedness generally own less smart devices?

The connection between the heatmap and the barplot is made through the use of classes that represent the groups of users (e.g., Average Users who feel A little wary). On the click on the heatmap, the class of that square (e.g.,".Average_User_A_little_wary") is used to update the barplot to highlight the parts of the stack with the same class attached to it.

## Design process and roles
Our design process consisted of the following steps. All of the steps that do not mention a specific group member where done by the whole group.

1. An initial brainstorming meeting in which we familiarized ourselves with the data and came up with possible visualizations and tasks.
2. Creating mock-ups of some of our ideas.
3. Preprocessing the survey data. [Annebeth]
4. Start of implementation:  
  - Code for layout and creating canvases. [Nishank]
  - Initial code for heatmap. [Chandan]
  - Initial code for barplot. [Tetsumichi]
5. Combining the code and adding interaction. [Annebeth]
6. Review and discussion of further changes.

Our choice for these visualizations was guided by the choice for the heatmap, with which we could relate two columns of categorical data on user types. Based on that, we thought about other interesting tasks with which to combine the subgroups of users. That is how we decided on the (simple) barplot for the second visualization: the numeric data here gives even more information about the people in the user subgroups.

## Running the project
This project can be run in the browser by cloning the Github project or by downloading the zipped folder. Although the visualizations depend on preprocessed data, that data is available in the folder [preprocessed_data](https://github.com/INFO-4602-5602/project-1-mozilla-5602_project1_annebeth_-chandan_telly/tree/master/preprocessed_data). By using the project folder as the root folder and running a server (for example: `python -m SimpleHTTPServer`), the visualizations should be visible on [localhost](http://localhost:8000/).

## Sources
To implement this project, we looked at various sources. Below is a link to the sources and a short description of which part of the source were used:

- An overview of how to create a basic heatmap: https://www.d3-graph-gallery.com/graph/heatmap_basic.html.
- An overview of how to create a basic stacked barplot: https://www.d3-graph-gallery.com/graph/barplot_stacked_basicWide.html.
- Help with finding the domain of y-axis in a stacked barplot: https://bl.ocks.org/DimsumPanda/689368252f55179e12185e13c5ed1fee.
- Ideas on adding tooltips on hover: https://www.d3-graph-gallery.com/graph/barplot_stacked_hover.html &
https://www.d3-graph-gallery.com/graph/heatmap_style.html
- Ideas on how to select a group in a stacked barplot: https://www.d3-graph-gallery.com/graph/barplot_stacked_highlight.html.
