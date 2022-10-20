smb_path = '//1.1.1.1/eoi/python'

smb_url = smb_path.strip("/")
smb_slash_index = smb_url.find("/")

host = smb_url[:smb_slash_index]
route = smb_url[smb_slash_index:]

print(f"Host: {host}, Path: {route}")