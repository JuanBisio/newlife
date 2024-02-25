import reflex as rx
from newlife.styles.styles import Color


class FloatButton(rx.Component):
    library = 'antd'
    tag = 'FloatButton'
    icon = rx.chakra.image(src='/iconsImage/WhatsappB.webp',width='24px', height='auto')
    href = 'https://api.whatsapp.com/send/?phone=5493584299645&text&app_absent=0'
    target = '_blank'
    badge = {'dot': True, 'color': Color.DARK_RED.value}
    colorFillContent = Color.PRIMARY.value


float_button = FloatButton.create
