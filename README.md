# Data-Anyalytics-Project

## H2Woah!

### Collaborators
* [Chaitanya Birla](https://github.com/chaitanyabirla)  (Reg No 22112312)
* [Kanishk Saleria](https://github.com/kanishksaleria)  (Reg No 22112317)
* [Kedhar Krishhnan](https://github.com/Kedhar-K) (Reg No 22112319)
* [Aditya Pratap Singh](https://github.com/aditya22112303) (Reg No 22112303)

### Description
`H2Woah!` is a data-driven exploration project focused on the water landscapes of four distinct states: Kerala, Madhya Pradesh, Himachal Pradesh, and Uttarakhand. Leveraging the power of Django, our web application is designed to provide a comprehensive analysis of water bodies based on the dataset sourced from the water body survey published in 2023 by data.gov.in.

### Goals:
`H2Woah!` aims to contribute to the understanding of water ecosystems by investigating the distribution of water bodies in specific states and examining the influence of urbanization on water resources.

### Features:
* **Data Tab:**
  Explore the raw dataset in the 'Data' tab, offering a transparent view of the information extracted from the authoritative source.

* **EDA Tab (Exploratory Data Analysis):**
  Immerse yourself in the 'EDA' tab, where we've crafted customizable and interactive exploratory data visualizations. Uncover patterns, relationships, and trends to better understand the distribution of water   bodies in each state.

* **Descriptive Statistics Tab:**
In the 'Descriptive Statistics' tab, dive deep into numerical insights derived from the dataset. Gain a nuanced understanding of how factors such as urbanization impact the water landscape, as we present key statistical summaries for comprehensive analysis.

* **Profile Tab**
A comprehensive profile of the data and the analysis done. Created using ydata-profiling


### Data Source:
The project relies on data.gov.in's water body survey published in 2023, ensuring reliability and credibility in our analysis.

### Installation Procedure:
* Download the folder from Github and store it in a folder
* In the parent folder create a virtual environment
* In the environment pip install the following dependencies: pandas 2.0.3, Django 5.0, pydantic 2.5.2, ydata-profiling 4.6.2, seaborn 0.12.2, plotly 5.18.0, matplotlib 3.7.3 (It is imperative that pydantic is installed before ydata-profiling)
* Change the directory to the folder that contains manage.py
* In the terminal execute the command: python manage.py runserver
* If that does not work try: python3 manage.py runserver

### User Guide:
* In the first page select the state to be analysed from the dropdown menu
* Click the "Go!" button
* Click the tab to be viewed
* To be noted that the predict tab does not work.

