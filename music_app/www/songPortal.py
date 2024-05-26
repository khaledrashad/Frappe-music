import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_paginated_songs(page_number=1, page_size=10):
    page_number = int(page_number)
    page_size = int(page_size)
    start = (page_number - 1) * page_size

    songs = frappe.db.get_list('Artist_songs', fields=['name', 'artist', 'song_image'], start=start, limit=page_size)
    total_songs = frappe.db.count('Artist_songs')

    return {
        'songs': songs,
        'total_songs': total_songs,
        'page_number': page_number,
        'page_size': page_size
    }