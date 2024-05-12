import os
import json

def read_content_json(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON file '{file_name}'.")
        return None

def json_to_markdown(data):
    if not data:
        return ""

    markdown_content = "---\n"
    for key, value in data.items():
        if key not in ["content", "tags"]:
            markdown_content += f"{key}: {value}\n"
    markdown_content += "---\n\n"

    tags = data.get("tags", [])
    if tags:
        markdown_content += "#" + " #".join(tags) + "\n\n"

    markdown_content += data.get("content", "")

    return markdown_content

def write_to_md_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Markdown content has been written to {file_path}.")
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

def main():
    json_file_name = input("Enter the backup file name to convert: ")
    content_data = read_content_json(json_file_name)
    if content_data:
        export_folder = "export"
        if not os.path.exists(export_folder):
            os.makedirs(export_folder)

        for index, item in enumerate(content_data, start=1):
            markdown_content = json_to_markdown(item)
            created_at = item.get("created_at", "")
            if created_at:
                file_name = f"{created_at.replace(':', '-').replace('T', '-').replace('Z', '')}-{index}.md"
                file_path = os.path.join(export_folder, file_name)
                write_to_md_file(file_path, markdown_content)
            else:
                print(f"No 'created_at' field found in template data {index}.")

if __name__ == "__main__":
    main()
