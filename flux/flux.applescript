tell application "System Events"
	tell application process "Flux"
		set frontmost to true
	end tell
end tell
tell application "System Events"
	tell application process "Flux"
		tell menu bar 1
			tell menu bar item 1
				try
					with timeout of 0.1 seconds
						perform action "AXPress"
					end timeout
				end try
			end tell
		end tell
	end tell
end tell
do shell script "killall 'System Events'"
tell application "System Events"
	tell application process "Flux"
		tell menu bar 1
			tell menu bar item 1
				tell menu 1
					tell menu item "Disable"
						perform action "AXPress"
					end tell
					if menu 1 of menu item "Disable" exists then
						tell menu 1 of menu item "Disable"
							tell menu item 1
								perform action "AXPress"
							end tell
						end tell
					end if
				end tell
			end tell
		end tell
	end tell
end tell