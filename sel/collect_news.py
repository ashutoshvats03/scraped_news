from bs4 import BeautifulSoup
import os
import pandas as pd

# --- Get the base directory for 'sel' package ---
# This ensures paths are relative to where this script (e.g., ai_api.py) is located.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_directory_path = os.path.join(current_dir, "data")
# --- End of base directory setup ---

d={'title':[], 'author':[], 'published':[], 'content':[]}

all_news={}
list_id=set()
num=0

# Deletion of duplicate files
# Use data_directory_path for listing files
for file_name in os.listdir(data_directory_path):
    if file_name.endswith(".html"):
        # Construct the full path to the HTML file
        file_path = os.path.join(data_directory_path, file_name)
        del_path = "" # Initialize del_path for each iteration

        try: # Added try-except for robust file handling
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                meta = soup.select_one('div.jsx-ace90f4eca22afc7.jsx-73334835.Story_story__content__body__qCd5E.story__content__body.widgetgap meta')
                if meta: # Check if meta tag was found
                    new_id = meta.get('content', '').strip()
                else:
                    new_id = None # Or handle cases where meta is not found
                    print(f"Warning: No meta tag found with content in {file_name}")

                if new_id and new_id in list_id:
                    del_path = file_path
                elif new_id: # Only add if new_id is not None
                    list_id.add(new_id)

            if del_path: # Only attempt deletion if del_path is set
                os.remove(del_path)
                print(f"{del_path} has been deleted.")
        except Exception as e:
            print(f"Error processing or deleting {file_path}: {e}")


# Process files to extract news data
# Use data_directory_path for listing files
for file_name in os.listdir(data_directory_path):
    if file_name.endswith(".html"):
        # Construct the full path to the HTML file for opening
        file_path = os.path.join(data_directory_path, file_name)
        
        try: # Added try-except for robust file handling
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                
                meta = soup.select_one('div.jsx-ace90f4eca22afc7.jsx-73334835.Story_story__content__body__qCd5E.story__content__body.widgetgap meta')
                new_id = meta.get('content', '').strip() if meta else "N/A_ID"
                
                content = soup.select('div.jsx-ace90f4eca22afc7.jsx-73334835.Story_description__fq_4S.description.paywall p')
                content_text = [n.get_text(strip=True) for n in content]

                author = soup.select('div.jsx-ace90f4eca22afc7.jsx-73334835.Story_description__fq_4S div.authors__container div.authors__by div.authdetaisl')
                author_name = [a.get_text(strip=True) for a in author]

                published = soup.select('div.jsx-ace90f4eca22afc7.jsx-73334835 div.published__on div.authdetaisl')
                published_date = [p.get_text(strip=True) for p in published]

                title = soup.select_one('div.jsx-ace90f4eca22afc7.jsx-73334835.Story_story__content__body__qCd5E.story__content__body.widgetgap h1')
                title_text = title.text.strip() if title else "N/A_Title"
                
                href_link = soup.select_one('div.jsx-ace90f4eca22afc7.jsx-73334835.Story_description__fq_4S.description.paywall a')
                link = href_link.get('href') if href_link else "N/A_Link"
                # print(title_text)
                # print("--------------------------------------------------------------------")
                # print(author_name)
                # print("--------------------------------------------------------------------")
                # print(published_date)
                # print("--------------------------------------------------------------------")
                # print(new_id)
                
                dic = {
                    'news_id': new_id,
                    'title': title_text,
                    'author': author_name,
                    'published': published_date,
                    'content': content_text,
                    'summary': "N/A", # Added a placeholder for summary as it was used in views.py
                    'link': link
                }
                all_news["news"+str(num)] = dic
                num += 1
        except Exception as e:
            print(f"Error processing {file_path} for data extraction: {e}")

# If you want to export to CSV, use data_directory_path for the output file
# df = pd.DataFrame(d)
# df.to_csv(os.path.join(data_directory_path, "laptop.csv"), index=False)