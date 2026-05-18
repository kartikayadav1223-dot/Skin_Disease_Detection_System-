import os
import hashlib

def get_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def clean_duplicates(directory):
    seen_hashes = {}
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    deleted_count = 0
    for filename in files:
        file_path = os.path.join(directory, filename)
        file_hash = get_hash(file_path)
        
        if file_hash in seen_hashes:
            print(f"Deleting duplicate: {filename} (Matches {seen_hashes[file_hash]})")
            os.remove(file_path)
            deleted_count += 1
        else:
            seen_hashes[file_hash] = filename
            
    print(f"Cleanup complete. Deleted {deleted_count} duplicates.")

if __name__ == "__main__":
    target_dir = r"c:\skin_detection_project\media\skin_images"
    clean_duplicates(target_dir)
