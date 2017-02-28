from data import locations, map_cols, map_rows

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0,0)

def map_for_print(player_position):
    adventure_map = {}
    for pos, loc in locations.iteritems():
        if pos == player_position:
            adventure_map[pos] = "you are here"
        else:
            adventure_map[pos] = loc
    return adventure_map

def print_map(player_position):
    adventure_map = map_for_print(player_position)
    for row in range(map_rows):                                     #for each row in number of rows
        for col in range(map_cols):
            print '{:*^20}'.format(adventure_map[(col, row)]),      #comma prints each column on same 'row'
        print



while True:
    location = locations[position]
    print "You are at the %s" %location

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print "to the %s is a %s" %(k, possible_location)
            valid_directions[k] = possible_position

    direction = raw_input('which direction do you want to go?\n')
    if direction in valid_directions:
        position = valid_directions[direction]
        print_map(position)
    else:
        print "that wasn't a valid direction"