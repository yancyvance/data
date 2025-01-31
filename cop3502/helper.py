import os
import subprocess
import urllib.request

def download_file(url, filename):
    """Downloads a file from a given URL and saves it as the specified filename."""
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {filename} successfully.")
    except Exception as e:
        print(f"Failed to download file.")
        exit(1)

def compile_c_code(c_filename):
    """Compiles a C program using gcc."""
    executable_name = c_filename.replace(".c", "")
    compile_command = ["gcc", c_filename, "-o", executable_name]
    
    try:
        subprocess.run(compile_command, check=True)
        print(f"Compilation successful: {executable_name}")
        return executable_name
    except subprocess.CalledProcessError:
        print("Compilation failed.")
        exit(1)

def run_executable(executable_name):
    """Runs the compiled executable."""
    try:
        subprocess.run(["./" + executable_name])
    except Exception as e:
        print(f"Error running {executable_name}: {e}")
        exit(1)

def main():
    # check which lab exercise this is
    exercise_number = input("Which programming assignment is this for (Enter a number): ")
    complete_file_name = 'pa{}_data.txt'.format(int(exercise_number))
    
    # check if the file already exists
    if not os.path.exists(complete_file_name):
        github_url = 'https://raw.githubusercontent.com/yancyvance/data/refs/heads/main/cop3502/pa{}_data.txt'.format(exercise_number)
        input_filename = os.path.basename(github_url)
        download_file(github_url, input_filename)
    
    c_filename = input("Enter the name of your C file (including .c extension): ")
    if not os.path.exists(c_filename):
        print("C file not found.")
        exit(1)
    
    executable_name = compile_c_code(c_filename)
    run_executable(executable_name)

if __name__ == "__main__":
    main()
