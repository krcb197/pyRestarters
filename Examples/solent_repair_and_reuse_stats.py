"""
An example of using pyRestarters plot the cumulative statistics for multiple repair groups
"""
from dataclasses import dataclass, asdict
import datetime
from collections.abc import Iterator

import pandas as pd
import matplotlib.pyplot as plt

from pyRestarters import Groups
from pyRestarters.data_model import Statistics

@dataclass
class EventSummary(Statistics):
    group: str
    date: datetime.date


if __name__ == '__main__':
    restarters_groups = Groups()
    rcg = restarters_groups.group_by_name('Repair Café Gosport')
    rcp = restarters_groups.group_by_name('Repair Cafe Portchester')
    rct = restarters_groups.group_by_name('Repair Café Titchfield')

    def event_summarys() -> Iterator[EventSummary]:
        for group in [rcg,rcp,rct]:
            for event in group.past_events.values():
                yield EventSummary(group=group.name,
                                   date=event.start.date(),
                                   **asdict(event.statistics))

    srr_event_summary = list(event_summarys())
    srr_event_summary_df = pd.DataFrame(srr_event_summary)

    fig, all_ax = plt.subplots(figsize=(12, 6), nrows=1, ncols=3)
    for ax, key, y_label in zip(all_ax,
                  ["fixed_devices", "co2_total", "waste_total"],
                  ["Cumulative Items Fixed",
                   "Cumulative CO2 Emissions Prevented",
                   "Cumulative Waste Emissions Prevented"]):
        # Create one column per repair cafe
        pivot = (
            srr_event_summary_df.pivot(index="date", columns="group", values=key)
            .fillna(0)
            .sort_index()
        )
        # Calculate cumulative totals
        cumulative = pivot.cumsum()
        cumulative.plot.area(ax=ax)
        ax.set_xlabel("Date")
        ax.set_ylabel(y_label)
        ax.legend(title="Repair Cafe")

    plt.tight_layout()
    plt.suptitle('KPIs for Solent Repair and Reuse')
    plt.show()

