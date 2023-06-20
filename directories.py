import os
import glob

dirname = os.path.dirname(__file__)

jewelry_photo_common = os.path.join(dirname, 'images/jewelry/photo_common')
jewelry_photo_common_path = os.path.join(jewelry_photo_common, '*')

jewelry_photo_masters = os.path.join(dirname, 'images/jewelry/photo_masters')
jewelry_photo_masters_path = os.path.join(jewelry_photo_masters, '*')

masters_paths = sorted(glob.glob(jewelry_photo_masters_path))
photo_paths = sorted(glob.glob(jewelry_photo_common_path))

embroidery_photo_common = os.path.join(dirname, 'images/embroidery/photo_common')
embroidery_photo_common_path = os.path.join(embroidery_photo_common, '*')

embroiderers_photos = os.path.join(dirname, 'images/embroidery/embroiderers_photos')
embroiderers_photo_path = os.path.join(embroiderers_photos, '*')

embroiderers_paths = sorted(glob.glob(embroiderers_photo_path))
embroidery_photo_paths = sorted(glob.glob(embroidery_photo_common_path))
