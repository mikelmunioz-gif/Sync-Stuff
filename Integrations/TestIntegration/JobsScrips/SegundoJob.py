from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED

SCRIPT_NAME = "SegundoJob"

@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    # --- Lee los parámetros definidos en el .jobdef ---
    TEST = siemplify.extract_job_param("Test", input_type=str, is_mandatory=True)
    DRY_RUN = siemplify.extract_job_param("Dry Run", input_type=bool, default_value=False)
    VERIFY_SSL = siemplify.extract_job_param("Verify SSL", input_type=bool, default_value=True)
    TIME_WINDOW_MIN = siemplify.extract_job_param("Time Window (Minutes)", input_type=int, default_value=60)
    MAX_ITEMS = siemplify.extract_job_param("Max Items", input_type=int, default_value=100)
    LOG_LEVEL = siemplify.extract_job_param("Log Level", input_type=str, default_value="INFO")

    status = EXECUTION_STATE_COMPLETED
    result_value = True
    output_message = "Ping OK (job vacío)."

    try:
        siemplify.LOGGER.info(f"🚀 SegundoJob | Test={TEST} | DryRun={DRY_RUN} | TW={TIME_WINDOW_MIN}m | Max={MAX_ITEMS} | SSL={VERIFY_SSL} | Log={LOG_LEVEL}")
        # Tu lógica aquí...
    except Exception as e:
        status = EXECUTION_STATE_FAILED
        result_value = False
        output_message = f"Error: {e}"

    siemplify.end(output_message, result_value, status)

if __name__ == "__main__":
    main()
