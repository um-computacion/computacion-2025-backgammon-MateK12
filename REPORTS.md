# Automated Reports

## Coverage Report
```text
          Name                                                                   Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------------------------------
src/cli/__init__.py                                                        0      0   100%
src/cli/cli.py                                                           123     20    84%   66, 74-75, 148-166, 188-198
src/core/__init__.py                                                       0      0   100%
src/core/helpers/Tablero_Impresor.py                                      54      0   100%
src/core/helpers/Tablero_Inicializador.py                                 15      0   100%
src/core/helpers/__init__.py                                               0      0   100%
src/core/models/__init__.py                                                0      0   100%
src/core/models/backgammon/Backgammon_Turnos.py                           29      0   100%
src/core/models/backgammon/Estrategias/EstrategiaMovimientoComida.py      18      0   100%
src/core/models/backgammon/Estrategias/EstrategiaMovimientoNormal.py      34      0   100%
src/core/models/backgammon/Estrategias/EstrategiaUnicaFicha.py            75      1    99%   165
src/core/models/backgammon/__init__.py                                     0      0   100%
src/core/models/backgammon/backgammon.py                                  98      0   100%
src/core/models/dado/Dados.py                                             16      0   100%
src/core/models/dado/__init__.py                                           0      0   100%
src/core/models/ficha/Ficha.py                                            10      0   100%
src/core/models/ficha/__init__.py                                          0      0   100%
src/core/models/jugador/Jugador.py                                         5      0   100%
src/core/models/jugador/__init__.py                                        0      0   100%
src/core/models/tablero/Tablero.py                                        50      1    98%   70
src/core/models/tablero/Tablero_Validador.py                              60      0   100%
src/core/models/tablero/__init__.py                                        0      0   100%
src/pygame_ui/CamposUI/__init__.py                                         0      0   100%
src/pygame_ui/CamposUI/camposUI.py                                       130     15    88%   61, 150, 163-166, 170-174, 197, 222-224
src/pygame_ui/Cartel_UI/Cartel_UI.py                                      63      0   100%
src/pygame_ui/Cartel_UI/__init__.py                                        0      0   100%
src/pygame_ui/Tablero_UI/Tablero_UI.py                                   105     16    85%   65, 80-97
src/pygame_ui/Tablero_UI/__init__.py                                       0      0   100%
src/pygame_ui/__init__.py                                                  0      0   100%
src/pygame_ui/ui.py                                                      138     39    72%   87-125, 160, 176-187, 191
----------------------------------------------------------------------------------------------------
TOTAL                                                                   1023     92    91%

```

          ## Pylint Report
```text
          ************* Module pygame_ui.ui
src/pygame_ui/ui.py:26:0: C0301: Line too long (104/100) (line-too-long)
src/pygame_ui/ui.py:27:0: C0301: Line too long (104/100) (line-too-long)
src/pygame_ui/ui.py:122:0: C0301: Line too long (124/100) (line-too-long)
src/pygame_ui/ui.py:128:0: C0301: Line too long (151/100) (line-too-long)
src/pygame_ui/ui.py:139:0: C0301: Line too long (102/100) (line-too-long)
src/pygame_ui/ui.py:149:0: C0301: Line too long (115/100) (line-too-long)
src/pygame_ui/ui.py:153:0: C0301: Line too long (115/100) (line-too-long)
src/pygame_ui/ui.py:176:0: C0301: Line too long (102/100) (line-too-long)
src/pygame_ui/ui.py:38:4: R0913: Too many arguments (6/5) (too-many-arguments)
src/pygame_ui/ui.py:38:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
src/pygame_ui/ui.py:46:8: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/ui.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/ui.py:65:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/ui.py:97:37: E1101: Module 'pygame' has no 'QUIT' member (no-member)
src/pygame_ui/ui.py:98:24: E1101: Module 'pygame' has no 'quit' member (no-member)
src/pygame_ui/ui.py:124:8: E1101: Module 'pygame' has no 'quit' member (no-member)
src/pygame_ui/ui.py:136:12: W0707: Consider explicitly re-raising using 'raise NingunMovimientoPosible(e) from e' (raise-missing-from)
src/pygame_ui/ui.py:168:19: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/pygame_ui/ui.py:170:20: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/pygame_ui/ui.py:175:0: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/ui.py:10:0: W0611: Unused Ficha imported from src.core.models.ficha.Ficha (unused-import)
************* Module pygame_ui.Test_Ui
src/pygame_ui/Test_Ui.py:10:39: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Test_Ui.py:22:33: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Test_Ui.py:76:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Test_Ui.py:96:0: C0301: Line too long (118/100) (line-too-long)
src/pygame_ui/Test_Ui.py:126:0: C0301: Line too long (130/100) (line-too-long)
src/pygame_ui/Test_Ui.py:146:0: C0301: Line too long (131/100) (line-too-long)
src/pygame_ui/Test_Ui.py:155:0: C0301: Line too long (135/100) (line-too-long)
src/pygame_ui/Test_Ui.py:162:0: C0301: Line too long (134/100) (line-too-long)
src/pygame_ui/Test_Ui.py:19:4: W0221: Number of parameters was 1 in 'TestCase.setUp' and is now 2 in overriding 'Test_Ui.setUp' method (arguments-differ)
src/pygame_ui/Test_Ui.py:47:24: W0212: Access to a protected member _BackgammonUI__dados_tirados of a client class (protected-access)
src/pygame_ui/Test_Ui.py:59:41: W0613: Unused argument 'mock_flip' (unused-argument)
src/pygame_ui/Test_Ui.py:83:25: W0212: Access to a protected member _BackgammonUI__dados_tirados of a client class (protected-access)
src/pygame_ui/Test_Ui.py:100:8: W0212: Access to a protected member _BackgammonUI__dados_disponibles of a client class (protected-access)
src/pygame_ui/Test_Ui.py:157:4: E0102: method already defined line 150 (function-redefined)
src/pygame_ui/Test_Ui.py:2:0: W0611: Unused import pygame (unused-import)
src/pygame_ui/Test_Ui.py:3:0: W0611: Unused WINDOW_HEIGHT imported from src.pygame_ui.ui (unused-import)
src/pygame_ui/Test_Ui.py:3:0: W0611: Unused WINDOW_WIDTH imported from src.pygame_ui.ui (unused-import)
************* Module pygame_ui.CamposUI.Test_CampsUI
src/pygame_ui/CamposUI/Test_CampsUI.py:6:39: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:12:4: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/CamposUI/Test_CampsUI.py:15:0: C0413: Import "import unittest" should be placed at the top of the module (wrong-import-position)
src/pygame_ui/CamposUI/Test_CampsUI.py:16:0: C0413: Import "from unittest.mock import patch, MagicMock" should be placed at the top of the module (wrong-import-position)
src/pygame_ui/CamposUI/Test_CampsUI.py:17:0: C0413: Import "from src.core.enums.TipoFicha import TipoFicha" should be placed at the top of the module (wrong-import-position)
src/pygame_ui/CamposUI/Test_CampsUI.py:18:0: C0413: Import "from src.core.models.ficha.Ficha import Ficha" should be placed at the top of the module (wrong-import-position)
src/pygame_ui/CamposUI/Test_CampsUI.py:19:0: C0413: Import "from src.pygame_ui.CamposUI.camposUI import CamposUi" should be placed at the top of the module (wrong-import-position)
src/pygame_ui/CamposUI/Test_CampsUI.py:46:39: W0613: Unused argument 'mock_button' (unused-argument)
src/pygame_ui/CamposUI/Test_CampsUI.py:46:52: W0613: Unused argument 'mock_dropdown' (unused-argument)
************* Module pygame_ui.CamposUI.camposUI
src/pygame_ui/CamposUI/camposUI.py:13:0: R0902: Too many instance attributes (14/7) (too-many-instance-attributes)
src/pygame_ui/CamposUI/camposUI.py:203:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
src/pygame_ui/CamposUI/camposUI.py:199:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
src/pygame_ui/CamposUI/camposUI.py:85:8: W0201: Attribute 'select_triangulo' defined outside __init__ (attribute-defined-outside-init)
************* Module pygame_ui.Tablero_UI.Tablero_UI
src/pygame_ui/Tablero_UI/Tablero_UI.py:47:0: C0301: Line too long (116/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:115:27: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:124:0: C0301: Line too long (107/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:159:0: C0301: Line too long (108/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:207:0: C0301: Line too long (110/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:5:0: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/Tablero_UI/Tablero_UI.py:88:13: R1716: Simplify chained comparison between the operands (chained-comparison)
src/pygame_ui/Tablero_UI/Tablero_UI.py:91:13: R1716: Simplify chained comparison between the operands (chained-comparison)
src/pygame_ui/Tablero_UI/Tablero_UI.py:95:58: E0606: Possibly using variable 'text_y' before assignment (possibly-used-before-assignment)
************* Module pygame_ui.Tablero_UI.Test_Tablero_UI
src/pygame_ui/Tablero_UI/Test_Tablero_UI.py:16:39: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Test_Tablero_UI.py:22:8: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/Tablero_UI/Test_Tablero_UI.py:171:8: E1101: Module 'pygame' has no 'quit' member (no-member)
************* Module pygame_ui.Cartel_UI.Test_Cartel
src/pygame_ui/Cartel_UI/Test_Cartel.py:8:39: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Cartel_UI/Test_Cartel.py:24:0: C0301: Line too long (119/100) (line-too-long)
src/pygame_ui/Cartel_UI/Test_Cartel.py:33:0: C0301: Line too long (124/100) (line-too-long)
src/pygame_ui/Cartel_UI/Test_Cartel.py:44:0: C0301: Line too long (118/100) (line-too-long)
src/pygame_ui/Cartel_UI/Test_Cartel.py:51:0: C0301: Line too long (118/100) (line-too-long)
src/pygame_ui/Cartel_UI/Test_Cartel.py:61:0: C0301: Line too long (126/100) (line-too-long)
src/pygame_ui/Cartel_UI/Test_Cartel.py:15:8: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/Cartel_UI/Test_Cartel.py:25:25: W0212: Access to a protected member _Cartel_UI__mensaje of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:26:25: W0212: Access to a protected member _Cartel_UI__titulo of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:27:25: W0212: Access to a protected member _Cartel_UI__duracion of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:28:25: W0212: Access to a protected member _Cartel_UI__color_fondo of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:29:25: W0212: Access to a protected member _Cartel_UI__color_texto of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:52:17: W0212: Access to a protected member _Cartel_UI__dividir_mensaje of a client class (protected-access)
************* Module pygame_ui.Cartel_UI.Cartel_UI
src/pygame_ui/Cartel_UI/Cartel_UI.py:5:0: R0902: Too many instance attributes (12/7) (too-many-instance-attributes)
src/pygame_ui/Cartel_UI/Cartel_UI.py:27:4: R0913: Too many arguments (6/5) (too-many-arguments)
src/pygame_ui/Cartel_UI/Cartel_UI.py:27:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
src/pygame_ui/Cartel_UI/Cartel_UI.py:39:8: W0201: Attribute '__mensaje' defined outside __init__ (attribute-defined-outside-init)
************* Module cli.cli
src/cli/cli.py:22:0: C0301: Line too long (104/100) (line-too-long)
src/cli/cli.py:24:0: C0301: Line too long (104/100) (line-too-long)
src/cli/cli.py:37:43: W0621: Redefining name 'backgammon' from outer scope (line 195) (redefined-outer-name)
src/cli/cli.py:94:18: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/cli/cli.py:96:18: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/cli/cli.py:100:14: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/cli/cli.py:180:8: W0621: Redefining name 'dados' from outer scope (line 189) (redefined-outer-name)
src/cli/cli.py:181:14: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/cli/cli.py:21:0: W0611: Unused Ficha imported from src.core.models.ficha.Ficha (unused-import)
************* Module cli.Test_Cli
src/cli/Test_Cli.py:17:0: C0301: Line too long (104/100) (line-too-long)
src/cli/Test_Cli.py:18:0: C0301: Line too long (104/100) (line-too-long)
src/cli/Test_Cli.py:31:0: C0301: Line too long (106/100) (line-too-long)
src/cli/Test_Cli.py:13:0: W0404: Reimport 'patch' (imported line 5) (reimported)
src/cli/Test_Cli.py:120:29: C2801: Unnecessarily calls dunder method __repr__. Use repr built-in function. (unnecessary-dunder-call)
src/cli/Test_Cli.py:121:29: C2801: Unnecessarily calls dunder method __repr__. Use repr built-in function. (unnecessary-dunder-call)
src/cli/Test_Cli.py:23:0: R0904: Too many public methods (25/20) (too-many-public-methods)
src/cli/Test_Cli.py:5:0: W0611: Unused Mock imported from unittest.mock (unused-import)
src/cli/Test_Cli.py:16:0: W0611: Unused NingunMovimientoPosible imported from src.core.exceptions.NingunMovimientoPosible (unused-import)
************* Module core.exceptions.NoPuedeLiberarException
src/core/exceptions/NoPuedeLiberarException.py:1:0: C0304: Final newline missing (missing-final-newline)
************* Module core.helpers.Tablero_Inicializador
src/core/helpers/Tablero_Inicializador.py:10:0: C0301: Line too long (140/100) (line-too-long)
src/core/helpers/Tablero_Inicializador.py:5:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.helpers.Test_Tablero_impresor
src/core/helpers/Test_Tablero_impresor.py:120:0: C0304: Final newline missing (missing-final-newline)
src/core/helpers/Test_Tablero_impresor.py:5:0: W0611: Unused Tablero_Validador imported from src.core.models.tablero.Tablero_Validador (unused-import)
************* Module core.helpers.Tablero_Impresor
src/core/helpers/Tablero_Impresor.py:6:4: R0912: Too many branches (20/12) (too-many-branches)
src/core/helpers/Tablero_Impresor.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.models.backgammon.Test_Backgammon
src/core/models/backgammon/Test_Backgammon.py:15:0: C0301: Line too long (104/100) (line-too-long)
src/core/models/backgammon/Test_Backgammon.py:16:0: C0301: Line too long (104/100) (line-too-long)
src/core/models/backgammon/Test_Backgammon.py:25:0: C0301: Line too long (104/100) (line-too-long)
src/core/models/backgammon/Test_Backgammon.py:470:0: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/backgammon/Test_Backgammon.py:493:44: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/backgammon/Test_Backgammon.py:23:0: R0904: Too many public methods (56/20) (too-many-public-methods)
src/core/models/backgammon/Test_Backgammon.py:2:0: W0611: Unused Mock imported from unittest.mock (unused-import)
src/core/models/backgammon/Test_Backgammon.py:2:0: W0611: Unused patch imported from unittest.mock (unused-import)
************* Module core.models.backgammon.Backgammon_Turnos
src/core/models/backgammon/Backgammon_Turnos.py:1:0: W0611: Unused Ficha imported from src.core.models.ficha.Ficha (unused-import)
************* Module core.models.backgammon.backgammon
src/core/models/backgammon/backgammon.py:16:0: C0301: Line too long (120/100) (line-too-long)
src/core/models/backgammon/backgammon.py:37:0: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/backgammon/backgammon.py:49:0: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/backgammon/backgammon.py:63:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
src/core/models/backgammon/backgammon.py:105:0: C0301: Line too long (103/100) (line-too-long)
src/core/models/backgammon/backgammon.py:157:0: C0301: Line too long (115/100) (line-too-long)
src/core/models/backgammon/backgammon.py:61:11: C0123: Use isinstance() rather than type() for a typecheck. (unidiomatic-typecheck)
src/core/models/backgammon/backgammon.py:78:11: C0123: Use isinstance() rather than type() for a typecheck. (unidiomatic-typecheck)
src/core/models/backgammon/backgammon.py:80:16: R1716: Simplify chained comparison between the operands (chained-comparison)
src/core/models/backgammon/backgammon.py:92:8: R1703: The if statement can be replaced with 'return bool(test)' (simplifiable-if-statement)
src/core/models/backgammon/backgammon.py:92:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
src/core/models/backgammon/backgammon.py:111:8: R1720: Unnecessary "else" after "raise", remove the "else" and de-indent the code inside it (no-else-raise)
src/core/models/backgammon/backgammon.py:194:12: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
************* Module core.models.backgammon.Estrategias.EstrategiaMovimientoNormal
src/core/models/backgammon/Estrategias/EstrategiaMovimientoNormal.py:40:0: C0301: Line too long (104/100) (line-too-long)
src/core/models/backgammon/Estrategias/EstrategiaMovimientoNormal.py:73:0: C0301: Line too long (106/100) (line-too-long)
src/core/models/backgammon/Estrategias/EstrategiaMovimientoNormal.py:84:0: C0301: Line too long (110/100) (line-too-long)
src/core/models/backgammon/Estrategias/EstrategiaMovimientoNormal.py:97:0: C0304: Final newline missing (missing-final-newline)
src/core/models/backgammon/Estrategias/EstrategiaMovimientoNormal.py:7:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.models.backgammon.Estrategias.Test_Estrategia_Unica_Ficha
src/core/models/backgammon/Estrategias/Test_Estrategia_Unica_Ficha.py:123:0: C0304: Final newline missing (missing-final-newline)
************* Module core.models.backgammon.Estrategias.EstrategiaUnicaFicha
src/core/models/backgammon/Estrategias/EstrategiaUnicaFicha.py:59:0: C0301: Line too long (116/100) (line-too-long)
src/core/models/backgammon/Estrategias/EstrategiaUnicaFicha.py:106:0: C0301: Line too long (106/100) (line-too-long)
src/core/models/backgammon/Estrategias/EstrategiaUnicaFicha.py:117:0: C0301: Line too long (110/100) (line-too-long)
src/core/models/backgammon/Estrategias/EstrategiaUnicaFicha.py:175:0: C0304: Final newline missing (missing-final-newline)
src/core/models/backgammon/Estrategias/EstrategiaUnicaFicha.py:89:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module core.models.backgammon.Estrategias.EstrategiaMovimientoComida
src/core/models/backgammon/Estrategias/EstrategiaMovimientoComida.py:52:0: C0304: Final newline missing (missing-final-newline)
src/core/models/backgammon/Estrategias/EstrategiaMovimientoComida.py:9:64: W0613: Unused argument 'backgammon' (unused-argument)
src/core/models/backgammon/Estrategias/EstrategiaMovimientoComida.py:6:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.models.backgammon.Estrategias.Test_Estrategia_ficha_comida
src/core/models/backgammon/Estrategias/Test_Estrategia_ficha_comida.py:3:0: C0301: Line too long (104/100) (line-too-long)
src/core/models/backgammon/Estrategias/Test_Estrategia_ficha_comida.py:97:0: C0304: Final newline missing (missing-final-newline)
************* Module core.models.backgammon.Estrategias.Test_Estrategia_movimiento_normal
src/core/models/backgammon/Estrategias/Test_Estrategia_movimiento_normal.py:3:0: C0301: Line too long (104/100) (line-too-long)
src/core/models/backgammon/Estrategias/Test_Estrategia_movimiento_normal.py:187:0: C0304: Final newline missing (missing-final-newline)
************* Module core.models.dado.Dados
src/core/models/dado/Dados.py:17:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module core.models.tablero.Tablero
src/core/models/tablero/Tablero.py:54:0: C0301: Line too long (106/100) (line-too-long)
src/core/models/tablero/Tablero.py:70:0: C0301: Line too long (110/100) (line-too-long)
src/core/models/tablero/Tablero.py:72:0: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/tablero/Tablero.py:77:8: R1720: Unnecessary "else" after "raise", remove the "else" and de-indent the code inside it (no-else-raise)
src/core/models/tablero/Tablero.py:2:0: W0611: Unused TipoFicha imported from src.core.enums.TipoFicha (unused-import)
************* Module core.models.tablero.Test_Tablero
src/core/models/tablero/Test_Tablero.py:8:0: W0611: Unused patch imported from unittest.mock (unused-import)
************* Module core.models.tablero.Test_Tablero_Validador
src/core/models/tablero/Test_Tablero_Validador.py:224:0: C0301: Line too long (143/100) (line-too-long)
src/core/models/tablero/Test_Tablero_Validador.py:225:0: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/tablero/Test_Tablero_Validador.py:230:0: C0301: Line too long (146/100) (line-too-long)
src/core/models/tablero/Test_Tablero_Validador.py:124:4: E0102: method already defined line 112 (function-redefined)
src/core/models/tablero/Test_Tablero_Validador.py:5:0: W0611: Unused MovimientoNoJustoParaGanar imported from src.core.exceptions.MovimientoNoJustoParaGanar (unused-import)
************* Module core.models.tablero.Tablero_Validador
src/core/models/tablero/Tablero_Validador.py:62:42: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/tablero/Tablero_Validador.py:64:42: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/tablero/Tablero_Validador.py:129:0: C0301: Line too long (109/100) (line-too-long)
src/core/models/tablero/Tablero_Validador.py:135:0: C0301: Line too long (111/100) (line-too-long)
src/core/models/tablero/Tablero_Validador.py:61:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
src/core/models/tablero/Tablero_Validador.py:48:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
src/core/models/tablero/Tablero_Validador.py:49:52: W0613: Unused argument 'triangulo_origen' (unused-argument)
src/core/models/tablero/Tablero_Validador.py:127:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
src/core/models/tablero/Tablero_Validador.py:115:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
************* Module core.models.jugador.Jugador
src/core/models/jugador/Jugador.py:1:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.interfaces.EstrategiaMovible
src/core/interfaces/EstrategiaMovible.py:8:0: C0304: Final newline missing (missing-final-newline)
src/core/interfaces/EstrategiaMovible.py:8:8: W0107: Unnecessary pass statement (unnecessary-pass)
src/core/interfaces/EstrategiaMovible.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.interfaces.PuedeHacerMovimiento
src/core/interfaces/PuedeHacerMovimiento.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.interfaces.TrianguloValidaciones
src/core/interfaces/TrianguloValidaciones.py:7:4: E0213: Method 'seleccion_triangulo_valida' should have "self" as first argument (no-self-argument)
src/core/interfaces/TrianguloValidaciones.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.interfaces.JuegoInterfazMovimientos
src/core/interfaces/JuegoInterfazMovimientos.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.interfaces.EstrategiasPuedeMover
src/core/interfaces/EstrategiasPuedeMover.py:7:0: C0304: Final newline missing (missing-final-newline)
src/core/interfaces/EstrategiasPuedeMover.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
src/core/interfaces/EstrategiasPuedeMover.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.interfaces.DadosValidaciones
src/core/interfaces/DadosValidaciones.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.interfaces.CartelUI
src/core/interfaces/CartelUI.py:7:0: C0301: Line too long (110/100) (line-too-long)
src/core/interfaces/CartelUI.py:12:0: C0304: Final newline missing (missing-final-newline)
src/core/interfaces/CartelUI.py:7:4: R0913: Too many arguments (6/5) (too-many-arguments)
src/core/interfaces/CartelUI.py:7:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
************* Module core.enums.__init__
src/core/enums/__init__.py:1:0: R0801: Similar lines in 2 files
==core.models.backgammon.Estrategias.EstrategiaMovimientoNormal:[79:97]
==core.models.backgammon.Estrategias.EstrategiaUnicaFicha:[112:140]
        return tablero.validador.se_pasa_del_tablero(
            Ficha(tipo), triangulo_destino, triangulo_origen, tablero.tablero
        )

    def _es_movimiento_ganar(self, tipo: int, triangulo_destino: int, triangulo_origen: int, tablero) -> bool:
        '''Verifica si el movimiento es para ganar
        Parametros:
            tipo (int): Tipo de ficha
            triangulo_destino (int): Triángulo destino del movimiento
            triangulo_origen (int): Triángulo origen del movimiento
            tablero: El tablero de juego
        '''
        puede_ganar = tablero.validador.puede_ganar(
            Ficha(tipo), triangulo_destino, triangulo_origen
        )
        no_se_pasa = not self._se_pasa_tablero(tipo, triangulo_destino, triangulo_origen, tablero)
        return puede_ganar and no_se_pasa


    def _obtener_triangulos_validos(self, tipo: int, movimiento: int, tablero) -> list[int]:
        """Retorna lista de triángulos desde donde se puede mover con el movimiento dado
        Parametros:
            tipo (int): Tipo de ficha
            movimiento (int): Valor del dado
            tablero: El tablero de juego
        Retorna:
            list[int]: Lista de triángulos válidos (puede estar vacía)
        """ (duplicate-code)
src/core/enums/__init__.py:1:0: R0801: Similar lines in 2 files
==core.models.backgammon.Estrategias.Test_Estrategia_ficha_comida:[42:52]
==core.models.backgammon.Estrategias.Test_Estrategia_movimiento_normal:[96:107]
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]

        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_no_puede_mover_pared_completa_bloqueo(self):
        """Pared completa bloquea todos los movimientos""" (duplicate-code)
src/core/enums/__init__.py:1:0: R0801: Similar lines in 2 files
==core.models.backgammon.Estrategias.EstrategiaMovimientoNormal:[52:59]
==core.models.backgammon.Estrategias.EstrategiaUnicaFicha:[148:156]
            triangulo_destino = (
                triangulo + movimiento
                if tipo == TipoFicha.NEGRA.value
                else triangulo - movimiento
            )

            # Verificar si se pasa del tablero
            if self._se_pasa_tablero(tipo, triangulo_destino, triangulo, tablero): (duplicate-code)

-----------------------------------
Your code has been rated at 9.10/10


```
          