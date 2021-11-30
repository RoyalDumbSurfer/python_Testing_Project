basic_information = {"name": ['karl', 'Lary'], "mobile": ["0134567894", "0123456789"]}
academic_information = {"grade": ["A", "B"]}

# Combines Dict
details = dict()

#Dictionary Comprehension Method
details = {key: value for data in (basic_information, academic_information) for key, value in data.items()}
print(details)

## Dictionary unpacking
details = {**basic_information, **academic_information}
print(details)

## Copy and Update Method
details = basic_information.copy()
details.update(academic_information)
print(details)
