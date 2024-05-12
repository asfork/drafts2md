This script converts backup files from [Drafts](https://getdrafts.com/) into Markdown format and exports each draft as a separate Markdown file. You can then import these files into Obsidian or any other Markdown note-taking app.

## Features
- Reads JSON data from a `*.draftsExport` file.
- Converts backup file into Markdown format.
- Exports each draft as an individual Markdown file.
- Ignores unnecessary keys in JSON data during conversion.

## Requirements
- Python 3.x

## Usage
1. Ensure Python 3 is installed on your system.
2. Place your backup file in the same directory as this script.
3. Run the script `python drafts2md.py`.
4. Enter the name of the backup file when prompted, for example, "DraftsExport-2024-01-01-21-01.draftsExport".
5. The script will export each draft into separate Markdown files, naming each file based on the creation time of the corresponding draft. For example, 2018-05-06-23-13-20-1.md.

## License
This project is licensed under the MIT License.
