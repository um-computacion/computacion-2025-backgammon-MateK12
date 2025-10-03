# Automated Reports

## Coverage Report
```text
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
src/cli/__init__.py                                0      0   100%
src/cli/cli.py                                   108     30    72%   59, 67, 85-88, 125-130, 149-162, 166-172
src/core/__init__.py                               0      0   100%
src/core/helpers/Tablero_Inicializador.py         15      0   100%
src/core/models/__init__.py                        0      0   100%
src/core/models/backgammon/__init__.py             0      0   100%
src/core/models/backgammon/backgammon.py          83      2    98%   123, 125
src/core/models/dado/Dados.py                     16      0   100%
src/core/models/dado/__init__.py                   0      0   100%
src/core/models/ficha/Ficha.py                    18      0   100%
src/core/models/ficha/__init__.py                  0      0   100%
src/core/models/jugador/Jugador.py                 5      0   100%
src/core/models/jugador/__init__.py                0      0   100%
src/core/models/tablero/Tablero.py                45      0   100%
src/core/models/tablero/Tablero_Validador.py      31      1    97%   66
src/core/models/tablero/__init__.py                0      0   100%
src/pygame_ui/__init__.py                          0      0   100%
src/pygame_ui/ui.py                              125    125     0%   1-155
----------------------------------------------------------------------------
TOTAL                                            446    158    65%

```

## Pylint Report
```text
************* Module pygame_ui.ui
src/pygame_ui/ui.py:26:0: C0301: Line too long (155/100) (line-too-long)
src/pygame_ui/ui.py:38:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/ui.py:41:18: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/ui.py:50:51: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/ui.py:96:48: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/ui.py:112:12: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/ui.py:134:0: C0301: Line too long (102/100) (line-too-long)
src/pygame_ui/ui.py:142:0: C0301: Line too long (111/100) (line-too-long)
src/pygame_ui/ui.py:144:0: C0301: Line too long (112/100) (line-too-long)
src/pygame_ui/ui.py:153:0: C0301: Line too long (114/100) (line-too-long)
src/pygame_ui/ui.py:25:0: R0902: Too many instance attributes (9/7) (too-many-instance-attributes)
src/pygame_ui/ui.py:26:4: R0913: Too many arguments (7/5) (too-many-arguments)
src/pygame_ui/ui.py:26:4: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
src/pygame_ui/ui.py:26:22: W0621: Redefining name 'backgammon' from outer scope (line 148) (redefined-outer-name)
src/pygame_ui/ui.py:26:64: W0621: Redefining name 'camposUi' from outer scope (line 150) (redefined-outer-name)
src/pygame_ui/ui.py:26:105: W0621: Redefining name 'cartel_error' from outer scope (line 152) (redefined-outer-name)
src/pygame_ui/ui.py:26:128: W0621: Redefining name 'cartel_victoria' from outer scope (line 153) (redefined-outer-name)
src/pygame_ui/ui.py:27:8: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/ui.py:39:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/ui.py:39:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
src/pygame_ui/ui.py:48:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/ui.py:99:33: E1101: Module 'pygame' has no 'QUIT' member (no-member)
src/pygame_ui/ui.py:107:8: E1101: Module 'pygame' has no 'quit' member (no-member)
src/pygame_ui/ui.py:117:15: W0718: Catching too general exception Exception (broad-exception-caught)
src/pygame_ui/ui.py:100:20: W0238: Unused private member `BackgammonUI.__running` (unused-private-member)
src/pygame_ui/ui.py:100:20: W0201: Attribute '__running' defined outside __init__ (attribute-defined-outside-init)
src/pygame_ui/ui.py:6:0: W0611: Unused IJuegoInterfazDados imported from src.core.interfaces.JuegoInterfazDados (unused-import)
src/pygame_ui/ui.py:10:0: W0611: Unused Ficha imported from src.core.models.ficha.Ficha (unused-import)
************* Module pygame_ui.CamposUI.Test_CampsUI
src/pygame_ui/CamposUI/Test_CampsUI.py:11:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:36:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:38:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:52:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:64:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:74:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/Test_CampsUI.py:96:0: C0304: Final newline missing (missing-final-newline)
src/pygame_ui/CamposUI/Test_CampsUI.py:8:4: W0221: Number of parameters was 1 in 'TestCase.setUp' and is now 3 in overriding 'TestCampsUI.setUp' method (arguments-differ)
src/pygame_ui/CamposUI/Test_CampsUI.py:14:8: C0415: Import outside toplevel (src.pygame_ui.CamposUI.camposUI.CamposUi) (import-outside-toplevel)
src/pygame_ui/CamposUI/Test_CampsUI.py:19:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:21:8: W0212: Access to a protected member _CamposUi__crear_elementos of a client class (protected-access)
src/pygame_ui/CamposUI/Test_CampsUI.py:25:29: W0212: Access to a protected member _CamposUi__text_triangulo of a client class (protected-access)
src/pygame_ui/CamposUI/Test_CampsUI.py:26:29: W0212: Access to a protected member _CamposUi__text_dado of a client class (protected-access)
src/pygame_ui/CamposUI/Test_CampsUI.py:27:29: W0212: Access to a protected member _CamposUi__text_turno of a client class (protected-access)
src/pygame_ui/CamposUI/Test_CampsUI.py:19:39: W0613: Unused argument 'mock_button' (unused-argument)
src/pygame_ui/CamposUI/Test_CampsUI.py:19:52: W0613: Unused argument 'mock_dropdown' (unused-argument)
src/pygame_ui/CamposUI/Test_CampsUI.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:33:8: W0212: Access to a protected member _CamposUi__crear_elementos of a client class (protected-access)
src/pygame_ui/CamposUI/Test_CampsUI.py:34:8: W0212: Access to a protected member _CamposUi__crear_elementos of a client class (protected-access)
src/pygame_ui/CamposUI/Test_CampsUI.py:42:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:47:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:50:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:59:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:62:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:70:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:82:12: W0212: Access to a protected member _CamposUi__crear_elementos of a client class (protected-access)
src/pygame_ui/CamposUI/Test_CampsUI.py:86:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:88:16: W0212: Access to a protected member _CamposUi__get_text_turno of a client class (protected-access)
src/pygame_ui/CamposUI/Test_CampsUI.py:90:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/Test_CampsUI.py:92:16: W0212: Access to a protected member _CamposUi__get_text_turno of a client class (protected-access)
************* Module pygame_ui.CamposUI.camposUI
src/pygame_ui/CamposUI/camposUI.py:26:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:53:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:58:21: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:59:20: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:60:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:62:56: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:67:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:68:32: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:79:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:87:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:91:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:105:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:108:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:110:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:113:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:115:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:118:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:120:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:121:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:128:58: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:145:35: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:146:31: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/CamposUI/camposUI.py:9:0: R0902: Too many instance attributes (14/7) (too-many-instance-attributes)
src/pygame_ui/CamposUI/camposUI.py:28:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/camposUI.py:31:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/camposUI.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/camposUI.py:42:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/camposUI.py:45:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/camposUI.py:126:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
src/pygame_ui/CamposUI/camposUI.py:122:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
src/pygame_ui/CamposUI/camposUI.py:130:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/CamposUI/camposUI.py:11:8: W0238: Unused private member `CamposUi.__screen_width` (unused-private-member)
src/pygame_ui/CamposUI/camposUI.py:12:8: W0238: Unused private member `CamposUi.__screen_height` (unused-private-member)
src/pygame_ui/CamposUI/camposUI.py:61:8: W0201: Attribute 'select_triangulo' defined outside __init__ (attribute-defined-outside-init)
************* Module pygame_ui.Tablero_UI.Tablero_UI
src/pygame_ui/Tablero_UI/Tablero_UI.py:55:0: C0301: Line too long (116/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:59:9: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:82:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:84:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:86:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:87:29: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:89:13: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:91:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:94:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Tablero_UI/Tablero_UI.py:122:0: C0301: Line too long (107/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:144:0: C0301: Line too long (170/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:144:0: C0325: Unnecessary parens after '=' keyword (superfluous-parens)
src/pygame_ui/Tablero_UI/Tablero_UI.py:153:0: C0301: Line too long (108/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:201:0: C0301: Line too long (110/100) (line-too-long)
src/pygame_ui/Tablero_UI/Tablero_UI.py:5:0: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/Tablero_UI/Tablero_UI.py:22:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)
************* Module pygame_ui.Tablero_UI.Test_Tablero_UI
src/pygame_ui/Tablero_UI/Test_Tablero_UI.py:16:8: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/Tablero_UI/Test_Tablero_UI.py:51:8: E1101: Module 'pygame' has no 'quit' member (no-member)
************* Module pygame_ui.Cartel_UI.Test_Cartel
src/pygame_ui/Cartel_UI/Test_Cartel.py:44:0: C0301: Line too long (118/100) (line-too-long)
src/pygame_ui/Cartel_UI/Test_Cartel.py:49:0: C0304: Final newline missing (missing-final-newline)
src/pygame_ui/Cartel_UI/Test_Cartel.py:10:8: E1101: Module 'pygame' has no 'init' member (no-member)
src/pygame_ui/Cartel_UI/Test_Cartel.py:15:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/Cartel_UI/Test_Cartel.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/Cartel_UI/Test_Cartel.py:19:25: W0212: Access to a protected member _Cartel_UI__mensaje of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:20:25: W0212: Access to a protected member _Cartel_UI__titulo of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:21:25: W0212: Access to a protected member _Cartel_UI__duracion of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/Cartel_UI/Test_Cartel.py:31:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/Cartel_UI/Test_Cartel.py:36:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/Cartel_UI/Test_Cartel.py:43:4: C0116: Missing function or method docstring (missing-function-docstring)
src/pygame_ui/Cartel_UI/Test_Cartel.py:45:17: W0212: Access to a protected member _Cartel_UI__dividir_mensaje of a client class (protected-access)
src/pygame_ui/Cartel_UI/Test_Cartel.py:3:0: W0611: Unused MagicMock imported from unittest.mock (unused-import)
************* Module pygame_ui.Cartel_UI.Cartel_UI
src/pygame_ui/Cartel_UI/Cartel_UI.py:45:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Cartel_UI/Cartel_UI.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Cartel_UI/Cartel_UI.py:57:52: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Cartel_UI/Cartel_UI.py:58:0: C0301: Line too long (110/100) (line-too-long)
src/pygame_ui/Cartel_UI/Cartel_UI.py:76:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Cartel_UI/Cartel_UI.py:80:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Cartel_UI/Cartel_UI.py:88:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Cartel_UI/Cartel_UI.py:91:0: C0303: Trailing whitespace (trailing-whitespace)
src/pygame_ui/Cartel_UI/Cartel_UI.py:93:0: C0305: Trailing newlines (trailing-newlines)
src/pygame_ui/Cartel_UI/Cartel_UI.py:4:0: R0902: Too many instance attributes (13/7) (too-many-instance-attributes)
src/pygame_ui/Cartel_UI/Cartel_UI.py:8:8: W0238: Unused private member `Cartel_UI.__mensaje_error` (unused-private-member)
src/pygame_ui/Cartel_UI/Cartel_UI.py:34:8: W0201: Attribute '__mensaje' defined outside __init__ (attribute-defined-outside-init)
************* Module cli.cli
src/cli/cli.py:20:42: W0621: Redefining name 'backgammon' from outer scope (line 168) (redefined-outer-name)
src/cli/cli.py:47:32: W0621: Redefining name 'dados' from outer scope (line 167) (redefined-outer-name)
src/cli/cli.py:86:18: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/cli/cli.py:88:18: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/cli/cli.py:92:14: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
src/cli/cli.py:159:23: W0718: Catching too general exception Exception (broad-exception-caught)
src/cli/cli.py:162:14: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
************* Module cli.Test_Cli
src/cli/Test_Cli.py:109:29: C2801: Unnecessarily calls dunder method __repr__. Use repr built-in function. (unnecessary-dunder-call)
src/cli/Test_Cli.py:110:29: C2801: Unnecessarily calls dunder method __repr__. Use repr built-in function. (unnecessary-dunder-call)
src/cli/Test_Cli.py:14:0: R0904: Too many public methods (21/20) (too-many-public-methods)
src/cli/Test_Cli.py:3:0: W0611: Unused TipoFicha imported from src.core.enums.TipoFicha (unused-import)
src/cli/Test_Cli.py:5:0: W0611: Unused Mock imported from unittest.mock (unused-import)
************* Module core.helpers.Tablero_Inicializador
src/core/helpers/Tablero_Inicializador.py:8:0: C0301: Line too long (140/100) (line-too-long)
src/core/helpers/Tablero_Inicializador.py:3:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.helpers.Test_Tablero_Inicilizador
src/core/helpers/Test_Tablero_Inicilizador.py:5:0: W0404: Reimport 'TipoFicha' (imported line 3) (reimported)
src/core/helpers/Test_Tablero_Inicilizador.py:2:0: W0611: Unused Ficha imported from src.core.models.ficha.Ficha (unused-import)
************* Module core.helpers.Tablero_Impresor
src/core/helpers/Tablero_Impresor.py:6:4: R0912: Too many branches (20/12) (too-many-branches)
src/core/helpers/Tablero_Impresor.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.models.backgammon.Test_Backgammon
src/core/models/backgammon/Test_Backgammon.py:17:0: C0301: Line too long (115/100) (line-too-long)
src/core/models/backgammon/Test_Backgammon.py:89:0: C0303: Trailing whitespace (trailing-whitespace)
src/core/models/backgammon/Test_Backgammon.py:14:0: R0904: Too many public methods (28/20) (too-many-public-methods)
src/core/models/backgammon/Test_Backgammon.py:2:0: W0611: Unused Mock imported from unittest.mock (unused-import)
************* Module core.models.backgammon.backgammon
src/core/models/backgammon/backgammon.py:57:0: C0301: Line too long (103/100) (line-too-long)
src/core/models/backgammon/backgammon.py:44:8: R1703: The if statement can be replaced with 'return bool(test)' (simplifiable-if-statement)
src/core/models/backgammon/backgammon.py:44:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
src/core/models/backgammon/backgammon.py:63:8: R1720: Unnecessary "else" after "raise", remove the "else" and de-indent the code inside it (no-else-raise)
src/core/models/backgammon/backgammon.py:151:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module core.models.dado.Test_Dados
src/core/models/dado/Test_Dados.py:32:4: E0102: method already defined line 20 (function-redefined)
************* Module core.models.dado.Dados
src/core/models/dado/Dados.py:17:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module core.models.tablero.Tablero
src/core/models/tablero/Tablero.py:47:0: C0301: Line too long (106/100) (line-too-long)
src/core/models/tablero/Tablero.py:64:8: R1720: Unnecessary "else" after "raise", remove the "else" and de-indent the code inside it (no-else-raise)
src/core/models/tablero/Tablero.py:2:0: W0611: Unused TipoFicha imported from src.core.enums.TipoFicha (unused-import)
************* Module core.models.tablero.Test_Tablero
src/core/models/tablero/Test_Tablero.py:8:0: W0611: Unused patch imported from unittest.mock (unused-import)
************* Module core.models.tablero.Test_Tablero_Validador
src/core/models/tablero/Test_Tablero_Validador.py:117:4: E0102: method already defined line 105 (function-redefined)
src/core/models/tablero/Test_Tablero_Validador.py:10:0: R0904: Too many public methods (25/20) (too-many-public-methods)
src/core/models/tablero/Test_Tablero_Validador.py:5:0: W0611: Unused MovimientoNoJustoParaGanar imported from src.core.exceptions.MovimientoNoJustoParaGanar (unused-import)
************* Module core.models.tablero.Tablero_Validador
src/core/models/tablero/Tablero_Validador.py:61:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
************* Module core.models.jugador.Jugador
src/core/models/jugador/Jugador.py:1:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.interfaces.JuegoInterfazDados
src/core/interfaces/JuegoInterfazDados.py:7:4: C0116: Missing function or method docstring (missing-function-docstring)
src/core/interfaces/JuegoInterfazDados.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.interfaces.JuegoInterfazMovimientos
src/core/interfaces/JuegoInterfazMovimientos.py:12:0: C0305: Trailing newlines (trailing-newlines)
src/core/interfaces/JuegoInterfazMovimientos.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
src/core/interfaces/JuegoInterfazMovimientos.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 8.55/10


```
