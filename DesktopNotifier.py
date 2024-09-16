import time
from win10toast import ToastNotifier
from topnews import topStories

# Create a toast notification object
toaster = ToastNotifier()

# Fetch news items
newsitems = topStories()

# Loop through each news item
for newsitem in newsitems:
    # Show notification using win10toast
    toaster.show_toast(
        title=newsitem['title'].decode('utf8'),
        msg=newsitem['description'].decode('utf8'),
        duration=10  # Notification timeout in seconds
    )

    # Wait for a while before showing the next notification
    time.sleep(15)
