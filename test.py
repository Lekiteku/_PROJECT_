import sys

# Your message
your_message = "Your message here"

# Get the size of the message in bytes
message_size = sys.getsizeof(your_message)

# Print the size of the message
print(f"Size of the message: {message_size} bytes")
