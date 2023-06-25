import os

# The directory where your text files are located
dir_path = "/Users/pratik/Desktop/Projects/python/readCsv/"

# The file where the combined content will be written
output_file = "/Users/pratik/Desktop/Projects/python/readCsv/output.txt"

# Get a list of all text files in the directory
txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    for i, fname in enumerate(txt_files):
        with open(os.path.join(dir_path, fname)) as infile:
            # Write the contents of each file to the output file
            for line in infile:
                outfile.write(line)
            # Add a newline character after each file to separate the contents
            outfile.write("\n")
        
        # Print a progress message after each file is processed
        print(f"Processed file {i+1} of {len(txt_files)}: {fname}")

print("Combined all text files into one.")