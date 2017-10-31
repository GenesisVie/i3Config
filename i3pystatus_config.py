from i3pystatus import Status

status = Status(standalone=True)


status.register("clock",
	format="   %B %-d, %H:%M",
	on_leftclick= ["/usr/local/bin/orage_toggle"],
)

status.register("network",
    interface = "wlp2s0",
    hints = {"markup": "pango"},
    format_up = "<span color=\"#707880\">{essid}</span> {bytes_recv:6.1f}KiB",
    format_down = "",
    dynamic_color = True,
    )

status.register("pulseaudio",
	format="  {volume}",
	format_muted="  {volume}",
)

status.register("backlight",
    interval=10,
    format=" {percentage:.0f}%",
    backlight="intel_backlight",)


status.register("battery",
	format="  {consumption:.2f}W {status} {percentage:.0f}",
	full_color="#FFFFFF",
	color="#FFFFFF",
	charging_color="#FFFFFF",
	alert=True,
	alert_percentage=7,
	status={
		"DIS": " ",
		"CHR": " ",
		"FULL": " ",
	},
)
# Music
status.register("now_playing",
    format=" {status} {artist} - {title}",
    status={
        'stop': '  ',
        'play': '  ',
        'pause': '  '
    },
)

status.register("window_title",
	 format = "{title}",
	 empty_title="",
	 always_show = "False",


)


status.run()
