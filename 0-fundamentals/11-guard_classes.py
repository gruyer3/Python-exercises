# Guard classes handle edge cases at the top of functions to avoid deep nesting of if conditions
def process_data_guarded(data):
    if not data:
        print ("No data provided")
    elif not isinstance(data, list):
        print ("Invalid value for data. Please provide a list.")
    else:
        print (f"Processing {len(data)} items...")
        print ("Processed")

process_data_guarded(None)
process_data_guarded([])
process_data_guarded([1, 2, 3, 4, 5])
process_data_guarded("abc")