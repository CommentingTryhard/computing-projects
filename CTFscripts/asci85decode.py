import base64

encoded_string = "<~3DE^u0JR<M,#g<H/oWa1@U_J^0hj$6:-Cd&:1>t52#~>"

try:
    decoded = base64.a85decode(encoded_string[2:-2])  # Remove "<~" and "~>"
    print(decoded)
except Exception as e:
    print(f"Decoding error: {e}")
