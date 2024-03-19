import reflex as rx
import newlife.styles.styles as styles

from newlife.components.image_galery import image_galery
from newlife.styles.styles import Color, Size, Font
from newlife.components.products_card import products_card



def products() -> rx.Component:
    return rx.center(
        rx.script(src="/js/script.js"),
        rx.html('<script src="https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.min.js"></script>'),
        rx.vstack(
            rx.box(
                rx.box(
                    rx.box(
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Creatina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Pre workout','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Mass gainer','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Multivitamínicos','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Multivitamínicos','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        rx.box(products_card('Proteina','/instalaciones/2.webp'),class_name="swiper-slide",),
                        class_name="swiper-wrapper",
                    ),
                    rx.box(class_name='swiper-pagination'), 
                    class_name="swiper mySwiper",
                ),
                class_name="movies container",
            ),
        ),
    )
