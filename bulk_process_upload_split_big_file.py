#  bulk upload loopin 
# this program will upload all files one by one on server
# if file is uploaded it will be moved to processed folder
# if not uploaded it will remain there and transaction will stop

import os
import shutil
import mysql.connector
import re
import configparser
# import logging

def upload_to_live():
   
    cursor = db.cursor()
    # logging.basicConfig(filename="uploader.log", level=logging.INFO)

    # Folders    
    config = configparser.ConfigParser()
    config.read("config.ini")
    UPLOAD_DIR = config["settings"]["upload_dir"]
    PROCESSED_DIR = config["settings"]["porcessed_dir"]

    # UPLOAD_DIR = "D:/Aging_Data_Upload/upload"
    # PROCESSED_DIR = "D:/Aging_Data_Upload/processed"

    # Extract numbers from filenames and sort correctly
    def natural_sort(file_list):    
        return sorted(file_list, key=lambda x: int(re.search(r'\d+', x).group()))
                            
    # Get all CSV files in upload folder
    csv_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith('.csv')]

    # Apply natural sorting
    csv_files = natural_sort(csv_files)

    # Process each file one by one
    for file_name in csv_files:  # Sort to maintain order
        file_path = os.path.join(UPLOAD_DIR, file_name).replace("\\", "/")

        # SQL Query for Upload
        query = f"""
           
        """

        try:
            cursor.execute("START TRANSACTION;")  # Start transaction
            cursor.execute(query)  # Upload file
            cursor.execute("COMMIT;")  # Commit if successful            
            # logging.info("✅ Uploaded: {file_name}")            

            print(f"✅ Uploaded: {file_name}")

            # Move file to processed folder
            shutil.move(file_path, os.path.join(PROCESSED_DIR, file_name))
            # logging.info("📂 Moved {file_name} to processed folder.")  
            print(f"📂 Moved {file_name} to processed folder.")

        except Exception as e:
            cursor.execute("ROLLBACK;")  # Rollback if error occurs
            # logging.error("❌ Error uploading {file_name}: {e}")
            print(f"❌ Error uploading {file_name}: {e}")

    # Close connection
    cursor.close()
    db.close()

upload_to_live()
