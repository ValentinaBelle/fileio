import json
import os

history_file = "test_save_history.json"

def save_history(file_path, link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({"file_path": os.path.basename(file_path), 'download_link': link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)


def test_save_history():
    test_file_path = "test_file.txt"
    test_download_link = "https://file.io/drjggfj"

    save_history(test_file_path, test_download_link)

    with open("test_save_history_json", "r") as f:
        history = json.load(f)
        assert len(history) == 1
        assert history[0]["file_path"] == test_file_path
        assert history[0]["download_link"] == test_download_link

    os.remove("test_save_history.json")

test_save_history()
