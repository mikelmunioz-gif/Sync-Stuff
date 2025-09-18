from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED

SCRIPT_NAME = "NuevoJob"

@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    # Lee el parámetro definido en el jobdef
    TEST = siemplify.extract_job_param("Test", input_type=str, is_mandatory=True)

    status = EXECUTION_STATE_COMPLETED
    result_value = True
    output_message = "OK"

    try:
        siemplify.LOGGER.info(f"🚀 NuevoJob | Test={TEST}")
        # tu lógica aquí
    except Exception as e:
        status = EXECUTION_STATE_FAILED
        result_value = False
        output_message = f"Error: {e}"

    siemplify.end(output_message, result_value, status)

if __name__ == "__main__":
    main()
