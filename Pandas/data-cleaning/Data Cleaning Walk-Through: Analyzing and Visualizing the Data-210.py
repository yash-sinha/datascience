## 3. Finding Correlations With the r Value ##

correlations = combined.corr()
correlations = correlations.loc[:,["sat_score"]]
correlations.head()

## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt
combined.plot.scatter(x="total_enrollment", y="sat_score")
plt.show()

## 6. Exploring Schools With Low SAT Scores and Enrollment ##

low_enrollment = combined[(combined["total_enrollment"] < 1000) & 
                          (combined["sat_score"] <1000)]
low_enrollment["School Name"]

## 7. Plotting Language Learning Percentage ##

combined.plot.scatter(x= "ell_percent", y="sat_score")

## 9. Mapping the Schools With Basemap ##

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)
#zorder=2 to plot the points on top of the rest of the map
m.scatter(combined["lon"].tolist(), combined["lat"].tolist(), s=20, latlon = True, zorder = 2)
plt.show()

## 10. Plotting Out Statistics ##

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)
#zorder=2 to plot the points on top of the rest of the map
m.scatter(combined["lon"].tolist(), combined["lat"].tolist(),
          s=20, latlon = True, zorder = 2,
          c = combined["ell_percent"], cmap = "summer")
plt.show()

## 11. Calculating District-Level Statistics ##

import numpy as np
g = combined.groupby("school_dist") #returns groupby object
districts = g.agg(np.mean) #returns dataframe
districts.reset_index(inplace = True) #returns void
districts.head()

## 12. Plotting Percent Of English Learners by District ##

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)
#zorder=2 to plot the points on top of the rest of the map
m.scatter(districts["lon"].tolist(), districts["lat"].tolist(),
          s=50, latlon = True, zorder = 2,
          c = districts["ell_percent"], cmap = "summer")
plt.show()