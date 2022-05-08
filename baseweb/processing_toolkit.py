import pandas as pd
import numpy as np

def check_data(series, column_name):
    """
    Check data is used for checking data type and missing entries for medical insurance data.
    It returns a dictionary containing its status and errors.
    """
    status_dict = {"complete": False, "errors": []}

    # Expected datatypes of each field
    data_types = {
                "age": np.int64,
                "sex": "str",
                "children": np.int64,
                "bmi": np.float64,
                "smoker": "str",
                "region": "str",
                "expenses": np.float64}


    # Compare if the object read from the CSV is of the right data type
    if series.dtype != data_types[column_name]:
        try:
            # attempt to convert it excluding null values
            test_series = series.dropna().astype(data_types[column_name])
            status_dict['complete'] = True
            status_dict['errors'].append(f"Warning! The {column_name} column was the wrong datatype. We have beeen able to convert it on this occasion")

            # Report error of failed attempt
        except ValueError:
            status_dict['complete'] = False
            status_dict['errors'].append(f"Fatal Error! The {column_name} column should be a {data_types[column_name]}. We have tried to convert the datatype of '{series.dtype}' but recieved an error while doing so, please check the source before uploading again.")
    else:
        status_dict['complete'] = True
    # Let user know how many records are ommited as a result of this column
    null_entries = series.isna().sum()
    if null_entries > 0:

        # change wording based on quantity of null records.
        if null_entries > 1:
            entry_plural_check = "entries"
        else:
            entry_plural_check = "entry"

        # Add the error messag to the errors
        status_dict['errors'].append(f"Warning! {column_name} data is missing for {series.isna().sum()} {entry_plural_check}. This record will be ommitted if you continue with this document.")

    return status_dict

def check_medical_data_column_names(uploaded_col_names):
    required_column_names = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'expenses']
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

    # change the CSV to a dataframe for easy navigation
    df = pd.read_csv(csv)

    # Create a master status dictionary to help user upload correct data
    status_dict = {}
    status_dict['column_names'] = check_medical_data_column_names(df.columns)

    # Interupt other checks if column names are incorret it will cause errors.
    if not status_dict['column_names']['complete']:
        status_dict['complete'] = False
        return status_dict
    else:
        # Check data for each column, returning a status and error information
        for column_name in list(df.columns):
            status_dict[column_name] = check_data(df[column_name], column_name)

    # Check for any fatal errors that prevent the document from being processed
    fatal_errors = 0
    for key in status_dict:
        if not status_dict[key]['complete']:
            fatal_errors += 1

    # Total records to be ommited due to null values

    drop_na_df = df.dropna()

    status_dict['quantity_to_add'] = f"We can add {drop_na_df.shape[0]} of {df.shape[0]} records"


    # if fatal errors prevent user from continuing with document
    if fatal_errors > 0:
        status_dict['complete'] = False
    else:
        status_dict['complete'] = True


    return status_dict
