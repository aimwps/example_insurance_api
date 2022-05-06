import pandas as pd


def check_medical_data_column_names(uploaded_col_names):
    required_column_names = ['age', 'sex', 'bi', 'children', 'smoker', 'region', 'expenses']

    status_dict = {"complete": False, "errors": []}
    # Check column names are formatted as required
    if list(uploaded_col_names) == required_column_names:
        status_dict['complete'] = True
    else:
        status_dict['complete'] = False
        missing_columns = required_column_names[:]

        # Find where the error occurs:
        for csv_col_name in list(uploaded_col_names):
            col_name_count = required_column_names.count(csv_col_name)

            # The column name is incorrect
            if col_name_count == 0:
                status_dict['errors'].append(f"'{csv_col_name}' is not a required field")

            # There are duplicate correct column names
            elif col_name_count > 1:
                status_dict['errors'].append(f"'{csv_col_name}' appears more than once")

        # There is exactly one match for this column, remove it from missing columns list
            else:
                missing_columns.remove(csv_col_name)

        # Add an error message for the missin required columns
        if len(missing_columns) > 0 :
            missing_columns = " ".join([f"'{col_name}'" for col_name in missing_columns])
            status_dict['errors'].append(f"{missing_columns} fieleds are missing from the csv.")

    return status_dict

def check_csv_eligibility(csv):
    df = pd.read_csv(csv)
    status_dict = {}
    status_dict['column_names'] = check_medical_data_column_names(df.columns)
    if not status_dict['column_names']['complete']:
        return status_dict
    else:
        print("returning anyway")
        return status_dict














    return True
