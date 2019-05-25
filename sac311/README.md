# Code for Sacramento - Neighborhood Portal Project

![Sac311](https://github.com/walteryu/code4sac/blob/master/sac311/sac311.png)

### City of Sacramento - 311 Service Call Analysis

Code for Sacramento is develop a neighborhood portal application; as a result, this notebook evaluates the City of Sacramento 311 service call dataset for insights and trends which may be helpful in developing useful features. This notebook will focus on an initial analysis and identifying potential issues related to users and their neighborhoods.  

### Dataset

311 service call dataset from City of Sacramento; summary statistics for the full and partial datasets are listed below. The data is available in geospatial, tabular or API format; the tabular format is used for this analysis to identify important neighborhoods and trends which are relevant to developing the application.  

City of Sacramento 311 [Service Call Dataset](https://data.cityofsacramento.org/datasets/08794a6695b3483f889e9bef122517e9_0)

### Methodology
1. Exploratory data analysis (EDA) and model fits showed that spatial and temporal analysis would be more appropriate methods of analysis.
2. As a result, spatial analysis with R and GeoDa were used to identify trends.
3. Findings are documented within the notebook; additional analysis was completed in GeoDa.

### Installation
1. Notebook is written in R markdown, so be sure that R Studio is installed then clone this repository.
2. Load notebook in R Studio, run/download dependencies.
3. For spatial analysis, download and start the GeoDa [spatial analysis tool](https://geodacenter.github.io/download.html) which was developed by the University of Chicago [Spatial Data Science Program](https://spatial.uchicago.edu/).

### Citations

1. Spatial Data Science with R [textbook](https://rspatial.org/)
2. GeoDa Spatial Analysis [software](https://geodacenter.github.io/index.html)
