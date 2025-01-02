from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Directory to scan for .md files
DIRECTORY_PATH = "./files"

@app.route('/api/md-files', methods=['GET'])
def list_md_files():
    try:
        # Get all .md files in the directory
        md_files = [f for f in os.listdir(DIRECTORY_PATH) if f.endswith('.md')]
        
        # Create a dictionary with file names and their content
        files_with_content = {}
        for file in md_files:
            with open(os.path.join(DIRECTORY_PATH, file), 'r', encoding='utf-8') as f:
                files_with_content[file] = f.read()

        return jsonify(files_with_content), 200
    except FileNotFoundError:
        return jsonify({"error": "Directory not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
