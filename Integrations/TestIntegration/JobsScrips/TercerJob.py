from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED

SCRIPT_NAME = "TestJob"

@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    status = EXECUTION_STATE_COMPLETED
    result_value = True
    output_message = "Ping OK (job vacío)."

    try:
        siemplify.LOGGER.info("🚀 TercerJob - job de prueba")
        siemplify.LOGGER.info("🚀 ÉXITO. SE HA HECHO EL CAMBIO 17")
        # Aquí irá tu lógica real cuando quieras.
    except Exception as e:
        status = EXECUTION_STATE_FAILED
        result_value = False
        output_message = f"Error: {e}"

    siemplify.end(output_message, result_value, status)

if __name__ == "__main__":
    main()
