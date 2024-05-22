import os

structure = {
    "Sistema_De_Analisis": {
        "data": {
            "raw": {},
            "processed": {}
        },
        "src": {
            "__init__.py": "",
            "scraping": {
                "__init__.py": "",
                "scraper.py": ""
            },
            "analysis": {
                "__init__.py": "",
                "analysis.py": ""
            },
            "reporting": {
                "__init__.py": "",
                "report.py": ""
            },
            "utils": {
                "__init__.py": "",
                "helpers.py": ""
            }
        },
        "notebooks": {
            "exploration.ipynb": ""
        },
        "tests": {
            "__init__.py": "",
            "test_scraper.py": ""
        },
        "requirements.txt": "",
        "README.md": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as file:
                file.write(content)

base_path = "."
create_structure(base_path, structure)
