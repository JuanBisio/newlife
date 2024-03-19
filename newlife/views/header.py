import reflex as rx
import newlife.styles.head as head

from newlife.styles.styles import Color, Size, Font
from newlife.components.slide_header import slide_header



def header(color_bg) -> rx.Component:
    return rx.chakra.hstack(
        rx.html('<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>'),
        rx.script(src='/js/header.js'), 
        rx.box(
            rx.box(
                rx.box(slide_header(color_bg,'/header/CompressFondo3.webp'), class_name='swiper-slide'),
                rx.box(slide_header(color_bg,'/instalaciones/5.webp'), class_name='swiper-slide'),
                rx.box(slide_header(color_bg,'/instalaciones/7.webp'), class_name='swiper-slide'),
                class_name='swiper-wrapper'
            ),
            rx.box(class_name='swiper-pagination'),
            class_name='swiper mySwiper',
        ),
        stylesheets=head.STYLESHEETS,
    )
