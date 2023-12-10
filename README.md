# Rideshare saftey

## Topic

For this First Project I intend on developing safety rating predictions for taxi and ride-share trips in New York City (NYC) based on crime data analytics. My father had a second job in as a Taxi driver to make ends meet while he was in the military. Despite what they say about pay and the service, it was never great. This is especially true for those with families. My father did it both in New York and Illinois. It was dangerous picking up strangers in the middle of the night then, and still is now.

## Business Problem

The objective is to provide taxi and ride-share drivers with a safety score for potential passenger pickup locations, drop off locations, and times, thereby alerting them to the potential risk of crime. This can hopefully help people to mitigate at least some risk and return to the loved ones safely.

## Datasets

For this project I chose two datasets. The datasets to be use for this project will be the NYC TLC Trip Record Data, which encompasses both taxi and ride-share rides, and the NYPD Crime Reporting Data. The NYC open-data site has many datasets available for use with respect to crime and were not intuitive, at least not at first. Crime reporting will convey all crimes reported, whereas arrest data will leave out a potentially large subset of crimes committed. Many of the other sets were surrounding other specific crimes such as murder and hate crime,as these are subsets of crime in general, I will focus on all crime. 

## Methods

To achieve the desired safety rating predictions, a combination, or even a series, of regression algorithms and/or classification methods will be employed. The regression algorithms will be utilized to predict safety ratings on a scale of 1 to 5, but this scale may change. For the classification methods I was considering the categorization trips as either safe or unsafe. Additionally, I have also considered the potential implementation of random forest and neural networks. This will allow for the consideration of non-linear relationships within the data, which my initial thought is highly likely given the variance in crime type and severity, and the type of transit.

## Ethical Considerations

Several ethical considerations must be taken into account throughout the development of this project. One potential concern is the possibility of bias against certain neighborhoods. It is crucial to ensure that the predictive models do not unfairly discriminate against specific areas or communities. This may or may not prove to be difficult. It may also show deficits in policing or public services. Transparency is also of utmost importance, particularly in regards to the data inputs and the determinations made in assigning safety ratings. It is essential to provide clear explanations and justifications for the ratings generated. 

## Challenges

There are several challenges that need to be addressed in order to successfully develop safety rating predictions for taxi and ride-share trips. One such challenge is linking precise locations between the NYC TLC Trip Record Data and the NYPD Crime Data. Accurate Geo-location matching is crucial for the analysis and prediction of crime risk. Not everything is neatly aligned with coordinates, so grid mapping may need to be implemented. This may assist with ethical implications as well. Another challenge involves defining safety labels for model training. It is necessary to establish clear criteria for determining whether a trip is safe or unsafe. Not all crime may a ride-share trip dangerous. This view is narrow as it does not focus on other mitigating factors of driver danger such as weather, fatigue, road conditions, and traffic to name a few.

## References

Research papers on crime forecasting and risk modeling will be consulted. These papers will likely provide valuable insights and methodologies for predicting crime risk. Additionally, examples of crime data visualizations and analyses will be examined to gain a better understanding of effective ways to present the safety ratings to taxi and ride-share drivers. Furthermore, papers on bias in algorithmic systems will be reviewed to ensure that the predictive models are fair and unbiased.


## Data Sources

NYC TLC Trip Record Data:
https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

NYPD Complaint Crime Data Current (YTD): 
https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i
