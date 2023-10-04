def process_filepath(filepath):
    filepath = filepath.replace("c:/", "")
    filepath = filepath.replace("/", "%5C").replace(" ", "%20")
    return filepath

def main():
    with open("windows-files.txt", "r") as infile:
        file_paths = infile.readlines()

    updated_file_paths = [process_filepath(fp.strip()) for fp in file_paths]

    with open("windows-files-fixed.txt", "w") as outfile:
        for updated_fp in updated_file_paths:
            outfile.write(updated_fp + "\n")

if __name__ == "__main__":
    main()
