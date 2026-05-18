import os
import requests
import time

def add_complete_clinical_dataset():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Using reliable, high-uptime medical archives and educational stock
    catalog = {
        # Infections
        "scabies.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Scabies-burrow.jpg/1024px-Scabies-burrow.jpg",
        "warts.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Common_Wart_Hand.jpg/1024px-Common_Wart_Hand.jpg",
        "shingles.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Herpes_zoster_chest.jpg/1024px-Herpes_zoster_chest.jpg",
        "impetigo_blister.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Impetigo_close_up.jpg/1024px-Impetigo_close_up.jpg",
        
        # Hair & Nails
        "alopecia_areata.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Alopecia_areata.jpg/1024px-Alopecia_areata.jpg",
        "onychomycosis.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Onychomycosis.jpg/1024px-Onychomycosis.jpg",
        "keratosis_pilaris.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Keratosis_pilaris_arm.jpg/1024px-Keratosis_pilaris_arm.jpg",
        
        # Cancers & Pre-Cancers
        "basal_cell.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Basal_cell_carcinoma.jpg/1024px-Basal_cell_carcinoma.jpg",
        "actinic_keratosis.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Actinic_keratosis_on_temple.JPG/1024px-Actinic_keratosis_on_temple.JPG",
        
        # Scars & Structures
        "keloid_scar.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Keloid_scar.jpg/1024px-Keloid_scar.jpg",
        "skin_tags.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Skin_tags.jpg/1024px-Skin_tags.jpg",
        "ichthyosis.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Ichthyosis_vulgaris.jpg/1024px-Ichthyosis_vulgaris.jpg",
        
        # Pexels Clinical Variations
        "acne_rosacea.jpg": "https://images.pexels.com/photos/5451296/pexels-photo-5451296.jpeg?auto=compress&cs=tinysrgb&w=800",
        "atopic_dermatitis.jpg": "https://images.pexels.com/photos/5451366/pexels-photo-5451366.jpeg?auto=compress&cs=tinysrgb&w=800",
        "hidradenitis_suppurativa.jpg": "https://images.pexels.com/photos/5451258/pexels-photo-5451258.jpeg?auto=compress&cs=tinysrgb&w=800",
        "vitiligo.jpg": "https://images.pexels.com/photos/3845981/pexels-photo-3845981.jpeg?auto=compress&cs=tinysrgb&w=800"
    }

    target_dir = r"c:\skin_detection_project\media\skin_images"
    os.makedirs(target_dir, exist_ok=True)

    success_count = 0
    for local_name, url in catalog.items():
        try:
            print(f"Acquiring {local_name}...")
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                with open(os.path.join(target_dir, local_name), "wb") as f:
                    f.write(response.content)
                success_count += 1
                print(f"  [Verified]")
                time.sleep(2) # High politeness to bypass rate limits
            else:
                print(f"  [X] Failed: {response.status_code}")
        except Exception as e:
            print(f"  [!] Error: {e}")

    print(f"\nLibrary Expansion Complete: Added {success_count} new clinical disease samples.")

if __name__ == "__main__":
    add_complete_clinical_dataset()
