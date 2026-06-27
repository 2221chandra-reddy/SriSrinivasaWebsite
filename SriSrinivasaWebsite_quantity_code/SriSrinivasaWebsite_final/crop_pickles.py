from PIL import Image

REF = r"C:\Users\user\.cursor\projects\c-Users-user-Downloads-SriSrinivasaWebsite-quantity-code\assets\c__Users_user_AppData_Roaming_Cursor_User_workspaceStorage_1965d31735864088878038fded6f84b5_images_image-54180b34-8263-4182-b0bf-297066d2ef41.png"
OUT = r"c:\Users\user\Downloads\SriSrinivasaWebsite_quantity_code\SriSrinivasaWebsite_final\images\pickles"

names = [
    "tomato", "mamidi", "mirchi", "allam", "chintakaya", "aavakaya", "usiri", "nimma",
    "kothemeera", "podina", "gongura", "velluli",
]

im = Image.open(REF).convert("RGB")
W, H = im.size
card_w = W // 8
header_h = 36
row_h = (H - header_h) // 2
pad_x = 22
img_top = 2
img_h = 44

for i, name in enumerate(names):
    row = 0 if i < 8 else 1
    col = i if i < 8 else i - 8
    x0 = col * card_w + pad_x
    y0 = header_h + row * row_h + img_top
    x1 = (col + 1) * card_w - pad_x
    y1 = y0 + img_h
    crop = im.crop((x0, y0, x1, y1))
    crop = crop.resize((crop.width * 8, crop.height * 8), Image.Resampling.LANCZOS)
    crop.save(f"{OUT}/{name}.jpg", quality=95)
    print(name, crop.size)
