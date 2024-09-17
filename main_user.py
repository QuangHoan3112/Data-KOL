import os
from dotenv import load_dotenv
from api.user import user_api
import pandas as pd
from api.user import follower_api
from api.user import following_api 
from api.feed import user_feed_api
import json
import csv
from datetime import datetime
# Load các biến môi trường từ file .env_sample
load_dotenv(dotenv_path='.env_sample')

# Lấy các giá trị từ biến môi trường
rapidapi_key = os.getenv('x-rapidapi-key')
rapidapi_host = os.getenv('x-rapidapi-host')

headers = {
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host": rapidapi_host
}

def convert_str_to_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y")

def average_interaction(user_feed,limit):
    total_collect_count = 0
    total_comment_count = 0
    total_like_count = 0
    total_download = 0
    number_video = min(limit,len(user_feed))

    for video in user_feed[:number_video]:
        statistics = video["statistics"]
        total_collect_count += statistics["collect_count"]
        total_comment_count += statistics["comment_count"]
        total_like_count += statistics["digg_count"]
        total_download += statistics["download_count"]

    average_collect_count = total_collect_count / number_video
    average_comment_count = total_comment_count / number_video
    average_like_count = total_like_count / number_video
    average_download_count = total_download / number_video

    average_interactions = (average_collect_count + average_comment_count + average_like_count + average_download_count) /4

    return average_interactions 

if __name__ == '__main__':
    user_names = list(map(str, input("Nhập tên tài khoản KOL: ").split()))
    user_data_list = [] 

    output_file = 'kol_user_data.csv'

    for username in user_names:
        user = user_api.get_user_data_by_username(username, headers)  
        user_feed = user_feed_api.get_user_feed_by_username(username,headers)
        user_feed_sort = sorted(user_feed,key=lambda x:abs(datetime.now() - convert_str_to_date(x["release_date"])))
        if user:  
            user_data_list.append({
                "Nickname": user.nickname,       
                "Followers": user.follower_count, 
                "Total Favorited": user.total_favorited, 
                "UID": user.uid,            
                "Unique ID": user.unique_id,
                "user_feed": user_feed_sort,
                "percentage_interactions" : (average_interaction(user_feed_sort,len(user_feed_sort)) / int(user.follower_count)) * 100
            })
            with open(f"{username}.json","w",encoding= "utf-8") as file:
                json.dump(user_data_list,file,ensure_ascii=False,indent=4)
        


    if user_data_list:
        df = pd.DataFrame(user_data_list)

        # Ghi dữ liệu vào file CSV
        df.to_csv(output_file, index=False, encoding='utf-8-sig')

        print(f"Dữ liệu đã được lưu vào {output_file}")
    else:
        print("Không tìm thấy thông tin người dùng.")

        '''print(user.__str__())
        user_id = user.uid  # Giả sử uid là user ID cần thiết
        print('Id người dùng là:', user_id)
        # Lấy dữ liệu followers từ follower_api
        followers = follower_api.get_follower_data_by_user_id(user_id, headers)
        
        if followers:
            print("Thông tin của Followers là: ")
            print("\n")
            for follower in followers:
                print(follower)
                print("\n" + "="*40 + "\n")
        else:
            print("No followers found or API request failed.")
        
        # Lấy dữ liệu following từ following_api
        followings = following_api.get_following_data_by_user_id(user_id, headers)
        
        if followings:
            print("Thông tin của Followings là: ")
            print("\n")
            for following in followings:
                print(following)
                print("\n" + "="*40 + "\n")  
        else:
            print("No following found or API request failed.")
    else:
        print("Failed to fetch user data.")'''
