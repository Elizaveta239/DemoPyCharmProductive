"""

Split view with tests and source code

- Visual integration for tests
- Autorun tests (configuring timeout)
- Visual code coverage (exists for any Run configuration, useful for tests)

"""

EXPECTED = 'Hello Larry my name is Mary'


def test_01():
    from fortytwo.s00_navigation import main
    assert EXPECTED == main()


def test_02():
    from fortytwo.s02_reformat_code import main
    assert EXPECTED == main()


def test_03():
    from fortytwo.s03_generate_imports import main
    assert EXPECTED == main()


def test_04():
    from fortytwo.s05_refactorings import main
    assert EXPECTED == main()


def test_05():
    from fortytwo.s06_parameters_correct import main
    assert EXPECTED == main()
