# Automated Reports

## Coverage Report
```text
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
src/cli/__init__.py                                0      0   100%
src/cli/cli.py                                   100     27    73%   54, 62, 80-83, 120-125, 142-155, 159-160
src/core/__init__.py                               0      0   100%
src/core/models/__init__.py                        0      0   100%
src/core/models/backgammon/__init__.py             0      0   100%
src/core/models/backgammon/backgammon.py          94      2    98%   123, 125
src/core/models/dado/Dados.py                     16      0   100%
src/core/models/dado/__init__.py                   0      0   100%
src/core/models/ficha/Ficha.py                    18      0   100%
src/core/models/ficha/__init__.py                  0      0   100%
src/core/models/jugador/Jugador.py                 5      0   100%
src/core/models/jugador/__init__.py                0      0   100%
src/core/models/tablero/Tablero.py                45      0   100%
src/core/models/tablero/Tablero_Validador.py      31      1    97%   66
src/core/models/tablero/__init__.py                0      0   100%
src/pygame_ui/Tablero_UI.py                       94     48    49%   41, 46, 52-73, 79-94, 137-166, 174-178, 184-203, 207-208, 212-213
src/pygame_ui/__init__.py                          0      0   100%
src/pygame_ui/ui.py                               42     42     0%   1-53
----------------------------------------------------------------------------
TOTAL                                            445    120    73%

```

## Pylint Report
```text
************* Module main.py
main.py:1:0: F0001: No module named main.py (fatal)
************* Module test.py
test.py:1:0: F0001: No module named test.py (fatal)

```
