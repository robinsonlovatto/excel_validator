from frontend import ExcelValidatorUI
from backend import process_excel, excel_to_sql
import logging
import sentry_sdk
import os
from dotenv import load_dotenv

load_dotenv(".env")

# reading env variables
SENTRY_DSN = os.getenv('SENTRY_DSN')

# init of the sentry sdk
sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# settings to append 
# level debug write all the messages
logging.basicConfig(filename='app_logging.log', encoding='utf-8', level=logging.DEBUG)

def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        df, result, errors = process_excel(upload_file)
        ui.display_results(result, errors)
        logging.error("Error in Excel schema.")
        sentry_sdk.capture_message("Error in Excel schema.")

        if errors:
            ui.display_wrong_message()
        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_success_message()
            logging.info("Data sent to DB!")
            sentry_sdk.capture_message("Data sent to DB!")

if __name__ == "__main__":
    main()