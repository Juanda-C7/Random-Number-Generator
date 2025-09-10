import hashlib
from googleapiclient.discovery import build
from time_selector import get_keyword_from_time
from visualize import visualize_rng

API_KEY = "AIzaSyC1-iRmWhz8rAwmSGBVUdUFFg-Glhpb-v0"
youtube = build("youtube", "v3", developerKey=API_KEY)

TARGET_CHARS = 45000 


def search_videos(keyword, max_results=80):
    request = youtube.search().list(
        q=keyword,
        part="id",
        type="video",
        maxResults=max_results
    )
    response = request.execute()
    video_ids = [item["id"]["videoId"] for item in response["items"]]
    return video_ids

def get_comments(video_id, max_comments=40):
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_comments,
            textFormat="plainText"
        )
        response = request.execute()
        comments = []
        for item in response.get("items", []):
            text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(text)
        return comments
    except Exception:
        return []

def collect_random_bytes(video_ids, target_chars=TARGET_CHARS):
    all_bytes = bytearray()
    for vid in video_ids:
        comments = get_comments(vid, max_comments=30)
        for c in comments:
            try:
                h = hashlib.sha512(c.encode("ascii", "ignore")).digest()
            except Exception:
                continue
            all_bytes.extend(h)  # agrega 64 bytes crudos por comentario
            if len(all_bytes) >= target_chars:
                return list(all_bytes[:target_chars])
    return list(all_bytes[:target_chars])

# ---------- Main ----------
if __name__ == "__main__":
    keyword = get_keyword_from_time()
    video_ids = search_videos(keyword, max_results=50)
    rng_numbers = collect_random_bytes(video_ids, TARGET_CHARS)
    visualize_rng(rng_numbers, title="YouTube RNG 90k bytes")
