import argparse
from PIL import Image
import sys

def make_color_transparent(input_path, target_color):
    try:
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

        print(f"✅ 透過処理が完了しました: {input_path}")
        return True

    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        return False

def parse_color(color_str):
    # "R,G,B" -> (R, G, B) に変換
    try:
        parts = color_str.split(',')
        if len(parts) != 3:
            raise ValueError
        return tuple(int(p) for p in parts)
    except Exception:
        raise argparse.ArgumentTypeError("色は R,G,B の形式で指定してください。例: 255,255,255")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="指定した色を透過に変換する PNG ツール")
    parser.add_argument("input", help="入力 PNG ファイル")
    parser.add_argument("--color", default=(200, 191, 231), type=parse_color,
                        help="透過にする色 (例: 255,255,255)")

    args = parser.parse_args()

    success = make_color_transparent(args.input, args.color)

    if success:
        print("✔ すべて正常に完了しました。Enterキーを押してください。")
    else:
        print("⚠ 処理中に問題が発生しました。Enterキーを押してください。")

    input()  # ウィンドウが即閉じるのを防ぐ

