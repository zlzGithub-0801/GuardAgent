import string


def check_access(list_of_function:list, list_of_database:dict, summary_of_function:list, summary_of_database:dict):
    access_denied = False
    # Check access permission of functions
    inaccessible_function = list(set(summary_of_function) - set(list_of_function))
    if len(inaccessible_function) > 0:
        access_denied = True
    # Check access permission of databases and columns
    inaccessible_database = []
    inaccessible_column = []
    for key, value in summary_of_database.items():
        if key not in list_of_database:
            access_denied = True
            inaccessible_database.append(key)
        else:
            inaccessible_column_temp = list(set(value) - set(list_of_database[key]))
            if len(inaccessible_column_temp) > 0:
                access_denied = True
                inaccessible_column += inaccessible_column_temp

    if access_denied:
        print("Inaccessible functions: ", inaccessible_function)
        print("Inaccessible databases: ", inaccessible_database)
        print("Inaccessible columns: ", inaccessible_column)

    return access_denied


if __name__ == "__main__":
    # Example usage
    list_of_function = ["Calculate", "LoadDB", "FilterDB", "GetValue", "SQLInterpreter", "Calendar"]
    summary_of_function = ["LoadDB", "FilterDB", "GetValue"]
    list_of_database = {
        "allergy": ["patientunitstayid", "allergyname", "allergytime"],
        "cost": ["patienthealthsystemstayid", "cost"],
        "diagnosis": ["patientunitstayid", "diagnosisname", "diagnosistime"],
        "intakeoutput": ["patientunitstayid", "celllabel"],
        "lab": ["patientunitstayid", "labname", "labresult", "labresulttime"],
        "medication": ["patientunitstayid", "drugname", "routeadmin", "drugstarttime"],
        "microlab": ["patientunitstayid", "culturesite", "organism", "culturetakentime"],
        "patient": ["patientunitstayid", "patienthealthsystemstayid", "gender", "age", "admissionweight",
                    "dischargeweight", "uniquepid", "hospitaladmittime", "unitdischargetime", "hospitaldischargetime"],
        "treatment": ["patientunitstayid", "treatmentname", "treatmenttime"],
        "vitalperiodic": ["patientunitstayid", "temperature", "sao2", "heartrate", "respiration", "systemicdiastolic",
                          "systemicmean", "observationtime"]
    }
    summary_of_database = {
        "patient": ["uniquepid", "hospitaldischargetime", "patientunitstayid"],
        "medication": ["patientunitstayid", "drugname"]
    }

    access_denied = check_access(list_of_function, list_of_database, summary_of_function, summary_of_database)
    print(access_denied)

