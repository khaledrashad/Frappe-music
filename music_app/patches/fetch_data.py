import frappe
import requests
import json

def execute():
    id_array = ["16775","1421","20185","1096353"]
    for id in id_array:
        url = f'https://api.genius.com/artists/{id}'

        payload = {}
        headers = {
            'Authorization': 'Bearer Pa-GCITbBe8oQHj5lY0b4DY-kzBLrKq2tIvLyISzP4iJbgNq2XXnbQHwpFTIhsDC'
    }

        response = requests.request("GET", url, headers=headers, data=payload)
        artist_dict = json.loads(response.text)
        name = artist_dict["response"]['artist']["name"]
        image = artist_dict["response"]['artist']["image_url"]
        if not frappe.db.exists({"doctype": "Artist", "artist_name": name}):
            doc = frappe.get_doc({
                "doctype":"Artist",
                "artist_name": name,
                "artist_image": image
            })
            doc.insert()
        

        url = f'https://api.genius.com/artists/{id}/songs'

        payload = {}
        headers = {
        'Authorization': 'Bearer Pa-GCITbBe8oQHj5lY0b4DY-kzBLrKq2tIvLyISzP4iJbgNq2XXnbQHwpFTIhsDC'
        }

        response2 = requests.request("GET", url, headers=headers, data=payload)
        songs_dict = json.loads(response2.text)
        song_name_array = songs_dict["response"]['songs']
        for song in song_name_array:
            if not frappe.db.exists({"doctype": "Artist_songs", "song_name": song["full_title"]}):
                doc = frappe.get_doc({
                "doctype":"Artist_songs",
                "song_name": song["full_title"],
                "release_date": song["release_date_for_display"],
                "artist": name,
                "song_image": song["header_image_thumbnail_url"]
            })
                doc.insert()
                doc= frappe.get_doc("Artist", name)
                doc.append("songs", {
                    "song_name": song["full_title"],
                    "artist_name": song["artist_names"]
                })
                doc.save()
            




