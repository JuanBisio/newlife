# import reflex as rx
# from newlife.styles.styles import Color, Size, Font



# def form_control(input_type, placeholder, error,width=['20em','25em','25em','40em','60em'],name='text') -> rx.Component:
#     return rx.chakra.vstack(
#         rx.chakra.form_control(
#             rx.chakra.input(
#                 placeholder=placeholder,
#                 on_blur=FormErrorState.set_name,
#                 name=name,
#                 type_=input_type,
#                 focus_border_color=Color.DARK_RED.value,
#                 error_border_color='#777771',
#                 border=f"1px dotted #777771",
#                 _hover={
#                     'border': f'1px dotted {Color.DARK_RED.value}'
#                 },
#             ),
#             rx.cond(
#                 FormErrorState.is_error,
#                 rx.chakra.form_error_message(
#                     error
#                 ),
#             ),
#             is_invalid=FormErrorState.is_error,
#             is_required=True,
#         ),
#         width=width
#     )
