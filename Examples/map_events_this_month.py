"""
An example of using pyRestarters to map all the events due in the UK this month
"""
import datetime
from itertools import chain

import geopandas as gpd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from shapely.geometry import Point

from pyRestarters import Groups, Group

from datetime import datetime, timedelta

now = datetime.now()

# Start of month
start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

# Start of next month
if now.month == 12:
    start_of_next_month = now.replace(
        year=now.year + 1,
        month=1,
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )
else:
    start_of_next_month = now.replace(
        month=now.month + 1,
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )

# End of month (last microsecond before next month)
end_of_month = start_of_next_month - timedelta(microseconds=1)

if __name__ == "__main__":

    # plot a map of the UK
    url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
    world = gpd.read_file(url)
    uk = world[world["name"] == "United Kingdom"]
    fig, ax = plt.subplots(figsize=(6, 8))
    uk.plot(
        ax=ax,
        edgecolor="black",
        facecolor="none",
        linewidth=1
    )
    ax.set_title("Locations of Repair Cafe Events this Month")
    ax.set_axis_off()
    plt.show()

    # go through all the groups in the restarters.net data and find:
    # UK groups - tag == 5
    # Events this month for those UK groups
    restarters_groups = Groups()

    # function to filter if a group has the UK tag
    tags = restarters_groups.group_tags
    def is_uk_group(group: Group) -> bool:
        tags = group.tags
        for tag in tags:
            if tag.id == 5:
                return True
        return False

    # The filtering takes the full list groups, find all the UK groups and then chains together
    # the events before filtering based on this month
    uk_groups = filter(is_uk_group, restarters_groups)
    events_this_month = chain.from_iterable(group.events_in_daterange(start=start_of_month, end=end_of_month).values() for group in uk_groups)

    gdf_points = gpd.GeoDataFrame(
        geometry=[Point(event.coordinates.longitude, event.coordinates.latitude) for event in events_this_month],
        crs="EPSG:4326"  # WGS84 lon/lat
    )

    gdf_points.plot(
        ax=ax,
        color="green",
        markersize=2
    )
