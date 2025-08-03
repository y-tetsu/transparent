import argparse
from PIL import Image

def make_color_transparent(input_path, target_color):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        if item[:3] == target_color:
            new_data.append((*target_color, 0))  # アルファを0に
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(input_path, "PNG")

def parse_color(color_str):
    # "R,G,B" -> (R, G, B) に変換
    parts = color_str.split(',')
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("色は R,G,B の形式で指定してください。例: 255,255,255")
    return tuple(int(p) for p in parts)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="指定した色を透過に変換する PNG ツール")
    parser.add_argument("input", help="入力 PNG ファイル")
    parser.add_argument("--color", default=(200,191,231), type=parse_color, help="透過にする色 (例: 255,255,255)")

    args = parser.parse_args()

    make_color_transparent(args.input, args.color)
