import os
import subprocess


def main():
    for file in os.listdir():
        if file.endswith(".m4a"):
            print(f"Transcribing {file}")
            print('-----------------------------------')
            command = ["whisper", f"{file}", "--output_format", "json", "--model", "large", "--language", "pl",
                       "--verbose", "True", "--task", "transcribe", "--word_timestamps", "True" ]
            process = subprocess.Popen(command, stdout=subprocess.PIPE)

            for line in iter(process.stdout.readline, b''):
                print(line.decode(), end='')
            process.stdout.close()
            process.wait()
            print('-----------------------------------')


if __name__ == "__main__":
    main()
