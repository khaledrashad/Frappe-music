import frappe

def get_context(context):
    context.songs = frappe.db.get_list('Artist_songs',fields=["artist", "song_name","release_date"])
    print("\n\n\n\n",context.songs,"\n\n\n\n")
    return context