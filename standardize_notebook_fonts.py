
# Make Markdown text uniform across all notebooks

import argparse
import json
import re
import shutil
from pathlib import Path


# Remove Markdown headings and bold formatting

def plain_markdown(source):

    updated = []
    inside_fence = False

    for line in source.splitlines(keepends=True):

        if re.match(r"^\s*(```|~~~)", line):
            inside_fence = not inside_fence
            updated.append(line)
            continue

        if inside_fence:
            updated.append(line)
            continue

        # Remove heading symbols from Markdown text

        line = re.sub(
            r"^( {0,3})#{1,6}[ \t]+",
            r"\1",
            line
        )

        # Remove bold formatting but keep the text

        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        line = re.sub(r"(?<!\w)__(.+?)__(?!\w)", r"\1", line)

        updated.append(line)

    return "".join(updated)


# Review and update the notebooks

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--apply",
        action="store_true"
    )

    args = parser.parse_args()

    # Identify the notebook folder

    notebook_folder = Path("00_Notebooks")

    if not notebook_folder.is_dir():
        print("Open the main project folder and try again.")
        return

    files_changed = 0
    total_cells = 0

    # Review each notebook

    for path in sorted(notebook_folder.glob("*.ipynb")):

        original_text = path.read_text(encoding="utf-8")
        notebook = json.loads(original_text)

        cells_changed = 0

        # Only change Markdown cells

        for cell in notebook.get("cells", []):

            if cell.get("cell_type") != "markdown":
                continue

            original_source = cell.get("source", [])

            old_text = (
                "".join(original_source)
                if isinstance(original_source, list)
                else original_source
            )

            new_text = plain_markdown(old_text)

            if new_text != old_text:

                cell["source"] = (
                    new_text.splitlines(keepends=True)
                    if isinstance(original_source, list)
                    else new_text
                )

                cells_changed += 1

        if cells_changed == 0:
            continue

        files_changed += 1
        total_cells += cells_changed

        print(f"{path.name}: {cells_changed} Markdown cells")

        # Save the updated notebook when requested

        if args.apply:

            # Create a backup before changing the notebook

            backup_folder = (
                Path.home()
                / "notebook_format_backups"
                / Path.cwd().name
            )

            backup_folder.mkdir(
                parents=True,
                exist_ok=True
            )

            backup = backup_folder / path.name

            if not backup.exists():
                shutil.copy2(path, backup)

            # Save the updated notebook

            path.write_text(
                json.dumps(
                    notebook,
                    ensure_ascii=False,
                    indent=1
                ) + "\n",
                encoding="utf-8"
            )

    # Display the results

    if args.apply:

        print(
            f"\nUpdated {total_cells} Markdown cells "
            f"in {files_changed} notebooks."
        )

        print("Python code and saved outputs remain unchanged.")
        print("Backups saved outside the project folder.")

    else:

        print(
            f"\nPreview: {total_cells} Markdown cells "
            f"in {files_changed} notebooks."
        )

        print("No files were changed.")


if __name__ == "__main__":
    main()
