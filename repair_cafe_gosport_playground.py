from pyRestarters import Group, Network

if __name__ == '__main__':

    repair_cafe_gosport = Group(group_id=410)
    print(repair_cafe_gosport.name)
    events = repair_cafe_gosport.events
    future_events = repair_cafe_gosport.future_events
    past_events = repair_cafe_gosport.past_events
    next_event = repair_cafe_gosport.next_event
    print(f'Next Event start at {next_event.start}')

    hampshire_repair_cafe_network = Network(network_id=7)
    print(hampshire_repair_cafe_network.name)
    print('members:')
    for group in hampshire_repair_cafe_network.groups.values():
        print(f'- {group.name}')

