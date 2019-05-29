# Code for Sacramento - Neighborhood Portal Project
![Sac311](https://github.com/walteryu/code4sac/blob/master/sac311/images/sac311_logo.png)

### City of Sacramento - 311 Service Call Analysis
Code for Sacramento is develop a neighborhood portal application; as a result, this notebook evaluates the City of Sacramento 311 service call dataset for insights and trends which may be helpful in developing useful features. This notebook will focus on an initial analysis and identifying potential issues related to users and their neighborhoods.  

### Conjecture  
Per discussion with City of Sacramento staff, 311 service calls are a relatively stable source for identify potential issues/needs of neighborhoods. Included are time and location data which will be useful for identifying trends.  

### Findings  
1. Conventional statistical and machine learning methods were not a good fit for analyzing service call data due to its highly categorial nature; almost all variables were categorical with exception of time/location data.  
2. Exploratory data analysis and logistic regression were used to confirm this finding; spatial analysis was used to yield better results.  
3. Clustering and density plots were developed in the GeoDa software application to identify natural concentrations of service calls by zipcode.  

### Dataset
311 service call dataset from City of Sacramento; summary statistics for the full and partial datasets are listed below. The data is available in geospatial, tabular or API format; the tabular format is used for this analysis to identify important neighborhoods and trends which are relevant to developing the application.  

* [311 Service Call Dataset](https://data.cityofsacramento.org/datasets/08794a6695b3483f889e9bef122517e9_0)

### Installation
1. Notebook is written in R markdown, so be sure that R Studio is installed then clone this repository.
2. Load notebook in R Studio, run/download dependencies.
3. For spatial analysis, download and start the GeoDa [spatial analysis tool](https://geodacenter.github.io/download.html) which was developed by the University of Chicago [Spatial Data Science Program](https://spatial.uchicago.edu/).

### Methodology
1. Exploratory data analysis (EDA) and model fits showed that spatial and temporal analysis would be more appropriate methods of analysis.
2. As a result, spatial analysis with R and GeoDa were used to identify trends.
3. Findings are documented within the notebook; additional analysis was completed in GeoDa.

### Citations
1. Spatial Data Science with R [textbook](https://rspatial.org/)
2. GeoDa Spatial Analysis [software](https://geodacenter.github.io/index.html)

### Spatial Analysis
GeoDa is a GUI-based tool which allows users to complete spatial analysis without coding in R or Python. As a result, it is a good analysis tool to create reproducible work with a minimal barrier to entry for the audience. Software installation can be completed on their website (see citations) without executable programs for each major OS.  

Initial plot was completed using a scatterplot of 5k service locations on a basemap as shown below; service calls (shown in green) are clustered in the downtown and Pocket neighborhood areas with smaller clusters in other neighborhoods:

**Figure 1 - Scatterplot of 311 Service Calls (5k Records in Green)**
![5k_plot](https://github.com/walteryu/code4sac/blob/master/sac311/images/sac311_5k_plot.png)

Next, a [KNN cluster](https://en.wikipedia.org/wiki/K-means_clustering) plot was created based on zipcode and confirmed the initial clustering identified in the scatterplot. Again, larger clusters of calls (shown in shades of blue/green) were observed within the downtown and Pocket neighborhood areas:

**Figure 2 - KNN Cluster Plot of 311 Service Calls (5k Records in Green)**
![5k_zip_kmeans](https://github.com/walteryu/code4sac/blob/master/sac311/images/sac311_5k_zip_kmeans.png)
