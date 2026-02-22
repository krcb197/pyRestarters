# PyRestarters
Python Wrappers for the restarters.net API

## Restarters.net
[restarters.net](https://restarters.net/) is a website widely used within the Repair Community.

### Restarters API
The [API documentation](https://restarters.net/apiv2/documentation) describes the REST API which is wrapped by this package

## Usage

Currently this package supports reading data from the [restarters.net](https://restarters.net/) website which 
does not require an API key. The APIs to modify or delete data are not currently supported.


## Getting Started

### Installation

1. Install a recent version of Python 3
2. Install `pyRestarters`
   ```console
   python3 -m pip install pyRestarters
   ```
   
### Demo

The date for the next Repair Cafe Gosport Event

```python
restarters_groups = Groups()
rcg = restarters_groups.group_by_name('Repair Café Gosport')
next_rcg_event = rcg.next_event
print(f'The next Repair Café Gosport is {next_rcg_event.start:%d %b %Y}')
```

This will print a string as follows, the date will change if you rerun it
```
The next Repair Café Gosport is 14 Feb 2026
```











