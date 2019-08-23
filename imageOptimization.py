import os
import glob
from PIL import Image

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


if __name__ == '__main__':
	# source...舐め回したいディレクトリ
	# target...保存先ディレクトリ
	dir_info = [
		{
			'source': './271/tmp/*',
			'target': './271/'
		},
		{
			'source': './287/tmp/*',
			'target': './287/'
		},
		{
			'source': './683/tmp/*',
			'target': './683/'
		}
	]
	# dir_infoを参考にsourceディレクトリの直下にある画像ファイルに均等な余白をつけ、200 * 200の正方形の画像としてtargetディレクトリの直下に保存する
	for d in dir_info:
		cnt = 1
		files = glob.glob(d['source'])
		for f_name in files:
			if(os.path.isdir(f_name)):
				continue
			im = Image.open(f_name)
			im_new = expand2square(im, (0, 0, 0)).resize((200, 200))
			im_new.save(d['target'] + 'slide' + str(cnt) + '.jpg', quality=95)
			cnt += 1

