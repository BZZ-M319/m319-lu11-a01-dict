def main():
    """
    main program - creates some dictionaries and calls the functions
    """
    cities = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    add_cities(cities)

    cities = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    remove_cities(cities)

    cities = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    find_cities(cities)
    loop_cities(cities)
    sort_cities(cities)

def add_cities(cities):
    """
    adds two cities
    :param cities: dictionary of cities
    :return: None
    """
    # TODO: add 2500 Biel
    # TODO: add 4000 Basel
    print('add_cities:\n', cities)

def remove_cities(cities):
    """
    removes a city
    :param cities: dictionary of cities
    :return: None
    """
    # TODO: remove the city with the zip-code 8400
    print('remove_cities:\n', cities)


def find_cities(cities):
    """
    finds a city
    :param cities: dictionary of cities
    :return: None
    """
    print('find_city:')
    # TODO: print the name of the city with the zip-code 6000
    # TODO: print the zip-code of Genf
    pass


def loop_cities(cities):
    """
    prints all cities using a loop
    :param cities: dictionary of cities
    :return: None
    """
    print('loop_cities:')
    # TODO: print all cities in the list. output should be 'zip-code: name', i.e. '3000: Bern'


def sort_cities(cities):
    """
    sorts the cities by zip-code
    :param cities: dictionary of cities
    :return: None
    """
    print('sort_cities:')
    # TODO: print all cities ordered by zip-Code (descending). output should be 'name: zip-code', i.e. 'Bern: 3000'

if __name__ == '__main__':
    main()