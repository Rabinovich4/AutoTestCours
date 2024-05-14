from pytest import mark


@mark.dev
def test_run(chek_fixture):
    assert chek_fixture == '1'
