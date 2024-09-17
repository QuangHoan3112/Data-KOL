# Dữ liệu user_feed
user_feed = [
    {
        "statistics": {
            "aweme_id": "7415193603368176904",
            "collect_count": 457,
            "comment_count": 311,
            "digg_count": 33019,
            "download_count": 31,
            "play_count": 451903,
            "share_count": 201,
            "forward_count": 0,
            "lose_count": 0,
            "lose_comment_count": 0,
            "whatsapp_share_count": 0
        },
        "release_date": "16-09-2024"
    },
    {
        "statistics": {
            "aweme_id": "7415193275604159762",
            "collect_count": 733,
            "comment_count": 537,
            "digg_count": 51110,
            "download_count": 31,
            "play_count": 472317,
            "share_count": 309,
            "forward_count": 0,
            "lose_count": 0,
            "lose_comment_count": 0,
            "whatsapp_share_count": 0
        },
        "release_date": "16-09-2024"
    },
    {
        "statistics": {
            "aweme_id": "7415094795707616520",
            "collect_count": 3034,
            "comment_count": 1894,
            "digg_count": 125726,
            "download_count": 338,
            "play_count": 1635231,
            "share_count": 4518,
            "forward_count": 0,
            "lose_count": 0,
            "lose_comment_count": 0,
            "whatsapp_share_count": 2
        },
        "release_date": "16-09-2024"
    }
]

# Hàm tính trung bình
def calculate_averages(user_feed):
    total_collect_count = 0
    total_comment_count = 0
    total_digg_count = 0
    total_download_count = 0
    num_entries = len(user_feed)
    
    # Duyệt qua từng phần tử trong user_feed để cộng giá trị
    for entry in user_feed:
        statistics = entry["statistics"]
        total_collect_count += statistics["collect_count"]
        total_comment_count += statistics["comment_count"]
        total_digg_count += statistics["digg_count"]
        total_download_count += statistics["download_count"]
    
    # Tính trung bình
    average_collect_count = total_collect_count / num_entries
    average_comment_count = total_comment_count / num_entries
    average_digg_count = total_digg_count / num_entries
    average_download_count = total_download_count / num_entries
    
    # Trả về kết quả
    return {
        "number of video" : num_entries, 
        "average_collect_count": average_collect_count,
        "average_comment_count": average_comment_count,
        "average_digg_count": average_digg_count,
        "average_download_count": average_download_count
    }

# Gọi hàm và in kết quả
averages = calculate_averages(user_feed)
print(averages)
