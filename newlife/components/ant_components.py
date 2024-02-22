import reflex as rx 
from newlife.styles.styles import Color

class Carrousel(rx.Component):
    library = 'antd'
    tag = 'Carousel'
    height = '160px'
    color = '#fff'
    lineHeight = '160px'
    textAlign = 'center'
    background = '#364d79'
carrousel_antd = Carrousel.create

class FloatButton(rx.Component):
    library = 'antd'
    tag = 'FloatButton'
    icon = rx.chakra.image(src='/icons/WhatsappB.svg')
    href = 'https://api.whatsapp.com/send/?phone=5493584299645&text&app_absent=0'
    target = '_blank'
    badge = {'dot':True, 'color':Color.DARK_RED.value}
    colorFillContent = Color.PRIMARY.value
    
float_button = FloatButton.create
