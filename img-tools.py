import pyautogui as pa
from skimage.metrics import structural_similarity as ssim

pa.click()

a = 1
b = 1
ssim(a,b)