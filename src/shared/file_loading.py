def load_text_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents


def load_text_file_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents.splitlines()
