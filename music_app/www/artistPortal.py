import frappe

def get_context(context):
    context.artist = frappe.db.get_list('Artist',fields=["artist_name", "artist_image"])
    return context
