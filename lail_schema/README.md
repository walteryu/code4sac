# Latin American Indigenous Languages (LAIL) in CA

![LAIL](https://github.com/walteryu/code4sac/blob/master/lail_schema/images/lail_schema.png)

### 

This repository contains the initial data model/schema for the LAIL in CA App project which was presented at the [Code for Sacramento](https://codeforsacramento.org/) weekly meetup in June 2019. The project supports the CalEPA Race and Equity project per citation in the section below. This schema is intended to normalize data currently documented in spreadsheets into a machine-readable format

### Objectives

The project objectives are as follows:

1. Build data schema, gather data and research on “communities where indigenous languages from Latin America are aggregated” in CA
2. Populate data (base) and publish datasets, documentation, metadata, etc.
3. Engage with others to improve the data resources
4. Build or find interface(s) that use this data to integrate with other datasets to convey better information, answer management questions, etc.

### Methodology

This initial schema assumes Latin American languages to be the primary model entity with relationships to Latin American and US Regions as follows:

1. Languages have many-to-many relationships with Latin American and US regions, so joint tables need to be added; schema currently shows one-to-many relationships.
2. Additional tables attributes will be added as information gathering progresses; specifically, Latin American countries and US counties are likely lookup tables which will be needed and connected to the regions tables.
3. Additional data attributes will be added as information gathering progresses; specifically, they will be added with additional research and field interviews.

### Installation

Initial database schema has been created using [MySQL Workbench](https://www.mysql.com/products/workbench/) as a starting point to develop into an actual database once project requirements, field data collection and information gathering is further along. Installation steps are as follows:

1. Download and install the MySQL Workbench from the [website](https://dev.mysql.com/downloads/workbench/)
2. Clone this repository and open the .mwb file to view the schema
3. Images of the model may be exported using options in the file tab

### Citations

1. LAIL Project [Presentation](https://docs.google.com/presentation/d/1hciMUyJdT-u6d4VA6AetnbkaosuQFIxMqpMa9P-simI/edit?usp=sharing) - Project vision, objectives and next steps.
2. CalEPA Race and Equity Project [Presentation](https://docs.google.com/presentation/d/12iTLCcX2qJdTxPP6yveGo46zU45V1huZCJaISqXlAew/edit?usp=sharing) - Project overview and data visualizations.
