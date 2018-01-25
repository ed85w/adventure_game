from data import locations, map_cols, map_rows

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0,0)
posessions = []


def map_for_print(player_position):
    adventure_map = {}
    for pos, loc in locations.iteritems():
        if pos == player_position:
            adventure_map[pos] = "you are here"
        else:
            adventure_map[pos] = loc[0]
    return adventure_map


def print_map(player_position):
    adventure_map = map_for_print(player_position)
    for row in range(map_rows):                                     #for each row in number of rows
        for col in range(map_cols):
            print '{:*^20}'.format(adventure_map[(col, row)]),      #comma prints each column on same 'row'
        print


def collect_item(player_position):
    if locations[player_position][2]=="Nothing":
        print "Nothing to collect!"
    else:
        posessions.append(locations[player_position][2])
        print "You have picked up %s" %locations[player_position][2]
        locations[player_position][2] = "Nothing"

def print_posessions(posessions):
    if len(posessions) > 1:
        item_list = " and ".join([str(p) for p in posessions])
        print "You are holding " + item_list
    else:
        print "You are holding " + posessions[0]


while True:
    location = locations[position]
    print "You are at the %s, %s, at the %s there is %s" %(location[0], location[1], location[0], location[2])
    if posessions: #if not empty
        print_posessions(posessions)
    else:
        print "You are holding nothing"
    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print "to the %s is a %s" %(k, possible_location[0])
            valid_directions[k] = possible_position

    if raw_input("Pick up the thing? (y/n)").lower() == "y":
        collect_item(position)
    direction = raw_input('which direction do you want to go?\n')
    if direction in valid_directions:
        position = valid_directions[direction]
        print_map(position)
    else:
        print "that wasn't a valid direction"