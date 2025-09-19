from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED

SCRIPT_NAME = "HelloJob"

@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    # Lee el parámetro que definimos en el .jobdef
    TEST = siemplify.extract_job_param("Test", input_type=str, is_mandatory=True)

    status = EXECUTION_STATE_COMPLETED
    result_value = True
    output_message = "OK"

    try:
        siemplify.LOGGER.info(f"🚀 HelloJob(TestIntegration2) | Test={TEST}")
        siemplify.LOGGER.info(f"Mensaje de prueba. Si sale es que todo ha salido bien")
        # tu lógica real aquí
    except Exception as e:
        status = EXECUTION_STATE_FAILED
        result_value = False
        output_message = f"Error: {e}"

    siemplify.end(output_message, result_value, status)

if __name__ == "__main__":
    main()
