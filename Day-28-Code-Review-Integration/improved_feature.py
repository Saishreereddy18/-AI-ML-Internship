
from pathlib import Path

ALLOWED_EXTENSIONS = {".pdf"}


def validate_resume(file_path):
    """Validate an uploaded resume file."""

    try:
        if not file_path:
            return False, "No file was uploaded."

        resume = Path(file_path)

        if resume.suffix.lower() not in ALLOWED_EXTENSIONS:
            return False, "Only PDF files are allowed."

        if not resume.is_file():
            return False, "File does not exist."

        if resume.stat().st_size == 0:
            return False, "The uploaded file is empty."

        return True, "Resume uploaded successfully."

    except (OSError, TypeError, ValueError) as error:
        return False, f"File validation failed: {error}"


if __name__ == "__main__":
    test_files = [None, "resume.docx", "resume.pdf"]

    for file in test_files:
        status, message = validate_resume(file)
        print(f"{file}: {message}")
