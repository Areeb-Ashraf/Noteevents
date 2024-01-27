def prompt(text):
    return f'''
    Please analyze the following medical report and determine if the patient has experienced an ischemic stroke. 
    Respond with 1 if it is an ischemic stroke patient, and 0 if it is not. Respond with 0 or 1 ONLY

    The medical report:
    {text}
    '''