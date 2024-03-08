from frontend import ExcelValidatorUI
from backend import process_excel, excel_to_sql


def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        df, result, errors = process_excel(upload_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_wrong_message()
        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_success_message()

if __name__ == "__main__":
    main()