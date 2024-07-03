# Preprocess the CSV file to replace semicolons and tabs with commas
input_file = '/home/dan/Downloads/layoffs.csv'
output_file = '/home/dan/Downloads/layoffs_preprocessed.csv'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Replace semicolons and tabs with commas
        processed_line = line.replace(';', ',').replace('\t', ',')
        outfile.write(processed_line)

output_file
