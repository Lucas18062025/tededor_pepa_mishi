import tempfile
# This script demonstrates the use of temporary files in Python using the tempfile module.
if __name__=="__main__":
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        print(f"Temporary file created: {temp_file.name}")
        
        # Write some data to the temporary file
        temp_file.write(b"Hello, this is a temporary file.")
        temp_file.flush()  # Ensure data is written
        
        # Read the data back
        temp_file.seek(0)  # Go back to the beginning of the file
        data = temp_file.read()
        print(f"Data read from temporary file: {data.decode()}")
    
    print("Temporary file will be deleted automatically.")
else:
    print("This script is intended to be run as the main module.")# The temporary file is automatically deleted when closed or when the program ends.
# The temporary file is automatically deleted when closed or when the program ends.