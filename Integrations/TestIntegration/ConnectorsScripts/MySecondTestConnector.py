# ==============================================================================
# title           : HelloWorldConnector.py
# description     : Conector de ejemplo que imprime "Hola mundo".
# author          : ejemplo
# date            : 2025-09-08
# python_version  : 3.x
# ==============================================================================

# =====================================
#              IMPORTS
# =====================================
from SiemplifyConnectors import SiemplifyConnectorExecution
from SiemplifyUtils import output_handler


# =====================================
#             CONSTANTS
# =====================================
CONNECTOR_NAME = "HelloWorld Connector"


# =====================================
#               MAIN
# =====================================
@output_handler
def main():
    siemplify = SiemplifyConnectorExecution()
    siemplify.script_name = CONNECTOR_NAME

    siemplify.LOGGER.info("===== Iniciando conector de ejemplo =====")
    print("Hola mundo")   # salida estándar
    siemplify.LOGGER.info("MySecondTestConnector 23")  # salida en logs de SecOpsproi

    # Siempre hay que devolver una lista de casos (aunque vacía)
    return []


if __name__ == "__main__":
    main()
