from src.models.table import Table

def test_create_default_table():
    table = Table()
    assert table._length == 5
    assert table._width == 5
    assert table._grid == [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
