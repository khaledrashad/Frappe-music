import frappe

def get_context(context):
    name = frappe.request.args.get('name')
    context.songs = frappe.db.get_list(
        'Artist_songs',
        fields=["artist", "song_name", "release_date"],
        filters={"artist": name}
    )
    print("\n\n\n\n", context.songs, "\n\n\n\n")
    return context