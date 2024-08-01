import reflex as rx

def link_icon(icon: str, url: str) -> rx.Component:
  return rx.link(
    rx.html(f'<i class="nes-icon {icon} is-medium"></i>'),
    href=url,
    is_external=True
  )

    