from src.models.table import Table

def test_create_default_table():
    table = Table()
    assert table._length == 5
    assert table._width == 5
    assert table._grid == [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]

def test_create_table_length_2_width_3():
    table = Table(2,3)
    assert table._length == 2
    assert table._width == 3
    assert table._grid == [[-1,-1,-1],[-1,-1,-1]]

def test_table_set_letter_Y_in_3rd_column_5th_row():
    table = Table()
    table.set(2,4, 'Y')
    assert table._grid == [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,'Y',-1,-1]]

def test_table_get_2nd_column_1_row():
    table = Table()
    table.set(1,0, 'Y')
    assert table.get(1,0) == 'Y'
    assert table._grid == [[-1,'Y',-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
