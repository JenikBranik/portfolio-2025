from src.utils.targetfolder import TargetFolder
from src.finder.scanner import ParallelScanner


class DuplicateController:
    """
    Main logic of program
    """
    def start_program(self):
        user_path = input("Enter the folder path: ")

        try:
            target_folder = TargetFolder(user_path)
            app = ParallelScanner(target_folder)
            app.scan()
            print(app)

        except (FileNotFoundError, NotADirectoryError, ValueError) as e:
            print(f"\nError: {e}")
