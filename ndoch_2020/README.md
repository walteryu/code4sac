## Code of America - NDoCH 2020
### Code for Sacramento - Asset Map

![asset_map][02.xx]
[02.xx]: https://github.com/walteryu/code4sac/blob/master/ndoch_2020/asset_map.PNG

### Change Log
* 08-21-2020: Baseline Version v0.1

### Introduction
This project focuses on the asset map item for the [CFA NDoCH][02.01] event; it consists of a web application to visualize various assets within the Sacramento area. The data is sourced from various open data portals.

Data processing and maps are created using Jupyter Notebook due to its ability to visualize results effectively and efficiently. Listed below are installation instructions and more about Jupyter and the Python programming language.

### Instructions
The CFA-NDoCH instructions are shown below and specify that open data sources should be used to visualize resources available to the Sacramento community. This notebook is intended as starting point to visualize such data for further development.

> Asset mapping is an integral part of empowered community building that is based on understanding the strengths and needs of diverse communities. First, use publicly available information about your locale to give a sense of the landscape and demographics. Next, research the location and availability of government programs (e.g. county health and human services offices), community based organizations (like resource centers, food banks, and legal aid clinics) or other resources that are vital to your community. Visually documenting the landscape can help identify what might make your community more equitable and accessible to all who live there.

### Approach
This notebook starts with a tutorial using Python mapping tools as a prototype, then develops a map for the Sacramento area. Open data sources are listed below and will be added to with additional development.

*Tutorials*
1. [Folium Tutorial: SFPD Crime Data][03.01]
2. [SFPD Crime Report Data (2003-18)][03.02]
3. [Folium Example: Cluster Markers][03.03]
4. [Folium Tutorial: Cluster Markers (JPYTR)][03.04]
5. [Folium Tutorial: Shapefile Data (Medium)][03.05]

*CA Geoportal Data*
1. [CA Geoportal: Open Datasets][04.01]
2. [CA School Locations (2019-20)][04.02]
3. [CA Healthcare Shortage (Primary Care)][04.03]
4. [CA Healthcare Shortage (Mental Health)][04.04]
5. [CA Healthcare Shortage (Dental Care)][04.05]

*SACOG Data*
1. [Sac Region LIHM Communities (2016)][05.01]
2. [Sac Region High Transit Frequency Areas (2020)][05.02]
3. [Sac Region High Quality Transit Areas (2017)][05.03]

*City of Sacramento Data*
1. [City of Sacramento Bike Facilities (2018)][06.01]
2. [City of Sacramento Bike Opportunity Areas (2016)][06.02]

### Jupyter Installation
1. Download and install Jupyter Notebook from their [website][01.01]
2. Verify that Jupyter Notebook was installed and visible from Windows Start menu
3. Start Jupyter Notebook; it will start CMD shell and load in the web browser
4. Save this notebook and CSV data to your "Documents" folder and navigate to it from the Notebook start page
5. Open this notebook from the start page; file and cells should be viewable

### Jupyter Introduction
This notebook will require some basic understanding of the Python programming language, Jupyter platform and data analysis concepts.

Jupyter is a powerful collaborative tool which is open-source and light-weight. It provides all the tools necessary to run data analysis, visualization, statistics and data science [out of the box][01.02]. In addition, it has gain acceptance from industry and academia for collaborating on projects and publishing work.

Jupyter is a combination of text and code with the programming run-time built into the platform so there is no need to install additional software. The text is in the markdown file format (similar to HTML), and code in several languages. It is organized by cells which can consist of either text or code; placed together, they can be sent as a single document to share/publish work.

### Jupyter Notebook
Notebooks are organized by cells, which mainly consist of text (in markdown) and code (Python). It operations like a hybrid between MS Word and Excel file; whereas the entire file is like a document, the cells operate like a spreadsheet. For getting started, feel free to scroll down each cell and navigate around the cells for a quick tour. Here is a breakdown of how to view/edit cells:

1. Each cell may be edited by hitting ENTER; toggle between cells using the arrow keys or mouse/scroller
2. When editing a cell, be sure to select "markdown" for text or "code" before writing into it
3. Each cell can be run by hitting CTRL + ENTER or the "run" button form the menu bar
4. Output from each cell will appear below; if an error occurs, please read and try to debug it(!)
5. File can be saved by hitting CTRL + "s" or file/save from the pulldown menu above

### Quick Start
This notebook will require some Python programming, which is widely used and gain enough traction to be taught in [high school][01.03] and AP Computer Science [courses][01.04].

[Jupyter][01.05] supports several different languages (R, Scala and Julia); however, Python is the most popular of them and can be used for other tasks, primarily data science and web programming.

### Exercises
If you are new to Jupyter, then please review the links below:
1. [Intro Guide (DataQuest)][01.06]
2. [Intro Guide (DataCamp)][01.07]
3. [Notebook Intro (Medium)][01.08]
4. [Intro Guide (Jupyter)][01.09]

If you are new to programming or Python, then please review the links below:
1. [Quick Start (Official)][01.10]
2. [Intro Tutorials (Real Python)][01.11]
3. [Quick Start (FCC)][01.12]

If you are new to programming or Markdown, then please review the links below:
1. [Quick Start (Github)][01.13]
2. [Quick Start Guide (Markdown)][01.14]
3. [Quick Start Tutorial (Markdown)][01.15]

[01.01]: https://jupyter.org/install
[01.02]: https://jupyter.org/jupyter-book/01/what-is-data-science.html
[01.03]: https://codehs.com/info/curriculum/intropython
[01.04]: https://code.org/educate/curriculum/high-school
[01.05]: https://jupyter.org/
[01.06]: https://www.dataquest.io/blog/jupyter-notebook-tutorial/
[01.07]: https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook
[01.08]: https://towardsdatascience.com/a-beginners-tutorial-to-jupyter-notebooks-1b2f8705888a
[01.09]: https://jupyter.org/jupyter-book/01/what-is-data-science.html
[01.10]: https://www.python.org/about/gettingstarted/
[01.11]: https://realpython.com/learning-paths/python3-introduction/
[01.12]: https://guide.freecodecamp.org/python/
[01.13]: https://guides.github.com/features/mastering-markdown/
[01.14]: https://www.markdownguide.org/getting-started/
[01.15]: https://www.markdowntutorial.com/

[02.01]: https://www.codeforamerica.org/events/national-day-of-civic-hacking-2020
[02.02]: https://github.com/walteryu/code4sac/blob/master/ndoch_2020/asset_map.PNG

[03.01]: https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/
[03.02]: https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry
[03.03]: https://github.com/python-visualization/folium/blob/master/examples/MarkerCluster.ipynb
[03.04]: https://www.jpytr.com/post/analysinggeographicdatawithfolium/
[03.05]: https://medium.com/@rohanguptha.bompally/python-data-visualization-using-folium-and-geopandas-981857948f02

[04.01]: https://gis.data.ca.gov/
[04.02]: https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20?geometry=-152.476%2C31.022%2C-85.723%2C43.235
[04.03]: https://gis.data.ca.gov/datasets/CHHSAgency::health-professional-shortage-area-primary-care?geometry=-146.864%2C31.069%2C-91.141%2C43.275
[04.04]: https://gis.data.ca.gov/datasets/CHHSAgency::health-professional-shortage-area-mental-health?geometry=-146.864%2C31.049%2C-91.141%2C43.257
[04.05]: https://gis.data.ca.gov/datasets/CHHSAgency::health-professional-shortage-area-dental?geometry=-147.022%2C31.077%2C-91.300%2C43.281
