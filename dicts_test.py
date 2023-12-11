import dicts


def test_add(monkeypatch, capsys):
    cities = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    dicts.add_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "add_cities:\n {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur', '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano', '2500': 'Biel', '4000': 'Basel'}\n"


def test_remove(monkeypatch, capsys):
    cities = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    dicts.remove_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "remove_cities:\n {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}\n"


def test_find(monkeypatch, capsys):
    cities = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    dicts.find_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "find_city:\nLuzern\n1200\n"


def test_loop(monkeypatch, capsys):
    cities = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    dicts.loop_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "loop_cities:\n8000: Zürich\n1200: Genf\n1000: Lausanne\n3000: Bern\n8400: Winterthur\n6000: Luzern\n9000: St. Gallen\n6900: Lugano\n"


def test_sort(monkeypatch, capsys):
    cities = {'8000': 'Zürich', '1200': 'Genf', '1000': 'Lausanne', '3000': 'Bern', '8400': 'Winterthur',
              '6000': 'Luzern', '9000': 'St. Gallen', '6900': 'Lugano'}
    dicts.sort_cities(cities)
    captured = capsys.readouterr()
    assert captured.out == "sort_cities:\nSt. Gallen: 9000\nWinterthur: 8400\nZürich: 8000\nLugano: 6900\nLuzern: 6000\nBern: 3000\nGenf: 1200\nLausanne: 1000\n"
